import bpy
from bpy.types import Operator

class EZLOOP_OT_Flatten(Operator):
    bl_idname = "ezloop.flatten"
    bl_label = "Flatten"
    bl_description = "Apply LoopTools Flatten"

    def execute(self, context):
        bpy.ops.mesh.looptools_flatten()
        return {'FINISHED'}

class EZLOOP_OT_Relax(Operator):
    bl_idname = "ezloop.relax"
    bl_label = "Relax"
    bl_description = "Apply LoopTools Relax"

    def execute(self, context):
        bpy.ops.mesh.looptools_relax()
        return {'FINISHED'}

class EZLOOP_OT_Space(Operator):
    bl_idname = "ezloop.space"
    bl_label = "Space"
    bl_description = "Apply LoopTools Space"

    def execute(self, context):
        bpy.ops.mesh.looptools_space()
        return {'FINISHED'}

classes = (
    EZLOOP_OT_Flatten,
    EZLOOP_OT_Relax,
    EZLOOP_OT_Space,
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)