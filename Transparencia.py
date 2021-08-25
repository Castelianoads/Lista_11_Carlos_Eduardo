# -*- coding: utf-8 -*-
import sys
from PIL import Image

# PNG = RGBA (235, 170, 10, 255) 255 totalmente opaco e 0 e totalmente transparente

# Checando e imprimindo os argumentos de linha de comando
if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")      

# Abrindo imagem
imagemOriginal = Image.open(sys.argv[1])

# Converter para PNG
imagemOriginalPNG = imagemOriginal.convert('RGBA')

# Mostra os pixels
pixels = list(imagemOriginalPNG.getdata())

for i, p in enumerate(pixels):
    pixels[i] = (p[0], p[1], p[2], int(sys.argv[3]))

imagemComFiltro = Image.new('RGBA', imagemOriginal.size)
imagemComFiltro.putdata(pixels)
imagemComFiltro.save(sys.argv[2])