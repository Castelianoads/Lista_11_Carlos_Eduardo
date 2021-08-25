# -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageFilter

#Checando e imprimindo os argumentos de linha de comando
if __name__ == "__main__":
    print(f'Quantos argumentos: {len(sys.argv)}')
    for i, arg in enumerate(sys.argv):
        print(f"Argumento {i}: {arg}")      

# Codigo da conversao
imagemOriginal = Image.open(sys.argv[1])

#O filtro EMBOSS da profundidade nos objetos/ mostra o relevo
imagemComFiltro = imagemOriginal.filter(ImageFilter.EMBOSS)

imagemComFiltro.save(sys.argv[2])