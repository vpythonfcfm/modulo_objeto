import numpy as np
from stl import mesh
from test_convert_stl import *


class Objeto(nombreArchivo):
    def __init__(self):
        malla=mesh.Mesh.from_file(nombreArchivo)
        cog=malla.get_mass_properties()[1]
        self.pos=
