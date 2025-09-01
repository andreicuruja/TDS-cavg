from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox
from cmath import sqrt
lista = []
def sair(): #FUNCIONA
    result = QMessageBox.question(consultorio, "Saindo da calculadora", "Deseja mesmo sair da calculadora?", QMessageBox.Yes, QMessageBox.No)
    if result == QMessageBox.Yes:
        consultorio.close()

def adiciona():
    nome=consultorio.lineEdit.text()
    consultorio.append(nome)#adiciona no vetor
def showdados():
    tam = len(consultorio) #lê o tamanho do vetor
    for i in range(tam):
        consultorio.listWidlw.addItem(consultorio[i])
        listAtendimentos.currentItem().text()
        listPacientes.takeItem(item)

def limpar():
    consultorio.listPacientes.clear()
    consultorio.listAtendimento.clear()

app=QtWidgets.QApplication([])
consultorio=uic.loadUi("consultorio.ui")
consultorio.btnFechar.clicked.connect(sair)
consultorio.btnAdd.clicked.connect(adiciona)
consultorio.btnLimpar.clicked.connect(limpar)
consultorio.show()
app.exec()