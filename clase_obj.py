from stl import mesh
from vpython import *

class objeto(nombreArchivo):
    from funcion import *
    crear_desde_stl(nombreArchivo)
    def __init__(self):

        '''
            Esta funcióntransforma unarchivo stl a un formato legible por vpython 7 para python 3.6, se requiere tener el
            paquete numpy-stl
            Entra el nombre del archivo (string) tiene que tener la extension y sale un archivo legible para vpython
            str->list[triangules]
            se recomienda guardar el output en una variable para animarlo
        '''

        vector0 = malla.v0
        vector1 = malla.v1
        vector2 = malla.v2

        tris = []
        normales = malla.normals

        for n in range(len(vector1)):
            normalActual = vec(normales[n][0], normales[n][1], normales[n][2])
            a = vertex(pos=vec(vector0[n][0], vector0[n][1], vector0[n][2]), color=color.red, normal=normalActual)
            b = vertex(pos=vec(vector1[n][0], vector1[n][1], vector1[n][2]), color=color.red, normal=normalActual)
            c = vertex(pos=vec(vector2[n][0], vector2[n][1], vector2[n][2]), color=color.red, normal=normalActual)
            tris.append(triangle(vs=[a, b, c]))



        self.pos=n





xwing=crear_desde_stl('xwing.stl')
