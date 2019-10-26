#!/usr/bin/env python
#
# Generate Mandelbrot image
#
# Nicolas Hennion (aka) Nicolargo
#

# Libs
######

import sys
import time
import Image
import colorsys

# Configuration
###############

# Image size (output)
nx = 640
ny = 480

# Image center and width (complex plan)
cx = -1.0
cy = 0.0
cw = 4.0
#~ cx = 0.443541797
#~ cy = 0.374095706
#~ cw = 0.016290788

# Max iteration number
nmax = 255

# Functions
###########

def mandelbrot(j):
    img = ymax-j*step
    sys.stdout.write ("\rLine: %d" % j + "/%d" % ny)
    sys.stdout.flush ()
    for i in xrange(nx):
        # Mandelbrot iteration
        c = complex(xreal[i], img)
        z = 0
        for n in xrange(nmax):
            if abs(z) > 2.0: 
                break 
            z = z * z + c
        # Save the pixel information
        image[i][j] = n

def theend():
    # End computing
    elapsed = time.time() - start
    sys.stdout.write("\rCompute time: %.2f second\n" % elapsed) 

    # Create the image file
    png = Image.new("RGB", (nx, ny))

    # Generate the image
    for j in xrange(ny):
        for i in xrange(nx):
            png.putpixel( (i,j), image[i][j])

    # Save the image
    png.save("mandelbrot.png", "PNG")

# Begin
#######

# Start computing
sys.stdout.write("Mandelbrot set\n") 

start = time.time()

# Optimisation
xmin = cx - cw / 2
ymax = cy + cw / 2 * ny / nx
step = cw / nx
xreal = [j * step + xmin for j in xrange(nx)]

# Image array
image = [[0 for j in xrange(ny)] for i in xrange(nx)]
for j in xrange(ny):
    mandelbrot(j)

# End computing
theend()
   
# End
#####
