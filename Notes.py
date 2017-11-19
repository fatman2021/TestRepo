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
