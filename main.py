import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QMainWindow, QMessageBox, QPushButton, QLabel, QToolTip, QGridLayout, QWidget, QMessageBox
from PyQt5.QtCore import QSize
import subprocess

class Janela(QMainWindow): #MainWindow
    def __init__(self):
        super(Janela, self).__init__()        
        self.setup_main_window()
        self.carregarJanela() #initUI

    def setup_main_window(self):
        self.x = 800
        self.y = 600
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Processamento Digital de Imagens")
        self.wid = QWidget(self) #Cria o widget
        self.setCentralWidget(self.wid) #Fica no centro da janela
        self.layout = QGridLayout() #Cria o layout em grid
        self.wid.setLayout(self.layout) #Aplica o layout grid no widget

    def carregarJanela(self): #initUI
        #Criar os componentes (Label, Button, Text, Image)

        #Criar a barra de menu
        self.barraMenu = self.menuBar() # Criando a barra de menu

        #Criar o menu
        self.menuArquivo = self.barraMenu.addMenu("&Arquivo") # Criando o menu arquivo
        self.menuTransformacao = self.barraMenu.addMenu("&Transformação") # Criando o menu transformacao
        self.menuSobre = self.barraMenu.addMenu("&Sobre") # Criando o menu sobre

        # Criar actions
        self.acaoAbrir = self.menuArquivo.addAction("Abrir") # Add o action(Botao) no menu arquivo
        self.acaoAbrir.triggered.connect(self.botaoAbrir) # Acao abrir arquivo

        self.acaoFechar = self.menuArquivo.addAction("Fechar") # Add o action(Botao) no menu arquivo
        self.acaoFechar.triggered.connect(self.close) # Ação fechar programa

        self.acaoTransformar1 = self.menuTransformacao.addAction("Contorno") # Add o action(Botao) no menu transformacao
        self.acaoTransformar1.triggered.connect(self.botaoTransformar1) # Ação
        self.menuTransformacao.addSeparator()

        self.acaoTransformar2 = self.menuTransformacao.addAction("Profundidade") # Add o action(Botao) no menu transformacao
        self.acaoTransformar2.triggered.connect(self.botaoTransformar2) # Ação
        self.menuTransformacao.addSeparator()

        self.acaoTransformar3 = self.menuTransformacao.addAction("Realça os Pixel") # Add o action(Botao) no menu transformacao
        self.acaoTransformar3.triggered.connect(self.botaoTransformar3) # Ação
        self.menuTransformacao.addSeparator()

        self.acaoTransformar4 = self.menuTransformacao.addAction("Rotacionar 90º") # Add o action(Botao) no menu transformacao
        self.acaoTransformar4.triggered.connect(self.botaoTransformar4) # Ação

        self.acaoTransformar5 = self.menuTransformacao.addAction("Ratocionar 180º") # Add o action(Botao) no menu transformacao
        self.acaoTransformar5.triggered.connect(self.botaoTransformar5) # Ação
        
        self.acaoTransformar6 = self.menuTransformacao.addAction("Rotacionar 270º") # Add o action(Botao) no menu transformacao
        self.acaoTransformar6.triggered.connect(self.botaoTransformar6) # Ação
        self.menuTransformacao.addSeparator()

        self.acaoTransformar7 = self.menuTransformacao.addAction("Espelhar horizontal") # Add o action(Botao) no menu transformacao
        self.acaoTransformar7.triggered.connect(self.botaoTransformar7) # Ação

        self.acaoTransformar8 = self.menuTransformacao.addAction("Espelhar vetical") # Add o action(Botao) no menu transformacao
        self.acaoTransformar8.triggered.connect(self.botaoTransformar8) # Ação
        self.menuTransformacao.addSeparator()

        self.acaoTransformar9 = self.menuTransformacao.addAction("Transparencia") # Add o action(Botao) no menu transformacao
        self.acaoTransformar9.triggered.connect(self.botaoTransformar9) # Ação

        # Criando o sobre
        self.acaoSobre = self.menuSobre.addAction("Sobre") # Add o action(Botao) no menu sobre
        self.acaoSobre.triggered.connect(self.botaoSobre) # Ação

        #Criando um imagem
        self.imagem1 = QLabel(self) 
        self.endereco1 = 'imagens/arara.jpg'
        self.pixmap1 = QtGui.QPixmap(self.endereco1) 
        self.pixmap1 = self.pixmap1.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem1.setPixmap(self.pixmap1)
        self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

        #Imagem 2
        self.imagem2 = QLabel(self) 
        self.endereco2 = 'imagens/arara.jpg'
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

        #Organizando os componentes Widgets dentro do GridLayout
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)

    #OpenFileDialog
    def botaoAbrir(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption='Abrir arquivo', 
                                                            directory=QtCore.QDir.currentPath(), 
                                                            filter='All files (*.*);; Imagens (*.jpg; *.png)',
                                                            initialFilter='Imagens (*.jpg; *.png)')
        self.endereco1 = fileName
        self.pixmap1 = QtGui.QPixmap(self.endereco1) 
        self.pixmap1 = self.pixmap1.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)

    def botaoTransformar1(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_contorno.jpg'
        self.script = '.\contorno.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar2(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_emboss.jpg'
        self.script = '.\emboss.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar3(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_pixel.jpg'
        self.script = '.\pixel.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar4(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_rotacionar_90.jpg'
        self.script = '.\grau_90.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar5(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_rotacioanr_180.jpg'
        self.script = '.\grau_180.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar6(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_rotacioanr_270.jpg'
        self.script = '.\grau_270.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar7(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_espelho_horizontal.jpg'
        self.script = '.\espelhar_horizontal.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar8(self):
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_espelho_vertical.jpg'
        self.script = '.\espelhar_vertical.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransformar9(self):
        trans, okPressed = QInputDialog.getInt(self, "Inserir a porcentagem","Percentagem:", 10, 0, 100, 1)
        if okPressed:
            valor = str(trans)
        self.imagemOriginal = self.endereco1
        self.imagemComFiltro = 'imagens/arquivo_novo_transparencia.png'
        self.script = '.\Transparencia.py'
        self.programa = 'python ' + self.script + ' \"' + self.imagemOriginal + '\" ' + self.imagemComFiltro + ' ' + valor
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imagemComFiltro
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio) # Deixa a imagem do tamanho desejado
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)
        
    def botaoSobre(self):
        self.menssagem = QMessageBox()
        self.menssagem.setWindowTitle("Sobre")
        self.menssagem.setText("Desenvolvido por Carlos Eduardo Casteliano de Paula\nAplicativo de transformação de imagens.\nItuiutaba, 21 de maio de 2021.")
        self.menssagem.setDetailedText("Utilizei os seguintes filtros:\nCONTOUR: Mostra o contorno, realça a diferencia de cor entros os pixels.\nEMBOSS: Da profundidade nos objetos / mostra o relevo entre pixels.\nEDGE ENHANCE MORE: Realça muito os pixels\nFLIP_LEFT_RIGTH: Espelha a imagem no sentido horizontal (Os pixels da esquerda vão para direita e da direta vão pra esquerda.\nFLIP_TOP_BOTTOM: Espelha a imagem no sentido vertical (Os pixels superiores vão para baixo e os inferiores vão para cima.\nROTATE_90: Rotaciona a imagem em 90º.\nROTATE_180: Rotaciona a imagem em 180º.\nROTATE_270: Rotaciona a imagem em 270º.\nTRANSPARENCIA: Ao informar a porcentagem e aplicado na imagem.")
        self.menssagem.exec_()

aplicacao = QApplication(sys.argv)        
j = Janela() #MainWindow
j.show()
sys.exit(aplicacao.exec_())