from scipy.signal.windows import blackmanharris
from scipy import fft
from numpy.fft import rfft
from numpy import argmax, mean, diff, nonzero
from pylab import log
import pylab
import numpy as np
import matplotlib.pyplot as plt


def get_freq_from_HPS(sig, fs):
    windowed = sig * blackmanharris(len(sig))

    # harmonic product spectrum:
    ft = abs(rfft(windowed))
    maxharms = 8
    freq = []
    for x in range(2, maxharms):
        a = pylab.copy(ft[::x])
        ft = ft[:len(a)]
        i = argmax(abs(ft))
        if i == len(abs(ft))-1:
          break;
        true_i = parabolic(log(abs(ft)), i)[0]
        freq.append(fs * true_i / len(windowed))
        ft *= a
    return freq[0]

def parabolic(f, x):
    xv = 1/2. * (f[x-1] - f[x+1]) / (f[x-1] - 2 * f[x] + f[x+1]) + x
    yv = f[x] - 1/4. * (f[x-1] - f[x+1]) * (xv - x)
    return (xv, yv)