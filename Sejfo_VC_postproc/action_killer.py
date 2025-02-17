import bpy
from bpy.types import Panel, Operator
from bpy.props import IntProperty

class SCENE_OT_ActionKiller(Operator):
    bl_idname = "scene.action_killer"
    bl_label = "Remove all unecessary animation"
    bl_options = {'REGISTER','UNDO'}

    min_frames: IntProperty(name="Minimum Frames", default=3, min=1, description="Minimum number of frames an action must have to be kept") #type: ignore

    def execute(self, context):
        actions_to_remove = [action for action in bpy.data.actions if all(len(fcurve.keyframe_points) < self.min_frames for fcurve in action.fcurves)]

        for action in actions_to_remove:
            if action.users > 0:
                for obj in bpy.data.objects:
                    if obj.animation_data and obj.animation_data.action == action:
                        obj.animation_data_clear()
            bpy.data.actions.remove(action)

        self.report({'INFO'}, f"Removed {len(actions_to_remove)} actions with less than {self.min_frames} frames.")
        return {'FINISHED'}

class ActionKiller (Panel):
    bl_idname = "SCENE_PT_ActionKiller"
    bl_label = "Action Killer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SEJFO"
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon="KEYTYPE_EXTREME_VEC")

    def draw(self, context):
        layout = self.layout
        
        layout.label(text="")
        row = layout.row()
        row.scale_y = 3.0
        row.operator("scene.action_killer")

