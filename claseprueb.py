import numpy as np
from stl import mesh
from convert_stl import *


class Objeto():
    def __init__(self,nombreArchivo):
        self.objeto=crear_desde_stl(nombreArchivo)
        self.pos=nombreArchivo.get_mass_properties()[2]
