---
title: Pyscript - Demo 2
header-includes: |
    <style>
       body { min-width: 90% !important; }
    </style>
include-after: |
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <!-- python -m http.server, URL: http://0.0.0.0:8000/demo/demo02.html -->
    <!-- file:///Users/josephchan/jc/www/python/pyscript/demo/demo02.html -->
---

# Pyscript - Math Plots

<!-- output target -->
<div id="mplot"></div>
<div id="figure"></div>


Type your Python code (hover mouse/pointer to bottom right-end for Green arrow to run code):
<py-repl></py-repl>

<!--
in REPL:
div = Element('mplot')
div.element.innerHTML

<div><img src="data:image/png;charset=utf-8;base64,iVBORw0KGgoAAAANSUhEUg ... 4AAAAASUVORK5CYII="></div>

A static image, no canvas.
-->

<!-- pyscript -->
```{=html}
<py-config>
    packages = ["matplotlib", "numpy"]
</py-config>
<py-script>
import matplotlib.pyplot as plt
import numpy as np

# First plot
plt.clf()  # clear, not really need for first

# specify the x coordinates
angle = np.linspace(0, 2 * np.pi, 100)

# make some plots
plt.plot(angle, np.sin(angle), color='green')
plt.plot(angle, np.cos(angle), color='blue')
plt.xlabel('angle')
plt.ylabel('value')
plt.title('Sine (green) and Cosine (blue) waves, from 0 to 2π:')

# display the plots
display(plt, target="mplot")


# Second plot
import matplotlib.tri as tri
plt.clf()  # clear the plot

# First create the x and y coordinates of the points.
n_angles = 36
n_radii = 8
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
angles[:, 1::2] += np.pi / n_angles

x = (radii * np.cos(angles)).flatten()
y = (radii * np.sin(angles)).flatten()
z = (np.cos(radii) * np.cos(3 * angles)).flatten()

# Create the Triangulation; no triangles so Delaunay triangulation created.
triang = tri.Triangulation(x, y)

# Mask off unwanted triangles.
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)

fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tpc = ax1.tripcolor(triang, z, shading='flat')
fig1.colorbar(tpc)
ax1.set_title('tripcolor of Delaunay triangulation, flat shading')

display(fig1, target="figure")

</py-script>
```

---

<!-- pandoc -s demo02.md -o demo02.html -->