from stl import mesh
from vpython import *

def crear_desde_stl(malla):
    '''
    Esta funciontransforma una malla stl a un formato legible por vpython 7 para python 3.6, se requiere tener el
    paquete numpy-stl
    Entra el nombre de la variable qUe tiene el stl
    stl->list[triangules]
    se recomienda guardar el output en una variable para animarlo
    '''
    cdg = malla.get_mass_properties()[1]
    vector0 = malla.v0
    vector1 = malla.v1
    vector2 = malla.v2

    tris = []
    normales = malla.normals

    for n in range(len(vector1)):
        normalActual = vec(normales[n][0], normales[n][1], normales[n][2])
        a = vertex(pos=vec(vector0[n][0]-cdg[0], vector0[n][1]-cdg[1], vector0[n][2]-cdg[2]), color=color.red, normal=normalActual)
        b = vertex(pos=vec(vector1[n][0]-cdg[0], vector1[n][1]-cdg[1], vector1[n][2]-cdg[2]), color=color.red, normal=normalActual)
        c = vertex(pos=vec(vector2[n][0]-cdg[0], vector2[n][1]-cdg[1], vector2[n][2]-cdg[2]), color=color.red, normal=normalActual)
        tris.append(triangle(vs=[a, b, c]))

#hasta ahora grafica perfe el centro de masa en el 0,0,0
#idea, usar matriz de inercia para ver ejes .get_mas_pro...
malla=mesh.Mesh.from_file('xwing.stl')

xwing=crear_desde_stl(malla)
