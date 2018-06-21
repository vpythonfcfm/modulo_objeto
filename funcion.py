from stl import mesh
from vpython import *
import numpy as np
#la idea es que 'malla' sea un archivo stl, eso se logra importando un archivo con mesh.Mesh.from_file('nombrearchivo')
#y asignandolo a una variable que luego sería la entrada de la función crear_desde_stl
xwing = mesh.Mesh.from_file('xwing.stl')

xwing=objeto(mesh.Mesh.from_file(''))

def multiplicar_matriz_vec(matriz, vecc):
        vecnp = np.array(vecc.x, vecc.y, vecc.z)
        out = matriz.dot(vecc)
        return vec(out[0], out[1], out[2])

def multiplicar_matriz_triangulo(matriz, triangulo):
    v0, v1, v2 = triangulo.v0.pos, triangulo.v1.pos, triangulo.v2.pos
    r0 = multiplicar_matriz_vec(matriz, v0)
    r1 = multiplicar_matriz_vec(matriz, v1)
    r2 = multiplicar_matriz_vec(matriz, v2)
    return (r0,r1,r2) 

class objeto():
    def __init__(self,malla):
        self.tris=[]
        cdg=malla.get_mass_properties()[1]
        self.I=malla.get_mass_properties()[2]
        self.v0=malla.v0
        self.v1=malla.v1
        self.v2=malla.v2
        self.normales=malla.normals



        for n in range(len(self.v1)):
            normalActual = vec(self.normales[n][0], self.normales[n][1], self.normales[n][2])
            a = vertex(pos=vec(self.v0[n][0] - cdg[0], self.v0[n][1] - cdg[1], self.v0[n][2] - cdg[2]),color=color.red, normal=normalActual)
            b = vertex(pos=vec(self.v1[n][0] - cdg[0], self.v1[n][1] - cdg[1], self.v1[n][2] - cdg[2]),color=color.red, normal=normalActual)
            c = vertex(pos=vec(self.v2[n][0] - cdg[0], self.v2[n][1] - cdg[1], self.v2[n][2] - cdg[2]),olor=color.red, normal=normalActual)
            self.tris.append(triangle(vs=[a,b,c]))  # esto toma los vertex para hacer un triangulo y los agrega a la lista que originalmente estaba vacía

    def rotar(self, matrizRot):
        for triangulo in self.tris:
            triangulo.v0.pos, triangulo.v1.pos, triangulo.v2.pos = multiplicar_matriz_triangulo(matrizRot, triangulo)
    

    def rotar_x(self, theta):
        matrizRot = np.array([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]])
        self.rotar(matrizRot)


    def rotar_y(self, theta):
        matrizRot = np.array([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]])
        self.rotar(matrizRot)


    def rotar_z(self, theta):
        matrizRot = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
        self.rotar(matrizRot)

    def desplazar(self, v):
        for triangulo in self.tris:
            triangulo.v0.pos += v
            triangulo.v1.pos += v
            triangulo.v2.pos += v


def crear_desde_stl(malla):
    '''
    Esta funciontransforma una malla stl a un formato legible por vpython 7 para python 3.6, se requiere tener el
    paquete numpy-stl
    Entra el nombre de la variable qUe tiene el stl
    stl->list[triangules]
    se recomienda guardar el output en una variable para animarlo
    '''

    cdg = malla.get_mass_properties()[1]#esta linea es el centro de gravedad yme parece que es un arreglo numpy, la idea es
    #tener este dato para poder usarlo al momento de centrar el objeto en vpython
    vector0 = malla.v0 #crea un vector con todos los primeros vectores de cada triangulo de la triangulacion
    vector1 = malla.v1 #lo mismo que arriba pero segundos vectores de c/triangulo
    vector2 = malla.v2 #lo musmo pero terceros

    tris = [] #lista vacía que se va a llenar con los triangulos que entiende vpython
    normales = malla.normals #vector con las normales de cada triangulo, las que sirven para orientar las caras de cada triangulo

    for n in range(len(vector1)):
        normalActual = vec(normales[n][0], normales[n][1], normales[n][2])#lee la normal correspondiente a la iteracion y la transforma en un vec que entienda vpython
        #lo que viene aca abajo es a partir de las listas de los vectors, se crean los vertex de vpython que sirven para hacer los triangles
        #de vpython ya que para hacer los triangulos es necesario que sean vertex y que cada uno especifique la normal
        a = vertex(pos=vec(vector0[n][0]-cdg[0], vector0[n][1]-cdg[1], vector0[n][2]-cdg[2]), color=color.red, normal=normalActual)
        b = vertex(pos=vec(vector1[n][0]-cdg[0], vector1[n][1]-cdg[1], vector1[n][2]-cdg[2]), color=color.red, normal=normalActual)
        c = vertex(pos=vec(vector2[n][0]-cdg[0], vector2[n][1]-cdg[1], vector2[n][2]-cdg[2]), color=color.red, normal=normalActual)
        tris.append(triangle(vs=[a, b, c]))#esto toma los vertex para hacer un triangulo y los agrega a la lista que originalmente estaba vacía



    '''epsilon=2*np.pi*0.001

    #prueba de rotacion que funciona!!!
    while True:
        rate(100)
        for triangulo in tris:
            triangulo.v1.pos = triangulo.v1.pos.rotate(angle=epsilon)
            triangulo.v2.pos = triangulo.v2.pos.rotate(angle=epsilon)
            triangulo.v0.pos = triangulo.v0.pos.rotate(angle=epsilon)
            '''






