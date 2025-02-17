import bpy
from bpy.types import Panel, Operator, PropertyGroup, Collection
from bpy.ops import object
from bpy.props import PointerProperty

def update_collection(self, context):
    print(f"Selected Collection: {self.selCollection.name}")

class MyProperties(PropertyGroup):
    selCollection: PointerProperty(
        name="Select Collection",
        type=Collection,
        update=update_collection
    ) #type: ignore

#region OPERATORS




#region _DensityFind
class SCENE_OT_DensityFind(Operator):
     bl_idname = "scene.find_by_density"
     bl_label = "Find by highest density"
     bl_options = {'REGISTER', 'UNDO'}

     def execute(self, context):
        most_vertices_object = None
        highest_vertex_count = 0

        for obj in context.scene.objects:
            if obj.type == 'MESH':
                vertex_count = len(obj.data.vertices)
                
                if vertex_count > highest_vertex_count:
                    highest_vertex_count = vertex_count
                    most_vertices_object = obj

        if most_vertices_object:
            object.select_all(action='DESELECT')
            most_vertices_object.select_set(True)
            context.view_layer.objects.active = most_vertices_object

        return {'FINISHED'}
#endregion

#region _objDimCopy

class SCENE_OT_objDimCopy(Operator):
    bl_idname = "scene.copy_obj_dim"
    bl_label = "Copy Dimensions from selected"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        CopyLimit_X = context.object.dimensions.x
        CopyLimit_Y = context.object.dimensions.y
        CopyLimit_Z = context.object.dimensions.z

        CopyMargin = context.scene.Margin

        context.scene.Limit_X = CopyLimit_X * 1000 + CopyMargin
        context.scene.Limit_Y = CopyLimit_Y * 1000 + CopyMargin
        context.scene.Limit_Z = CopyLimit_Z * 1000 + CopyMargin

        context.scene.Lower_X = CopyLimit_X * 1000 - CopyMargin
        context.scene.Lower_Y = CopyLimit_Y * 1000 - CopyMargin
        context.scene.Lower_Z = CopyLimit_Z * 1000 - CopyMargin

        print(CopyLimit_X,CopyLimit_Y,CopyLimit_Z)

        return{'FINISHED'}
    
#endregion

#region _screwfinder
       
class SCENE_OT_screwfinder(Operator):
    
    bl_idname = "scene.find_objects"
    bl_label = "Find objects"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        
        Limit_X = context.scene.Limit_X / 1000
        Limit_Y = context.scene.Limit_Y / 1000 
        Limit_Z = context.scene.Limit_Z / 1000
        
        Lower_X = context.scene.Lower_X / 1000
        Lower_Y = context.scene.Lower_Y / 1000
        Lower_Z = context.scene.Lower_Z / 1000
    
        for i in context.scene.objects:
            if Lower_X <= i.dimensions.x <= Limit_X and Lower_Y <= i.dimensions.y <= Limit_Y and Lower_Z <= i.dimensions.z <= Limit_Z:
                i.select_set(True)
            else:
                i.select_set(False)
        return {'FINISHED'}
#endregion

#region _bundler

class SCENE_OT_bundler(Operator):
     
     bl_idname = "scene.bundle_objects"
     bl_label = "Bundle and Hide"
     bl_options = {'REGISTER', 'UNDO'}

     def execute(self, context):
        #Create new collection
        col = bpy.data.collections.new(name="New Collection")
        context.scene.collection.children.link(col)
        
        #Add selected object into new collection
        for obj in context.selected_objects:
            for other_col in obj.users_collection:
                other_col.objects.unlink(obj)
            if obj.name not in col.objects:
                col.objects.link(obj)
        
        #Hide collection from viewport
        bpy.data.collections['New Collection'].hide_viewport = True



        return{'FINISHED'}
     
#endregion

#region _CollectionMover

class SCENE_OT_CollectionMover(Operator):

    bl_idname = "scene.move_to_collection"
    bl_label  = "Move to Collection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        selCollection = context.scene.selCol.selCollection

        for obj in context.selected_objects:
            for other_col in obj.users_collection:
                other_col.objects.unlink(obj)
            if obj.name not in selCollection.objects:
                selCollection.objects.link(obj)

        print(f"Moving objects to collection")
        return {'FINISHED'}
    
