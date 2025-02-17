import bpy
from bpy.types import Operator, Panel, Object, PropertyGroup
from bpy.props import EnumProperty


class AxisMenu(PropertyGroup):
    axis_options = [
        ('OPTION_1', "X", "Rotation Axis X"),
        ('OPTION_2', "Y", "Rotation Axis Y"),
        ('OPTION_3', "Z", "Rotation Axis Z"),
    ]
    dropdown: EnumProperty(
        items=axis_options,
        name="Axis",
        description="Rotation Axis",
        default='OPTION_1'
    ) #type: ignore

#region OPERATORS

class SCENE_OT_RotationKeyer(Operator):
    bl_idname = "scene.rotation_keyer"
    bl_label = "Fix Rotation"
    bl_options = {'REGISTER', 'UNDO'}
    
    def rotation_correction(self, context, obj: Object, rot_axis: float, rot_1: float, frame: int, option: int):
        """Corrects the rotation of the object at a given frame and keyframes it.

        Args:
            obj (Object): The selected object.
            rot_axis (float): The chosen axis for correction.
            rot_1 (float): The desired rotation value.
            frame (int): The frame to correct.
            option (int): The index of the rotation axis.
        """
        if rot_axis != rot_1 and rot_axis != -rot_1:
            context.scene.frame_set(frame)
            obj.rotation_euler[option] = rot_1
            obj.keyframe_insert(data_path="rotation_euler", index=option, frame=frame)

    def execute(self, context):
        if context.active_object is None:
            self.report({'ERROR'}, "No active object")
            return {'CANCELLED'}
        
        else:
            obj = context.object
            axis = context.scene.axis_menu.dropdown
            rot_1 = context.scene.Absolute_1

            if axis == 'OPTION_1':
                rot_axis = obj.rotation_euler.x
                option = 0
                    
            elif axis == 'OPTION_2':
                rot_axis = obj.rotation_euler.y
                option = 1
                
            elif axis == 'OPTION_3':
                rot_axis = obj.rotation_euler.z
                option = 2
                
            else:
                self.report({'ERROR'}, "Invalid axis")
                return {'CANCELLED'}
            
            for frame in range(context.scene.start_frame, context.scene.end_frame + 1):
                self.rotation_correction(obj, rot_axis, rot_1, frame, option)                
        return {'FINISHED'}
    
class SCENE_OT_RotationSingleKeyer(Operator):
    bl_idname = "scene.rotation_single_keyer"
    bl_label = "Fix Current Frame Only"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if context.active_object is None:
            self.report({'ERROR'}, "No active object")
            return {'CANCELLED'}
        
        else:
            obj = context.object
            axis = context.scene.axis_menu.dropdown
            rot_1 = context.scene.Absolute_1

            if axis == 'OPTION_1':
                rot_axis = obj.rotation_euler.x
                option = 0
                    
            elif axis == 'OPTION_2':
                rot_axis = obj.rotation_euler.y
                option = 1
                
            elif axis == 'OPTION_3':
                rot_axis = obj.rotation_euler.z
                option = 2
                
            else:
                self.report({'ERROR'}, "Invalid axis")
                return {'CANCELLED'}    
            
            frame = context.scene.frame_current
            SCENE_OT_RotationKeyer.rotation_correction(self, obj, rot_axis, rot_1, frame, option)
        return {'FINISHED'}

#endregion
#region PANELS

class SCENE_PT_RotationKeyerPanel(Panel):
    bl_idname = "SCENE_PT_RotationKeyerPanel"
    bl_label = "Rotation Fixer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SEJFO'
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        layout = self.layout
        layout.label(text="", icon="EMPTY_AXIS")

    def draw(self, context):
        layout = self.layout
        axis_menu = context.scene.axis_menu
        layout.prop(axis_menu, "dropdown")
        layout.prop(context.scene, "Absolute_1", text="Absolute Rotation")
        layout.prop(context.scene, "start_frame", text="Start Frame")
        layout.prop(context.scene, "end_frame", text="End Frame")
        layout.operator("scene.rotation_keyer")
        layout.operator("scene.rotation_single_keyer")

#endregion