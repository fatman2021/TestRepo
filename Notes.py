# Fluid simulation

import bpy

# Domain
bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.resize(value=(4.72379, 4.72379, 4.72379))
bpy.ops.object.modifier_add(type='FLUID_SIMULATION')
bpy.context.object.modifiers["Fluidsim"].settings.type = 'DOMAIN'

active_object = bpy.data.objects["Cube"]
active_object.data.materials.clear()

material = bpy.data.materials.new(name="Water")
material.use_nodes = True

material_output = material.node_tree.nodes.get('Material Output')
shader = material.node_tree.nodes.new('ShaderNodeBsdfGlass')

material.node_tree.links.new(material_output.inputs[0], shader.outputs[0])

active_object.active_material = material

# Inflow
bpy.ops.mesh.primitive_uv_sphere_add()
bpy.ops.transform.translate(value=(0, 0, 2.79482))
bpy.ops.object.modifier_add(type='FLUID_SIMULATION')
bpy.context.object.modifiers["Fluidsim"].settings.type = 'INFLOW'
bpy.context.object.modifiers["Fluidsim"].settings.inflow_velocity[1] = -1
bpy.context.object.modifiers["Fluidsim"].settings.inflow_velocity[2] = 1

active_object = bpy.data.objects["Sphere"]
active_object.active_material

# End of fluid simulation

# Rigid Body Simulation

import bpy



bpy.ops.mesh.primitive_cube_add()
active_object = bpy.data.objects["Cube"]
active_object.data.materials.clear()
material = bpy.data.materials.new(name="Cube_Blue")
material.use_nodes = True
material_output = material.node_tree.nodes.get('Material Output')
shader = material.node_tree.nodes.new('ShaderNodeBsdfDiffuse')
shader.inputs[0].default_value=(0.0153586, 0.160053, 0.8, 1)
material.node_tree.links.new(material_output.inputs[0], shader.outputs[0])
active_object.active_material = material
bpy.ops.transform.resize(value=(0.2791035, 0.2791035, 0.2791035))
bpy.ops.object.modifier_add(type='ARRAY')
bpy.context.object.modifiers["Array"].count = 10
bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 1.1
bpy.ops.transform.translate(value=(-8.24526, -3.04335, 0))
bpy.ops.object.modifier_add(type='ARRAY')
bpy.context.object.modifiers["Array.001"].count = 10
bpy.context.object.modifiers["Array.001"].relative_offset_displace[0] = 0
bpy.context.object.modifiers["Array.001"].relative_offset_displace[1] = 1.1
bpy.ops.object.modifier_add(type='ARRAY')
bpy.context.object.modifiers["Array.002"].count = 10
bpy.context.object.modifiers["Array.002"].relative_offset_displace[0] = 0
bpy.context.object.modifiers["Array.002"].relative_offset_displace[2] = 1.1
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array")
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array.001")
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Array.002")
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.separate(type='LOOSE')
bpy.ops.object.editmode_toggle()
bpy.ops.rigidbody.object_add()
bpy.context.object.rigid_body.mass = 100
bpy.context.object.rigid_body.collision_shape = 'MESH'
bpy.ops.rigidbody.object_settings_copy()
bpy.ops.transform.rotate(value=-1.17998, axis=(0.227181, -0.788104, -0.572085))
bpy.ops.transform.translate(value=(8.24526, 0, 7.93236))
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
bpy.ops.mesh.primitive_plane_add()
bpy.ops.transform.resize(value=(8, 8, 8))
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0.60964, 0.664721, 3.22626)})
bpy.ops.mesh.delete(type='FACE')
bpy.ops.object.editmode_toggle()
bpy.ops.rigidbody.object_add()
bpy.context.object.rigid_body.type = 'PASSIVE'
bpy.context.object.rigid_body.collision_shape = 'MESH'
bpy.ops.mesh.primitive_plane_add()
bpy.ops.transform.translate(value=(11.7198, 0, 7.82638))
bpy.ops.transform.rotate(value=0.785398, axis=(1.23656,   0.795478, -0.605983))
bpy.ops.transform.resize(value=(4, 4, 4))
active_object = bpy.data.objects["Plane.001"]
active_object.data.materials.clear()
material = bpy.data.materials.new(name="Emission")
material.use_nodes = True
material_output = material.node_tree.nodes.get('Material Output')
shader = material.node_tree.nodes.new('ShaderNodeEmission')
shader.inputs[0].default_value=(0.0153586, 0.160053, 0.8, 1)
shader.inputs[1].default_value=6
material.node_tree.links.new(material_output.inputs[0], shader.outputs[0])
active_object.active_material = material
bpy.context.object.cycles_visibility.camera = False
bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":(-10.6639, -6.20935, -0)})
bpy.context.object.cycles_visibility.camera = False
bpy.ops.object.duplicate_move(TRANSFORM_OT_translate={"value":(-9.49401, 17.6382, 0)})
bpy.ops.transform.rotate(value=3.141590, axis=(-0, -0, -1))
bpy.context.object.cycles_visibility.camera = False
bpy.ops.object.camera_add()
bpy.ops.transform.translate(value=(0, -14, 14))
bpy.ops.transform.rotate(value=0.785398, axis=(1, 0, 0))

