import numpy as np
from stl import mesh
from convert_stl import *


class Objeto():
    def __init__(self,nombreArchivo):
        self.pos=nombreArchivo.get_mass_properties()[1]
        self.objeto=crear_desde_stl(nombreArchivo)







#dejo como ejemplo acá lo que vpython tiene para el caso de la esfera, hay que intentar hacer algo parecido
"""class sphere(standardAttributes):
    def __init__(self, **args):
        args['_default_size'] = vector(2,2,2)
        args['_objName'] = "sphere"
        super(sphere, self).setup(args)
        
    @property
    def radius(self):
        return self._size.y/2
    @radius.setter
    def radius(self,value):
        d = 2*value
        self.size = vector(d,d,d) # size will call addattr
        
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,value):
        if not isinstance(value, vector): raise TypeError('size must be a vector')
        self._size = value
        if not self._constructing:
            self.addattr('size') # changing a sphere size should not affect axis

    @property
    def axis(self):
        return self._axis
    @axis.setter
    def axis(self,value): # changing a sphere axis should not affect size
        self._save_oldaxis = adjust_up(self._axis, value, self._up, self._save_oldaxis) # this sets self._axis and self._up
        self._axis.value = value
        if not self._constructing:
            # must update both axis and up when either is changed
            self.addattr('axis')
            self.addattr('up')"""