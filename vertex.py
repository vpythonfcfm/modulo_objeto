import stl as mesh
import numpy as np

A=mesh.Mesh.from_file('super.stl')
B=mesh.Mesh.from_file('xwing.stl')

I=A.get_mass_properties()[2]
print(I)


eig0=np.linalg.eig(I)[1][:,0]
eig1=np.linalg.eig(I)[1][:,1]
eig2=np.linalg.eig(I)[1][:,2]
X=np.array([1,0,0])
angulo_a_rotar=np.arccos((X.dot(eig0)/np.linalg.norm(eig0)))