# End of Rigid Body Simulation

# Game 1
import bpy

bpy.ops.mesh.primitive_plane_add()
bpy.ops.transform.resize(value=(30, 30, 30))
bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(0, 0, 1.0678884))
bpy.context.object.game.physics_type = 'DYNAMIC'
bpy.context.object.game.use_collision_bounds = True
for i in range(3):
    bpy.ops.logic.sensor_add(type='KEYBOARD')
    bpy.ops.logic.actuator_add(type='MOTION')
    bpy.ops.logic.controller_add(object="Cube")
bpy.context.scene.objects.active = None
bpy.data.objects['Camera'].select = True
bpy.context.scene.objects.active = bpy.data.objects['Camera']
bpy.ops.logic.sensor_add(type='MOUSE')
bpy.ops.logic.actuator_add(type='MOUSE')
bpy.ops.logic.controller_add(object="Camera")
bpy.context.object.game.physics_type = 'DYNAMIC'
for i in range( 3 ):
    bpy.ops.logic.sensor_add(type='KEYBOARD')
    bpy.ops.logic.actuator_add(type='MOTION')
    bpy.ops.logic.controller_add(object='Camera')
    
# End Game 1

# Game 2

import bpy

bpy.ops.object.camera_add()
bpy.ops.transform.translate(value=(0, 0, 6.2321))
bpy.ops.transform.rotate(value=1.5708, axis=(1, 0, 0))
bpy.ops.logic.sensor_add(type='MOUSE')
bpy.ops.logic.actuator_add(type='MOUSE')
bpy.ops.logic.controller_add(object='Camera')

bpy.ops.mesh.primitive_cube_add()
bpy.context.object.game.physics_type = 'CHARACTER'
bpy.ops.transform.translate(value=(0, 0, 3.78662))
bpy.ops.logic.sensor_add(type='MOUSE')
bpy.ops.logic.actuator_add(type='MOUSE')
bpy.ops.logic.controller_add(object='Cube')

for i in range(5):
    bpy.ops.logic.sensor_add(type='KEYBOARD')
    bpy.ops.logic.actuator_add(type='MOTION')
    bpy.ops.logic.controller_add(object='Cube')

bpy.data.objects['Camera'].select = True
bpy.ops.object.parent_set(type='OBJECT', keep_transform=False)

bpy.ops.mesh.primitive_plane_add()
bpy.ops.transform.resize(value=(60, 60, 60))
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

bpy.ops.object.editmode_toggle()
bpy.ops.uv.unwrap(method='ANGLE_BASED', margin=0.001)
bpy.ops.object.editmode_toggle()
bpy.ops.material.new()
bpy.ops.texture.new()

bpy.ops.mesh.primitive_monkey_add()
bpy.ops.transform.translate(value=(0, 15.19031, 2.25481))
bpy.ops.transform.resize(value=(3.6531, 3.6531, 3.6531))
bpy.ops.transform.rotate(value=0.586864, axis=(-1, -2.22045e-16, 0))

active_object = bpy.context.active_object
material = bpy.data.materials.new("Suzanne_Mat")
active_object.data.materials.append(material)
bpy.context.object.active_material.diffuse_color = (0.8, 0.137856, 0.0496239)

bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subsurf"].levels = 2

bpy.ops.object.shade_smooth()
bpy.context.object.game.use_collision_bounds = True

bpy.context.object.game.collision_bounds_type = 'SPHERE'
bpy.context.object.game.physics_type = 'RIGID_BODY'

