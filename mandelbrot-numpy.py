#!/usr/bin/env python
# Lib:

import numpy as np
import pylab

def mandelbrot(h, w, maxit=100):
        '''Returns an image of the Mandelbrot fractal of size (h,w).
        '''
        y, x = np.ogrid[-2:2:h*1j, -3:1:w*1j]
        c = x+y*1j
        z = c
        divtime = maxit + np.zeros(z.shape, dtype=int)

        for i in xrange(maxit):
                z  = z**2 + c
                diverge = z*np.conj(z) > 2**2              # who is diverging
                div_now = diverge & (divtime == maxit)  # who is diverging now
                divtime[div_now] = i                    # note when
                z[diverge] = 2                          # avoid diverging too much

        return divtime

pylab.imshow(mandelbrot(400, 400, 100))
# pylab.show()
