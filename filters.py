import numpy as np
from numpy.fft import fft, ifft, fftshift, ifftshift


class Filters():

    def __init__(self, s, p):
        """Recebe a sequência de coordenadas e a porcentagem entre 0 a 100"""
        self._s = s
        self._p = p
        self._n = len(s)

    def _d(self):
        """Distância a partir da frequência central"""
        d = np.zeros(self._n)
        for i in range(self._n):
            d[i] = np.sqrt((i-self._n/2)**2)
        return d

    def _remove_high_freq(self):
        """Remove as altas frequências"""
        size = self._n * self._p / 100
        lpass = np.zeros(self._n)
        d = self._d()
        for i in range(self._n):
            lpass[i] = 1 if d[i] <= size/2 else 0
        zeros = self._n - np.count_nonzero(lpass)
        print('High frequencies removed: {}/{}'.format(zeros, self._n))
        f = fftshift(fft(self._s))
        return ifft(ifftshift(f * lpass))

    def _remove_low_freq(self):
        """Remove as baixas frequências"""
        size = self._n * (1 + self._p / 100)
        hpass = np.ones(self._n)
        d = self._d()
        for i in range(self._n):
            hpass[i] = 0 if d[i] < size/2 else 1
        zeros = self._n - np.count_nonzero(hpass)
        print('Low frequencies removed: {}/{}'.format(zeros, self._n))
        f = fftshift(fft(self._s))
        return ifft(ifftshift(f * hpass))

    def apply_filter(self):
        """Aplica o filtro na sequência de coordenadas"""
        if self._p > 0:
            return self._remove_high_freq()
        else:
            return self._remove_low_freq()
