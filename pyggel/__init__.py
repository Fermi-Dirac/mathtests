"""
pyggle.__init__
This library (PYGGEL) is licensed under the LGPL by Matthew Roe and PYGGEL contributors.
"""

PYGGEL_VERSION = "0.075-alpha3b"
from .include import *

from . import mesh, view, image, camera, math3d, light
from . import scene, font, geometry, misc, data
from . import particle, event, gui

def quit():
    """Deinitialize PYGGEL..."""
    view.clear_screen()
    glFlush()
    pygame.quit()

init = view.init

def get_events():
    """Return (for now) generated pygame events..."""
    return pygame.event.get()

def get_version():
    """Return the version string for PYGGEL."""
    return PYGGEL_VERSION
