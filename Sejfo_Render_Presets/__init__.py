import bpy
from bpy.types import Operator, Panel
from bpy.utils import register_class, unregister_class

#region EEVEE

class SCENE_OT_EeveeSettings(Operator):
    bl_idname = 'scene.eevee_settings'
    bl_label = 'Eevee Settings'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.data.scenes["Scene"].render.engine = 'BLENDER_EEVEE_NEXT'

        rs = bpy.data.scenes["Scene"].render
        display = bpy.data.scenes["Scene"].display_settings
        view = bpy.data.scenes["Scene"].view_settings
        color = bpy.data.scenes["Scene"].sequencer_colorspace_settings
        e = context.scene.eevee
        
        # Sampling
            # Viewport
        e.taa_samples = 16
        e.use_taa_reprojection = True
        e.use_shadow_jitter_viewport = True
            # Render
        e.taa_render_samples = 256
            # Shadows
        e.use_shadows = True
        e.shadow_ray_count = 1
        e.shadow_step_count = 6
        e.use_volumetric_shadows = False
        e.volumetric_shadow_samples = 16
        e.shadow_resolution_scale = 1
            # Advanced
        e.light_threshold = 0.01
        # Clamping
            # Surface
        e.clamp_surface_direct = 0
        e.clamp_surface_indirect = 10
            # Volume
        e.clamp_volume_direct = 0
        e.clamp_volume_indirect = 0
        # Raytracing
        e.use_raytracing = True
        e.ray_tracing_method = 'SCREEN'
        e.ray_tracing_options.resolution_scale = '2'
        e.ray_tracing_options.trace_max_roughness = 0.5
            # Screen Tracing
        e.ray_tracing_options.screen_trace_quality = 0.25
        e.ray_tracing_options.screen_trace_thickness = 0.2
            # Denoising
        e.ray_tracing_options.use_denoise = True
        e.ray_tracing_options.denoise_spatial = True
        e.ray_tracing_options.denoise_bilateral = True
            # Fast GI Approximation
        e.fast_gi_method = 'GLOBAL_ILLUMINATION'
        e.fast_gi_resolution = '2'
        e.fast_gi_ray_count = 2
        e.fast_gi_step_count = 8
        e.fast_gi_quality = 0.25
        e.fast_gi_distance = 0
        e.fast_gi_thickness_near = 0.25
        e.fast_gi_thickness_far = 0.785398
        e.fast_gi_bias = 0.05
        # Volumes
        e.volumetric_tile_size = '8'
        e.volumetric_samples = 64
        e.volumetric_sample_distribution = 0.8
        e.volumetric_ray_depth = 16
            # Custom Range
        e.use_volume_custom_range = True
        e.volumetric_start = 0.1
        e.volumetric_end = 100.0
        # Performance
        rs.use_high_quality_normals = False
            # Memory
        e.shadow_pool_size = '512'
        e.gi_irradiance_pool_size = '16'
            # Viewport
        rs.preview_pixel_size = 'AUTO'
            # Compositor
        rs.compositor_device = 'GPU'
        rs.compositor_precision = 'AUTO'
        # Curves
        rs.hair_type = 'STRAND'
        rs.hair_subdiv = 0
        # Simplify
        rs.use_simplify = False
        # Depth of Field
        e.bokeh_max_size = 100.0
        e.bokeh_threshold = 1.0
        e.bokeh_neighbor_max = 10.00
        e.use_bokeh_jittered = False
        # Motion Blur
        rs.use_motion_blur = False
        # Film
        rs.filter_size = 1.5
        rs.film_transparent = True
        e.use_overscan = True
        e.overscan_size = 3.0
        # Freestyle
        rs.use_freestyle = False
        # Color Management
        display.display_device = 'sRGB'
        view.view_transform = 'Standard'
        view.look = 'None'
        view.exposure = 0.0
        view.gamma = 1.0
        color.name = 'sRGB'
            # Display
        view.use_hdr_view = False
            # Use Curves
        view.use_curve_mapping = False


        return {'FINISHED'}

#endregion
#region CYCLES
    
