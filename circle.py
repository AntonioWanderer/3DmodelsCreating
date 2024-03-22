import numpy as np
from math import pi, cos, sin
from stl import mesh

meridians = 10
parallels = 10
dfi = 2 * pi / meridians
dth = pi / parallels

sphere = mesh.Mesh(np.zeros(meridians * parallels * 4, dtype=mesh.Mesh.dtype))
ind = 0
for th in range(parallels):
    for fi in range(meridians):
        ind +=1

        sphere.vectors[ind][0] = np.array([sin((fi) * dfi) * sin((th) * dth),
                                         cos((fi) * dfi) * sin((th) * dth),
                                         cos((th) * dth)])
        sphere.vectors[ind][1] = np.array([sin((fi + 1) * dfi) * sin((th) * dth),
                                         cos((fi + 1) * dfi) * sin((th) * dth),
                                         cos((th) * dth)])
        sphere.vectors[ind][2] = np.array([sin((fi) * dfi) * sin((th + 1) * dth),
                                         cos((fi) * dfi) * sin((th + 1) * dth),
                                         cos((th + 1) * dth)])

for th in range(parallels):
    for fi in range(meridians):
        ind +=1

        sphere.vectors[ind][0] = np.array([-sin((fi) * dfi) * sin((th) * dth),
                                         cos((fi) * dfi) * sin((th) * dth),
                                         -cos((th) * dth)])
        sphere.vectors[ind][1] = np.array([-sin((fi + 1) * dfi) * sin((th) * dth),
                                         cos((fi + 1) * dfi) * sin((th) * dth),
                                         -cos((th) * dth)])
        sphere.vectors[ind][2] = np.array([-sin((fi) * dfi) * sin((th + 1) * dth),
                                         cos((fi) * dfi) * sin((th + 1) * dth),
                                         -cos((th + 1) * dth)])
sphere.save('Final.stl')