#endregion

#endregion
#region PANELS

class ObjectFinder (Panel):
    bl_space_type = 'VIEW_3D'
    
    bl_idname = "SCENE_PT_objectfinderpanel"
    bl_label = "Object Finder"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SEJFO"
    bl_options = {"DEFAULT_CLOSED"}
    
    def draw_header(self, context):
            self.layout.label(text = "", icon = "VIEWZOOM")
    
    def draw(self, context):
         self.layout.label(text="")

class DimensionDefiner (Panel):
        bl_idname = "SCENE_PT_Dimension_Definer"
        bl_label = "Dimensions"
        bl_parent_id = "SCENE_PT_objectfinderpanel"
        bl_space_type = "VIEW_3D"
        bl_region_type = "UI"
        bl_category = "SEJFO"
        bl_options = {"DEFAULT_CLOSED"}

        def draw_header(self, context):
            layout = self.layout
            layout.label(text="", icon="SELECT_SET")
            
        def draw(self, context):   
            layout = self.layout
        
            obj = context.scene

            layout.label(text="")
            row = layout.row()
            row.scale_y = 1.0
            layout.prop(obj, "Margin", text="Margin")
            row.operator("scene.copy_obj_dim")
            
            row = layout.row()
            row.label(text="Define max dimensions in mm")
            
            layout.prop(obj, "Limit_X", text="X")
            layout.prop(obj, "Limit_Y", text="Y")
            layout.prop(obj, "Limit_Z", text="Z")
            
            row = layout.row()
            row.label(text="Define minimum dimensions in mm")
            
            layout.prop(obj, "Lower_X", text="X")
            layout.prop(obj, "Lower_Y", text="Y")
            layout.prop(obj, "Lower_Z", text="Z")
        
            layout.label(text="")
            row = layout.row()
            row.scale_y = 3.0
            row.operator("scene.find_objects")

class ObjectBundler (Panel):
        bl_idname = "SCENE_PT_Object_Bundler"
        bl_label = "Bundler"
        bl_parent_id = "SCENE_PT_objectfinderpanel"
        bl_space_type = "VIEW_3D"
        bl_region_type = "UI"
        bl_category = "SEJFO"
        bl_options = {"DEFAULT_CLOSED"}

        def draw_header(self, context):
            layout = self.layout
            layout.label(text="", icon="OUTLINER_COLLECTION")
            
        def draw(self, context):  
            layout = self.layout

            layout.label(text="")
            row = layout.row()
            row.scale_y = 3.0
            row.operator("scene.bundle_objects")

class DensityFinder (Panel):
        bl_idname = "SCENE_PT_Density_Finder"
        bl_label = "Find densest object"
        bl_parent_id = "SCENE_PT_objectfinderpanel"
        bl_space_type = "VIEW_3D"
        bl_region_type = "UI"
        bl_category = "SEJFO"

        def draw_header(self, context):
            layout = self.layout
            layout.label(text="", icon="MOD_VERTEX_WEIGHT")

        def draw(self, context):
             layout = self.layout
             layout.label(text="")
             row = layout.row()
             row.scale_y = 3.0
             row.operator("scene.find_by_density")
     
class CollectionSelector (Panel):
        bl_idname = "SCENE_PT_Collection_Selector"
        bl_label = "Predefine Collection"
        bl_parent_id = "SCENE_PT_Object_Bundler"
        bl_space_type = "VIEW_3D"
        bl_region_type = "UI"
        bl_category = "SEJFO"
        bl_options = {"DEFAULT_CLOSED"}

        def draw_header(self, context):
            layout = self.layout
            layout.label(text="")
            
        def draw(self, context):  
            layout = self.layout
        
            obj = context.scene
            sCol = obj.selCol

            layout.prop(sCol, "selCollection", text="")
            row = layout.row()
            row.scale_y = 3.0
            row.operator("scene.move_to_collection")

#endregion