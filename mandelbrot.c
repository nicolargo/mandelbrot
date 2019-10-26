/*
  A program to generate an image of the Mandelbrot set.

  Usage: ./mandelbrot > output
         where "output" will be a binary image, 1 byte per pixel
         The program will print instructions on stderr as to how to
         process the output to produce a JPG file.

  Based on an original code written by Michael Ashley / UNSW / 23-Apr-2004

  Nicolargo (aka) Nicolas Hennion (irl) / 05-2013
*/

const double xCentre = -0.75;
const double yCentre = +0.0;
const int    nx      = 400;
const int    ny      = 400;

const double dxy     = 0.005;

#include <stdio.h>
#include <unistd.h>
#include <limits.h>
#include <complex.h>

int main() {

    double complex c, z;
    unsigned char n;
    int i, j;

    // The Mandelbrot calculation is to iterate the equation
    // z = z*z + c, where z and c are complex numbers, z is initially
    // zero, and c is the coordinate of the point being tested. If
    // the magnitude of z remains less than 2 for ever, then the point
    // c is in the Mandelbrot set. We write out the number of iterations
    // before the magnitude of z exceeds 2, or UCHAR_MAX, whichever is
    // smaller.

    for (j = 0; j < ny; j++) {
        for (i = 0; i < nx; i++) {
            c = xCentre + (i - nx/2)*dxy +  I * (yCentre + (j - ny/2)*dxy);
            z = 0.0;
            n = 0;
            while ((cabs(z) < 2.0) && (n != UCHAR_MAX)) {
                z = z*z + c;
                n++;
            }
            write(1, &n, sizeof(n)); // Write the result to stdout
        }
    }

    fprintf (stderr, "To process the image: convert -depth 8 -size %dx%d gray:output out.jpg\n",
         nx, ny);
    return 0;
}