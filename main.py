from f_descriptors import FourierDescriptors
import sys
import imageio

if len(sys.argv) < 6:
    print('Uso: $ python3 main.py <imagem (png)> <canal (int)> <intensidade (int)> <porcentagem (float)> <saida contorno (png)> <saida filtrado (png)>')
    exit(1)

try:
    i_filename = sys.argv[1]
except:
    print('Arquivo inválido: {}'.format(sys.argv[1]))
    exit(1)

try:
    c = int(sys.argv[2])
except:
    print('Canal inválido: {}'.format(sys.argv[2]))
    exit(1)

try:
    i = int(sys.argv[3])
except:
    print('Intensidade inválida: {}'.format(sys.argv[3]))
    exit(1)

try:
    p = float(sys.argv[4])
except:
    print('Porcentagem inválida: {}'.format(sys.argv[5]))
    exit(1)

try:
    o1_filename = sys.argv[5]
except:
    print('Arquivo inválido: {}'.format(sys.argv[5]))
    exit(1)

try:
    o2_filename = sys.argv[6]
except:
    print('Arquivo inválido: {}'.format(sys.argv[5]))

try:
    img = imageio.imread(i_filename)[:, :, c]
except FileNotFoundError:
    print('Arquivo de entrada não encontrado')
    exit(1)
except IndexError:
    print('Índice do Canal inválido')
    exit(1)

if i < 0 or i > 255:
    print('Valor de Intensidade deve estar entre 0-255')
    exit(1)

if p < -100 or p > 100 or p == 0:
    print('Valor da porcentagem deve estar entre [-100, 0) ou (0, 100)')
    exit(1)

fd = FourierDescriptors(img, i, p)

try:
    ctr, ctr_filtered = fd.get_results()
except:
    print('Não há borda com o valor de intensidade {}'.format(i))
    exit(1)

try:
    imageio.imwrite(o1_filename, ctr)
except OSError:
    print('Houve um problema na criação do arquivo {}'.format(o1_filename))
    exit(1)

try:
    imageio.imwrite(o2_filename, ctr_filtered)
except OSError:
    print('Houve um problema na criação do arquivo {}'.format(o2_filename))
    exit(1)
