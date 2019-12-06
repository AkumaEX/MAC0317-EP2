from edge_detector import EdgeDetector
from filters import Filters
import numpy as np


class FourierDescriptors():
    def __init__(self, img, i, p):
        self._img = img
        self._i = i
        self._p = p

    def get_results(self):
        """Retorna os resultados do contorno na forma de matriz"""
        ctr = EdgeDetector(self._img, self._i).get_edges()
        ctr_filtered = Filters(ctr, self._p).apply_filter()
        ctr_filtered = np.around(ctr_filtered, decimals=12)

        self._print_distance(ctr, ctr_filtered)
        return self._get_result(ctr), self._get_result(ctr_filtered)

    def _get_result(self, s):
        """Recebe uma sequência e devolve a sua representação em uma matriz"""
        h, w = self._img.shape
        s += (w*0.5 + h*0.5j)
        result = np.zeros((h, w), dtype=np.uint8)
        for x, y in zip(np.real(s), np.imag(s)):
            m, n = int(y), int(x)
            if 0 <= m and m < h and 0 <= n and n < w:
                result[m][n] = 255
        return result

    def _print_distance(self, a, b):
        """Imprime a distância Euclidiana dos contornos a partir do centro"""
        h, w = self._img.shape
        abs_a = abs(a - (w*0.5+h*0.5j))
        abs_b = abs(b - (w*0.5+h*0.5j))
        diff = abs(np.sum(abs_a) - np.sum(abs_b))
        print('Euclidean Distance: {}'.format(diff))