class SCENE_OT_CyclesSettings(Operator):
    bl_idname = 'scene.cycles_settings'
    bl_label = 'Cycles Settings'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.data.scenes["Scene"].render.engine = 'CYCLES'

        rs = bpy.data.scenes["Scene"].render
        display = bpy.data.scenes["Scene"].display_settings
        view = bpy.data.scenes["Scene"].view_settings
        color = bpy.data.scenes["Scene"].sequencer_colorspace_settings
        
        c = context.scene.cycles
        cc = context.scene.cycles_curves

        c.feature_set = 'SUPPORTED'
        c.device = 'GPU'

        # Sampling
            # Viewport
        c.use_preview_adaptive_sampling = True
        c.preview_adaptive_threshold = 0.1
        c.preview_samples = 32
        c.preview_adaptive_min_samples = 0
        c.use_preview_denoising = True
            # Render
        c.use_adaptive_sampling = True
        c.adaptive_threshold = 0.01
        c.samples = 500
        c.adaptive_min_samples = 0
        c.time_limit = 0
            # Denoise
        c.use_denoising = True
        c.denoiser = 'OPENIMAGEDENOISE'
        c.denoising_input_passes = 'RGB_ALBEDO_NORMAL'
        c.denoising_prefilter = 'ACCURATE'
        c.denoising_quality = 'HIGH'
        c.denoising_use_gpu = True
            # Lights
        c.use_light_tree = True
            # Advanced
        c.sampling_pattern = 'AUTOMATIC'
        c.seed = 0
        c.use_animated_seed = True
        c.sample_offset = 0
        c.min_light_bounces = 0
        c.min_transparent_bounces = 0
        # Light Paths
            # Max Bounces
        c.max_bounces = 32
        c.diffuse_bounces = 32
        c.glossy_bounces = 32
        c.transmission_bounces = 32
        c.volume_bounces = 32
        c.transparent_max_bounces = 32
            # Clamping
        c.sample_clamp_direct = 0
        c.sample_clamp_indirect = 10
            # Caustics
        c.blur_glossy = 1.0
        c.caustics_reflective = False
        c.caustics_refractive = False
            # Fast GI Approximation
        c.use_fast_gi = True
        # Volumes
        c.volume_step_rate = 1
        c.volume_preview_step_rate = 1
        c.volume_max_steps = 1024
        # Curves
        cc.shape = 'RIBBONS'
        cc.subdivisions = 2
            # Viewport Display
        rs.hair_type = 'STRAND'
        rs.hair_subdiv = 0
        # Simplify
        rs.use_simplify = False
        # Motion Blur
        rs.use_motion_blur = False
        # Film
        c.film_exposure = 1.0
            # Pixel Filter
        c.pixel_filter_type = 'BLACKMAN_HARRIS'
        c.filter_width = 1.5
            # Transparent
        rs.film_transparent = True
        c.film_transparent_glass = True
        c.film_transparent_roughness = 0.1
        # Performance
            # Compositor
        rs.compositor_device = 'GPU'
        rs.compositor_precision = 'AUTO'
            # Threads
        rs.threads_mode = 'AUTO'
        rs.threads = 32
            # Memory
        c.use_auto_tile = True
        c.tile_size = 2048
            # Final Render
        rs.use_persistent_data = True
            # Viewport
        rs.preview_pixel_size = 'AUTO'
        # Freestyle
        rs.use_freestyle = False
        # Color Management
        display.display_device = 'sRGB'
        view.view_transform = 'Standard'
        view.look = 'None'
        view.exposure = 0.0
        view.gamma = 1.0
        color.name = 'sRGB'
        # Display
        view.use_hdr_view = False
        # Use Curves
        view.use_curve_mapping = False
        


        return {'FINISHED'}
#endregion
#region PANELS
class SCENE_PT_RenderSettings(Panel):
    bl_label = 'Render Presets'
    bl_idname = 'SCENE_PT_RenderSettings'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'SEJFO'
    bl_options = {"DEFAULT_CLOSED"}

    def draw_header(self, context):
        layout = self.layout
        layout.label(text='', icon='PRESET')

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text='For animations or quick renders')
        row.operator('scene.eevee_settings', text='Eevee')
        row = layout.row()
        row.label(text='For realistic renders (slow)')
        row.operator('scene.cycles_settings', text='Cycles')

#endregion
#region REGISTER

def register():
    register_class(SCENE_OT_EeveeSettings)
    register_class(SCENE_OT_CyclesSettings)
    register_class(SCENE_PT_RenderSettings)

def unregister():
    unregister_class(SCENE_OT_EeveeSettings)
    unregister_class(SCENE_OT_CyclesSettings)
    unregister_class(SCENE_PT_RenderSettings)

#endregion

if __name__ == '__main__':
    register()