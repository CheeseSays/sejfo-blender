# SEJFO Blender Extensions
### Requires Blender 4.2+
##### Blender 3.6 compatible versions will be added in the future.

After installation of any of these extensions you'll find a SEJFO tab in your N-menu.

## Sejfo Tool Suite
This is our general purpose extension with a set of tools focused on optimising scenes comprised by large SolidWorks assemblies.
In this suite you'll find tools for finding and selecting all objects that matches a specified dimension interval (very useful for finding all screws in the scene), 
as well as a tool that helps collecting selected items and hiding them from the viewport.
A tool to identify the most dense object is included as well. This tool will select the object with most verticies, aiding you in model optimisation.

A tool to help creating a clean model hierarchy in Visual Components is included.

## Sejfo VC PostProc
This is a set of tools for cleaning up scenes exported from Visual Components using the Blenderer add-on.
### Action Killer
This tool removes all animation data for static objects. When you export a scene from VC into Blender all objects (including static objects) get animation data. Removing all the animation data for static objects results in a lighter file. 
In tests we've done with the simulations we create the animation data on static objects often equate to roughly 30% of the file size. 
### Rotation Fixer
When exporting from VC into Blender, an issue we often encounter is robot axises losing their rotation on some frames. Cleaning these kinds of issues by hand can be very time consuming, especially in long simulations, this tool aims to help reduce that time by automatically finding frames where the rotation differs and setting it to an absolute rotation.
### Material Replacer (In active development)
This tool comes with a selection of materials we use in our renders and works by replacing the materials of selected objects with more advanced materials of the selected type.

## Sejfo Render Presets
This a simple tool to set the render settings for the current scene to the default settings we use in our renders.
A lot of these settings are set for quick renders that still are nice to look at. In most cases we don't have a lot of time to set aside for rendering.