bpy.ops.object.lamp_add()
bpy.context.object.data.type = 'SUN'
bpy.ops.transform.translate(value=(0, 15.19031, 31.5536))
bpy.context.object.data.use_shadow = True
bpy.context.object.data.ge_shadow_buffer_type = 'VARIANCE'
bpy.context.scene.game_settings.material_mode = 'GLSL'

# End Game 2

# Game 3

import bpy

bpy.context.scene.name = "SceneGame"
bpy.context.scene.render.resolution_x = 640
bpy.context.scene.render.resolution_y = 480
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.render.engine = 'BLENDER_GAME'
bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(-0, -5.188273, 2))
bpy.context.object.game.physics_type = 'CHARACTER'
bpy.ops.logic.sensor_add(type='KEYBOARD')
bpy.ops.logic.actuator_add(type='MOTION')
bpy.ops.logic.controller_add(object="Cube")

bpy.ops.logic.sensor_add(type='COLLISION')
bpy.ops.logic.actuator_add(type='SCENE')
bpy.ops.logic.actuator_add(type='MOUSE')
bpy.ops.logic.controller_add(object="Cube")



bpy.ops.mesh.primitive_monkey_add()
bpy.ops.transform.translate(value=(-0.109028, 1.59881, 0.827893))
bpy.ops.transform.resize(value=(2.24086, 2.24086, 2.24086))
bpy.ops.transform.rotate(value=0.65906, axis=(-1, -0, -0))
active_object = bpy.context.active_object
material = bpy.data.materials.new("Suzanne_Mat")
active_object.data.materials.append(material)
bpy.context.object.active_material.diffuse_color = (1, 0, 0)

bpy.ops.mesh.primitive_plane_add()
bpy.ops.transform.resize(value=(12, 12, 12))

bpy.ops.scene.new(type='NEW')
bpy.context.scene.name = "SceneLose"
bpy.context.scene.render.resolution_x = 640
bpy.context.scene.render.resolution_y = 640
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.render.engine = 'BLENDER_GAME'
bpy.ops.object.camera_add()
bpy.ops.object.rotation_clear(clear_delta=False)
bpy.ops.transform.translate(value=(0, 0, 6.23475))
bpy.context.object.data.type = 'ORTHO'
bpy.ops.object.text_add()
bpy.ops.object.editmode_toggle()
bpy.ops.font.delete(type='ALL')
bpy.ops.font.text_insert(text="YOU LOSE")
bpy.ops.object.editmode_toggle()
bpy.ops.transform.translate(value=(-2.28259, 0, 0))
bpy.ops.object.convert(target='MESH')
active_object = bpy.context.active_object
material = bpy.data.materials.new("Lose_Mat")
active_object.data.materials.append(material)
bpy.context.object.active_material.diffuse_color = (1, 0, 0)
bpy.context.object.active_material.diffuse_intensity = 1
bpy.context.object.active_material.specular_intensity = 0
bpy.context.object.active_material.use_shadeless = True
bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(-.04291, -1.145425, -0))
bpy.ops.transform.resize(value=(2.5,  0.49923,  0.49923))
active_object = bpy.context.active_object
material = bpy.data.materials.new("Block_Mat")
active_object.data.materials.append(material)
bpy.context.object.active_material.diffuse_color = (0, 1, 0)
bpy.context.object.active_material.diffuse_intensity = 1
bpy.context.object.active_material.specular_intensity = 0
bpy.context.object.active_material.use_shadeless = True
bpy.ops.object.text_add()
bpy.ops.transform.translate(value =(-1.10,-1.44699, 1.15))
bpy.ops.object.editmode_toggle()
bpy.ops.font.delete(type='ALL')
bpy.ops.font.text_insert(text="RETRY")
bpy.ops.object.editmode_toggle()
bpy.ops.object.convert(target='MESH')
active_object = bpy.context.active_object
material = bpy.data.materials.new("Retry_Mat")
active_object.data.materials.append(material)
bpy.context.object.active_material.diffuse_color = (0, 0, 1)
bpy.context.object.active_material.diffuse_intensity = 1
bpy.context.object.active_material.specular_intensity = 0
bpy.context.object.active_material.use_shadeless = True
bpy.data.objects['Cube.001'].select = True
bpy.ops.object.join()
bpy.ops.logic.sensor_add(type='MOUSE')
bpy.ops.logic.sensor_add(type='MOUSE')
bpy.ops.logic.controller_add(type='LOGIC_AND')
bpy.ops.logic.actuator_add(type='SCENE')
bpy.ops.logic.actuator_add(type='MOUSE')

# End of Game 3
