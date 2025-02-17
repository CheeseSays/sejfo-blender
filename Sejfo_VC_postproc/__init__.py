import bpy
from bpy.types import Scene
from bpy.props import PointerProperty, FloatProperty, IntProperty, StringProperty
from bpy.utils import register_class, unregister_class
from math import radians
from . rotation_repair import AxisMenu, SCENE_OT_RotationKeyer, SCENE_PT_RotationKeyerPanel, SCENE_OT_RotationSingleKeyer
from . action_killer import SCENE_OT_ActionKiller, ActionKiller
from . material_replacer import SCENE_OT_MaterialReplacer, SCENE_PT_MaterialReplacer, SCENE_OT_FetchMaterials, MaterialMenu, SCENE_PT_CustomMaterialLibrary, SCENE_OT_CubeUV
        
def register():
    register_class(AxisMenu)
    register_class(SCENE_OT_RotationKeyer)
    register_class(SCENE_PT_RotationKeyerPanel)
    register_class(SCENE_OT_RotationSingleKeyer)
    register_class(SCENE_OT_ActionKiller)
    register_class(ActionKiller)
    register_class(SCENE_OT_MaterialReplacer)
    register_class(SCENE_PT_MaterialReplacer)
    register_class(SCENE_OT_FetchMaterials)
    register_class(MaterialMenu)
    register_class(SCENE_OT_CubeUV)
    register_class(SCENE_PT_CustomMaterialLibrary)
    Scene.material_menu = PointerProperty(type=MaterialMenu)
    Scene.axis_menu = PointerProperty(type=AxisMenu)
    Scene.Absolute_1 = FloatProperty(name="Absolute_1", default=radians(180.0), subtype='ANGLE', unit='ROTATION')
    Scene.start_frame = IntProperty(name="Start Frame", default=1)
    Scene.end_frame = IntProperty(name="End Frame", default=250)
    Scene.material_library_path = StringProperty(name="Material Library Path", subtype='FILE_PATH')

def unregister():
    unregister_class(AxisMenu)
    unregister_class(SCENE_OT_RotationKeyer)
    unregister_class(SCENE_PT_RotationKeyerPanel)
    unregister_class(SCENE_OT_RotationSingleKeyer)
    unregister_class(SCENE_OT_ActionKiller)
    unregister_class(ActionKiller)
    unregister_class(SCENE_OT_MaterialReplacer)
    unregister_class(SCENE_PT_MaterialReplacer)
    unregister_class(SCENE_OT_FetchMaterials)
    del Scene.material_menu
    del Scene.axis_menu
    del Scene.Absolute_1
    del Scene.start_frame
    del Scene.end_frame
    del Scene.material_library_path

if __name__ == "__main__":
    register()