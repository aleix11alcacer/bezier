import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import comb
from mpl_toolkits.mplot3d import Axes3D


def bernstein_surface(i, j, nU, nV, u, v):
    """
    Calculate the bernstein polynomial
    """
    return np.outer(comb(nU, i) * (u ** (nU - i)) * ((1 - u) ** i),
                    comb(nV, j) * (v ** (nV - j)) * ((1 - v) ** j))


def bezier_surface(points, part=10):
    """
    Calculate the bezier surface points
    """
    nU = points.shape[0]
    nV = points.shape[1]
    nPoints = nU*nV

    xPoints = np.array([p[0] for p in points.reshape(nPoints, 3)])
    yPoints = np.array([p[1] for p in points.reshape(nPoints, 3)])
    zPoints = np.array([p[2] for p in points.reshape(nPoints, 3)])

    u = np.linspace(0, 1, part)
    v = np.linspace(0, 1, part)

    polynomial_array = np.array([[bernstein_surface(i, j, nU - 1, nV - 1, u, v) for j in
                                range(nV)] for i in range(nU)]).reshape(nPoints, part ** 2)

    xvals = []
    yvals = []
    zvals = []

    for j in range(len(polynomial_array[0])):
        xvals.append(sum([polynomial_array[i][j] * xPoints[i] for i in range(nPoints)]))
        yvals.append(sum([polynomial_array[i][j] * yPoints[i] for i in range(nPoints)]))
        zvals.append(sum([polynomial_array[i][j] * zPoints[i] for i in range(nPoints)]))

    return (xvals, yvals, zvals)


#####################################################################

# Define the control points

points = np.array([[(0, 0, 0), (1, 0, 1), (2, 0, 1), (3, 0, 0)],
                  [(0, 1, 1), (1, 1, 4), (2, 1, 4), (3, 1, 1)],
                  [(0, 2, 1), (1, 2, 4), (2, 2, 4), (3, 2, 1)],
                  [(0, 3, 0), (1, 3, 1), (2, 3, 1), (3, 3, 0)]])

nU = points.shape[0]
nV = points.shape[1]
nPoints = nU * nV

# Obtain the surface points

xvals, yvals, zvals = bezier_surface(points, part=10)

# Plot results

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_trisurf(xvals, yvals, zvals)

xPoints = np.array([[points[i][j][0] for j in range(nV)] for i in range(nU)])
yPoints = np.array([[points[i][j][1] for j in range(nV)] for i in range(nU)])
zPoints = np.array([[points[i][j][2] for j in range(nV)] for i in range(nU)])

ax.plot(xPoints.flatten(), yPoints.flatten(), zPoints.flatten(), "ro")
ax.plot_wireframe(xPoints, yPoints, zPoints, color="r")

plt.show()
