import numpy as np


class EdgeDetector():

    def __init__(self, img, i):
        """Recebe uma matriz Numpy e a intensidade entre 0 e 255"""
        self._img = img
        self._img_h, self._img_w = img.shape
        self._i = i
        self._s = None

    def _is_top_left(self, y, x):
        return y > 0 and x > 0 and self._img[y-1][x-1] == self._i

    def _is_top(self, y, x):
        return y > 0 and self._img[y-1][x] == self._i

    def _is_top_right(self, y, x):
        return y > 0 and x+1 < self._img_w and self._img[y-1][x+1] == self._i

    def _is_right(self, y, x):
        return x+1 < self._img_w and self._img[y][x+1] == self._i

    def _is_bottom_right(self, y, x):
        return y+1 < self._img_h and x+1 < self._img_w and self._img[y+1][x+1] == self._i

    def _is_bottom(self, y, x):
        return y+1 < self._img_h and self._img[y+1][x] == self._i

    def _is_bottom_left(self, y, x):
        return y+1 < self._img_h and x > 0 and self._img[y+1][x-1] == self._i

    def _is_left(self, y, x):
        return x > 0 and self._img[y][x-1] == self._i

    def _next_from_top_left(self, y, x):
        if self._is_top(y, x):
            return y-1, x
        elif self._is_top_right(y, x):
            return y-1, x+1
        elif self._is_right(y, x):
            return y, x+1
        elif self._is_bottom_right(y, x):
            return y+1, x+1
        elif self._is_bottom(y, x):
            return y+1, x
        elif self._is_bottom_left(y, x):
            return y+1, x-1
        elif self._is_left(y, x):
            return y, x-1
        elif self._is_top_left(y, x):
            return y-1, x-1
        else:
            return y, x

    def _next_from_top(self, y, x):
        if self._is_top_right(y, x):
            return y-1, x+1
        elif self._is_right(y, x):
            return y, x+1
        elif self._is_bottom_right(y, x):
            return y+1, x+1
        elif self._is_bottom(y, x):
            return y+1, x
        elif self._is_bottom_left(y, x):
            return y+1, x-1
        elif self._is_left(y, x):
            return y, x-1
        elif self._is_top_left(y, x):
            return y-1, x-1
        elif self._is_top(y, x):
            return y-1, x
        else:
            return y, x

    def _next_from_top_right(self, y, x):
        if self._is_right(y, x):
            return y, x+1
        elif self._is_bottom_right(y, x):
            return y+1, x+1
        elif self._is_bottom(y, x):
            return y+1, x
        elif self._is_bottom_left(y, x):
            return y+1, x-1
        elif self._is_left(y, x):
            return y, x-1
        elif self._is_top_left(y, x):
            return y-1, x-1
        elif self._is_top(y, x):
            return y-1, x
        elif self._is_top_right(y, x):
            return y-1, x+1
        else:
            return y, x

    def _next_from_left(self, y, x):
        if self._is_top_left(y, x):
            return y-1, x-1
        elif self._is_top(y, x):
            return y-1, x
        elif self._is_top_right(y, x):
            return y-1, x+1
        elif self._is_right(y, x):
            return y, x+1
        elif self._is_bottom_right(y, x):
            return y+1, x+1
        elif self._is_bottom(y, x):
            return y+1, x
        elif self._is_bottom_left(y, x):
            return y+1, x-1
        elif self._is_left(y, x):
            return y, x-1
        else:
            return y, x

    def _next_from_right(self, y, x):
        if self._is_bottom_right(y, x):
            return y+1, x+1
        elif self._is_bottom(y, x):
            return y+1, x
        elif self._is_bottom_left(y, x):
            return y+1, x-1
        elif self._is_left(y, x):
            return y, x-1
        elif self._is_top_left(y, x):
            return y-1, x-1
        elif self._is_top(y, x):
            return y-1, x
        elif self._is_top_right(y, x):
            return y-1, x+1
        elif self._is_right(y, x):
            return y, x+1
        else:
            return y, x

    def _next_from_bottom_left(self, y, x):
        if self._is_left(y, x):
            return y, x-1
        elif self._is_top_left(y, x):
            return y-1, x-1
        elif self._is_top(y, x):
            return y-1, x
        elif self._is_top_right(y, x):
            return y-1, x+1
        elif self._is_right(y, x):
            return y, x+1
        elif self._is_bottom_right(y, x):
            return y+1, x+1
        elif self._is_bottom(y, x):
            return y+1, x
        elif self._is_bottom_left(y, x):
            return y+1, x-1
        else:
            return y, x

    def _next_from_bottom(self, y, x):
        if self._is_bottom_left(y, x):
            return y+1, x-1
        elif self._is_left(y, x):
            return y, x-1
        elif self._is_top_left(y, x):
            return y-1, x-1
        elif self._is_top(y, x):
            return y-1, x
        elif self._is_top_right(y, x):
            return y-1, x+1
        elif self._is_right(y, x):
            return y, x+1
        elif self._is_bottom_right(y, x):
            return y+1, x+1
        elif self._is_bottom(y, x):
            return y+1, x
        else:
            return y, x

    def _next_from_bottom_right(self, y, x):
        if self._is_bottom(y, x):
            return y+1, x
        elif self._is_bottom_left(y, x):
            return y+1, x-1
        elif self._is_left(y, x):
            return y, x-1
        elif self._is_top_left(y, x):
            return y-1, x-1
        elif self._is_top(y, x):
            return y-1, x
        elif self._is_top_right(y, x):
            return y-1, x+1
        elif self._is_right(y, x):
            return y, x+1
        elif self._is_bottom_right(y, x):
            return y+1, x+1
        else:
            return y, x

    def _find_start_point(self):
        """Encontra a posição inicial"""
        for x in range(self._img_w):
            for y in range(self._img_h):
                if self._img[y][x] == self._i:
                    return y, x
        raise

    def get_edges(self):
        """Encontra a borda da imagem e retorna a sequência de coordenadas"""
        self._s = np.array([], dtype=np.complex64)

        start_y, start_x = self._find_start_point()
        y, x = start_y, start_x

        self._s = np.append(self._s, x + y*1j)

        new_y, new_x = self._next_from_top(y, x)

        while new_y != start_y or new_x != start_x:
            dir_y, dir_x = new_y - y, new_x - x
            y, x = new_y, new_x
            self._s = np.append(self._s, x + y*1j)

            if dir_y > 0:
                if dir_x > 0:
                    new_y, new_x = self._next_from_top_left(y, x)
                elif dir_x == 0:
                    new_y, new_x = self._next_from_top(y, x)
                else:
                    new_y, new_x = self._next_from_top_right(y, x)
            elif dir_y == 0:
                if dir_x > 0:
                    new_y, new_x = self._next_from_left(y, x)
                elif dir_x == 0:
                    break
                else:
                    new_y, new_x = self._next_from_right(y, x)
            else:
                if dir_x > 0:
                    new_y, new_x = self._next_from_bottom_left(y, x)
                elif dir_x == 0:
                    new_y, new_x = self._next_from_bottom(y, x)
                else:
                    new_y, new_x = self._next_from_bottom_right(y, x)
                    
        return self._s - (self._img_w*0.5 + self._img_h*0.5j)
