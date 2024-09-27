bl_info = {
    "name": "EZLoop",
    "author": "Snowyegret",
    "version": (1, 0, 0),
    "blender": (3, 6, 0),
    "location": "View3D > N-Panel > EZLoop",
    "description": "Quick access to LoopTools Flatten, Relax, and Space",
    "category": "Mesh",
}

import bpy
from . import ezloop_operation
from . import ezloop_panel

def register():
    ezloop_operation.register()
    ezloop_panel.register()

def unregister():
    ezloop_operation.unregister()
    ezloop_panel.unregister()

if __name__ == "__main__":
    register()