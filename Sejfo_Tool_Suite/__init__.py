import bpy
from bpy.types import Scene
from bpy.props import IntProperty, PointerProperty, FloatProperty
from bpy.utils import register_class, unregister_class
from . object_finder import MyProperties, SCENE_OT_DensityFind, SCENE_OT_objDimCopy, SCENE_OT_screwfinder, SCENE_OT_bundler, SCENE_OT_CollectionMover, ObjectFinder, DimensionDefiner, ObjectBundler, DensityFinder, CollectionSelector
from . empty_parent import OBJECT_OT_EmptyParent, OBJECT_PT_EmptyParent

# Registration

def register():
        register_class(SCENE_OT_DensityFind)
        register_class(SCENE_OT_screwfinder)
        register_class(ObjectFinder)
        register_class(SCENE_OT_objDimCopy)
        register_class(SCENE_OT_bundler)
        register_class(MyProperties)
        register_class(SCENE_OT_CollectionMover)
        register_class(DimensionDefiner)
        register_class(ObjectBundler)
        register_class(CollectionSelector)
        register_class(DensityFinder)
        register_class(OBJECT_OT_EmptyParent)
        register_class(OBJECT_PT_EmptyParent)
        Scene.Limit_X = FloatProperty(min=1, precision=0, default=30)
        Scene.Limit_Y = FloatProperty(min=1, precision=0, default=30)
        Scene.Limit_Z = FloatProperty(min=1, precision=0, default=30)
        Scene.Lower_X = FloatProperty(min=0, precision=0, default=0)
        Scene.Lower_Y = FloatProperty(min=0, precision=0, default=0)
        Scene.Lower_Z = FloatProperty(min=0, precision=0, default=0)
        Scene.Margin = IntProperty(min=1, default=1)
        Scene.selCol = PointerProperty(type=MyProperties)
               
def unregister():
        unregister_class(SCENE_OT_DensityFind)
        unregister_class(SCENE_OT_screwfinder)
        unregister_class(ObjectFinder)
        unregister_class(SCENE_OT_objDimCopy)
        unregister_class(SCENE_OT_bundler)
        unregister_class(MyProperties)
        unregister_class(SCENE_OT_CollectionMover)
        unregister_class(DimensionDefiner)
        unregister_class(ObjectBundler)
        unregister_class(CollectionSelector)
        unregister_class(DensityFinder)
        unregister_class(OBJECT_OT_EmptyParent)
        unregister_class(OBJECT_PT_EmptyParent)
        del Scene.Limit_X
        del Scene.Limit_Y
        del Scene.Limit_Z
        del Scene.Lower_X
        del Scene.Lower_Y
        del Scene.Lower_Z
        del Scene.Margin
        del Scene.selCol
        
if __name__ == "__main__":
    register()        

