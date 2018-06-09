from vpython import *

scene.title = "Faces example"
scene.width = 600
scene.height = 400

f = frame()
tri = faces(
    pos = [
        [0.,0.,0.], [1.,0.,0.], [0.,1.,0.],   # first tri - vertices
        [0.,0.,0.], [-1.,0.,0.], [0.,-1.,0.]  # second tri - vertices
    ],
    color = [
        [1.,0.,0.], [0.5,0.5,0.], [0.,1.,0.], # first tri - colors
        [0.,0.,1.], [0.,0.5,0.5], [0.,1.,0.]  # second tri - colors
    ],
    frame = f
)

tri.make_normals()
tri.make_twosided()

while True:
    rate(100)
    f.rotate(angle=0.01)