import bpy
from bpy.types import Operator, Panel, PropertyGroup
from bpy.props import EnumProperty
from bpy.ops import object, uv

#region PROPERTIES

class MaterialMenu(PropertyGroup):
    material_options = [
        ('OPTION_1', "Glass", "Glass - Default"),
        ('OPTION_2', "Wood", "plywood"),
        ('OPTION_3', "Aluminium", "Aluminium - Polished"),
    ]
    dropdown: EnumProperty(
        items=material_options,
        name="Material Type",
        description="Material to replace",
        default='OPTION_1'
    ) #type: ignore

#endregion

#region OPERATORS

class SCENE_OT_FetchMaterials(Operator):
    bl_idname = "scene.fetch_materials"
    bl_label = "Fetch Materials"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Add file browser functionality
        filepath = bpy.path.abspath(context.scene.material_library_path) if context.scene.material_library_path else "G:\Andreas Wetter\Blender Assets\Asset Library\Materials\Sejfo_Standard_Materials.blend"
        if not filepath:
            self.report({'ERROR'}, "Please select a .blend file in the panel settings")
            return {'CANCELLED'}
            
        # Load materials from selected file
        try:
            with bpy.data.libraries.load(filepath) as (data_from, data_to):
                data_to.materials = data_from.materials
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, f"Error loading materials: {str(e)}")
            return {'CANCELLED'}

        

class SCENE_OT_MaterialReplacer(Operator):
    bl_idname = "scene.material_replacer"
    bl_label = "Replace Material"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Get the selected option from the dropdown
        selected_option = context.scene.material_menu.dropdown
        material_map = {
            'OPTION_1': ('glass', 'Glass - Default'),
            'OPTION_2': ('wood', 'plywood'),
            'OPTION_3': ('aluminium', 'Aluminium - Polished'),
        }
        
        search_term, replacement_name = material_map[selected_option]
        
        # Get all selected objects in the scene
        for obj in context.selected_objects:
            # Check if object has materials
            if obj.material_slots:
                # Check each material slot
                for slot in obj.material_slots:
                    # If material exists and contains the search term
                    if slot.material and search_term in slot.material.name.lower():
                        # Replace with the selected material
                        replacement = bpy.data.materials.get(replacement_name)
                        if replacement:
                            slot.material = replacement
        
        return {'FINISHED'}
    
class SCENE_OT_CubeUV(Operator):
    bl_idname = "scene.cube_uv"
    bl_label = "Fix Texture Mapping"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        object.mode_set(mode='EDIT')
        uv.cube_project()
        object.mode_set(mode='OBJECT')
        return {'FINISHED'}
    
#endregion

#region PANELS

class SCENE_PT_MaterialReplacer(Panel):
    bl_idname = "SCENE_PT_MaterialReplacer"
    bl_label = "Material Replacer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SEJFO"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon="MATERIAL")

    def draw(self, context):
        material_menu = context.scene.material_menu
        layout = self.layout
        layout.label(text="")
        row = layout.row()
        layout.prop(material_menu, "dropdown")
        row = layout.row()
        row.scale_y = 1.0
        row.operator("scene.fetch_materials")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("scene.material_replacer")
        row = layout.row()
        row.scale_y = 1.0
        row.operator("scene.cube_uv")

class SCENE_PT_CustomMaterialLibrary(Panel):
    bl_idname = "SCENE_PT_CustomMaterialLibrary"
    bl_label = "Custom Material Library"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SEJFO"
    bl_options = {"DEFAULT_CLOSED"}
    bl_parent_id = "SCENE_PT_MaterialReplacer"

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon="FILEBROWSER")

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Select a .blend file containing materials.")
        row = layout.row()
        row.label(text="Defaults to Sejfo_Standard_Materials.blend")
        layout.prop(context.scene, "material_library_path", text="Custom Material Library")

#endregion

'''def register():
    bpy.utils.register_class(SCENE_OT_MaterialReplacer)
    bpy.utils.register_class(SCENE_PT_MaterialReplacer)
    bpy.utils.register_class(SCENE_OT_FetchMaterials)
    bpy.types.Scene.material_library_path = bpy.props.StringProperty(name="Material Library Path", subtype='FILE_PATH')
    bpy.utils.register_class(MaterialMenu)
    bpy.utils.register_class(SCENE_OT_CubeUV)
    bpy.types.Scene.material_menu = bpy.props.PointerProperty(type=MaterialMenu)
    bpy.utils.register_class(SCENE_PT_CustomMaterialLibrary)

def unregister():
    bpy.utils.unregister_class(SCENE_OT_MaterialReplacer)
    bpy.utils.unregister_class(SCENE_PT_MaterialReplacer)
    bpy.utils.unregister_class(SCENE_OT_FetchMaterials)
    bpy.utils.unregister_class(MaterialMenu)
    bpy.utils.unregister_class(SCENE_OT_CubeUV)
    bpy.utils.unregister_class(SCENE_PT_CustomMaterialLibrary)
    del bpy.types.Scene.material_library_path
    del bpy.types.Scene.material_menu

if __name__ == "__main__":
    register()'''