xwing=mesh.Mesh.from_file('libro.stl')
def importar_stl(nombreArchivo):
    assert type(nombreArchivo)==str
    return mesh.Mesh.from_file(nombreArchivo)

crear_desde_stl(xwing)







'''
todo lo que viene acá es lo que hace rotar un objeto en los distintos ejes del sist de referencia de vpython
por lo que va a haber que hacer un cambio de base que estoy pensando para poder usarlo de una manera más 
limpia, probablemente sea con el producto punto o cruz entre los dos ultimos vectores posicion y así sacar cuanto tiene 
que rotar


noue el eje z es perpendicular a la pantalla en vpython, el x horizontal e y es vertical
todo lo que está adentro
'''



def multiplicar_matriz_vec(matriz,vecc):
    vecnp=np.array(vecc.x,vecc.y,vecc.z)
    out=matriz.dot(vecc)
    return vec(out[0],out[1],out[2])







def multiplicar_vertex_matriz(vertexDeVpython,Matriz):
    a=np.array([vertexDeVpython.pos.x,vertexDeVpython.pos.y,vertexDeVpython.pos.z])
    out=Matriz.dot(a)
    return vec(out[0],out[1],out[2])



def rotar_x(vertexDeVpython,theta):
    matrizRot=np.array([[1,0,0],[0,np.cos(theta),-np.sin(theta)],[0,np.sin(theta),np.cos(theta)]])
    multiplicar_vertex_matriz(vertexDeVpython,matrizRot)


def rotar_y(vertexDeVpython,theta):
    matrizRot=np.array([[1,0,0],[0,np.cos(theta),-np.sin(theta)],[0,np.sin(theta),np.cos(theta)]])
    multiplicar_vertex_matriz(vertexDeVpython,matrizRot)

def rotar_z(vertexDeVpython,theta):
    matrizRot=np.array([[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0],[0,0,1]])
    multiplicar_vertex_matriz(vertexDeVpython,matrizRot)



#lo que viene ahora es para poder alinear los ejes del objeto con los de la
#escena, la idea es que esto tb esté en el __init__ de la clase

def cuantoRotarCadaEje(variable_stl):
    '''
    esta función se encarga de alinear los ejes del modelo importado con los ejes de la escena de vpython
    la idea es que al momento de generar los vertex se les haga este arreglo para alinearlos y trabajar en
    un mismo sist de ref.

    :param variable_stl: entra un archivo stl guardado en una variable
    :return: devuelve un vector con el angulo que hay que girar en cada eje de la figura para alinearla con la escena
    '''
    I=variable_stl.get_mass_properties()[2]

    rotacion = np.linalg.eig(I)

    X=np.array([1,0,0])
    Y=np.array([0,1,0])
    Z=np.array([0,0,1])

    Alpha=np.arccos((X.dot(eig0))/np.linalg.norm(eig0))
    Beta=np.arccos((Y.dot(eig1))/np.linalg.norm(eig1))
    Gamma=np.arccos((Z.dot(eig2))/np.linalg.norm(eig2))

    return np.array([-Alpha,-Beta,-Gamma])



