import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import comb
from mpl_toolkits.mplot3d import Axes3D


def bernstein_curve(i, n, t):
    """
    Calculate the bernstein polynomial
    """
    return comb(n, i) * (t ** (n - i)) * ((1 - t) ** i)


def bezier_curve(points, part=100):
    """
    Calculate the bezier curve points
    """
    nPoints = len(points)

    xPoints = np.array([p[0] for p in points])
    yPoints = np.array([p[1] for p in points])
    zPoints = np.array([p[2] for p in points])

    t = np.linspace(0, 1, part)

    polynomial_array = np.array([bernstein_curve(i, nPoints - 1, t) for i in range(nPoints)])

    xvals = []
    yvals = []
    zvals = []

    for j in range(len(polynomial_array[0])):
        xvals.append(sum([polynomial_array[i][j]*xPoints[i] for i in range(nPoints)]))
        yvals.append(sum([polynomial_array[i][j]*yPoints[i] for i in range(nPoints)]))
        zvals.append(sum([polynomial_array[i][j]*zPoints[i] for i in range(nPoints)]))

    return (xvals, yvals, zvals)


#####################################################################

# Define the control points

points = [[0, 0, 0],
          [0, 1, 1],
          [1, 1, 2],
          [1, 0, 3],
          [0, 0, 4]]

xPoints = [p[0] for p in points]
yPoints = [p[1] for p in points]
zPoints = [p[2] for p in points]

# Obtain the curve points

xvals, yvals, zvals = bezier_curve(points, part=100)

# Plot results

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(xvals, yvals, zvals)
ax.plot(xPoints, yPoints, zPoints, "ro")
ax.plot(xPoints, yPoints, zPoints, "r")


plt.show()
