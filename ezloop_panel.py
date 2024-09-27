import bpy
from bpy.types import Panel

class EZLOOP_PT_Panel(Panel):
    bl_label = "EZLoop"
    bl_idname = "EZLOOP_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "EZLoop"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("ezloop.flatten", text="Flatten")

        row = layout.row()
        row.operator("ezloop.relax", text="Relax")

        row = layout.row()
        row.operator("ezloop.space", text="Space")

def register():
    bpy.utils.register_class(EZLOOP_PT_Panel)

def unregister():
    bpy.utils.unregister_class(EZLOOP_PT_Panel)