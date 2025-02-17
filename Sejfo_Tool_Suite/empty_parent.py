import bpy
from bpy.types import Operator, Panel
from bpy.ops import object


class OBJECT_OT_EmptyParent(Operator):
    bl_idname = "object.empty_parent"
    bl_label = "Create Transform Parents"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        for obj in context.selected_objects:
            object.empty_add(location=obj.location)
            empty = context.active_object
            empty.name = obj.name + "_transform"
            obj.parent = empty
            obj.location = (0, 0, 0)

        return {'FINISHED'}
    

class OBJECT_PT_EmptyParent(Panel):
    bl_label = "VC Transform Parent"
    bl_idname = "OBJECT_PT_EmptyParent"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SEJFO'
    bl_context = "objectmode"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        self.layout.label(text="", icon='ORIENTATION_PARENT')

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("object.empty_parent")
