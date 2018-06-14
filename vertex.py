from vpython import *
import stl as mesh
import numpy as np

A=mesh.Mesh.from_file('super.stl')
B=mesh.Mesh.from_file('xwing.stl')


I=A.get_mass_properties()[2]
DI=np.linalg.eig(I)[1]
print(DI)

