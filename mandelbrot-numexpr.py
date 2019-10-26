#!/usr/bin/env python
# Lib:

import numpy as np
import numexpr as ne
import pylab

def mandelbrot(h, w, maxit=100):
        '''Returns an image of the Mandelbrot fractal of size (h,w).
        '''
        y, x = np.ogrid[-2:2:h*1j, -3:1:w*1j]
        c = x+y*1j
        z = c
        divtime = maxit + np.zeros(z.shape, dtype=int)

        for i in xrange(maxit):
                # z = z**2 + c
                z = ne.evaluate('z**2 + c')
                # who is diverging
                diverge = z*np.conj(z) > 2**2
                # who is diverging now
                div_now = diverge & (divtime == maxit)
                # note when
                divtime[div_now] = i
                # avoid diverging too much
                z[diverge] = 2

        return divtime

pylab.imshow(mandelbrot(400, 400, 100))
# pylab.show()
