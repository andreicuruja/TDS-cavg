#importar 
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox

def exibir_mensagem():
    dado_lido = janela.lineEdit.text()
    print(dado_lido)
    janela.lineEdit.setText("")
    QMessageBox.about(janela,"alerta", dado_lido)

#exercicio dois:
def exibir_mensagem():
    dado_lido = janela.lineEdit.text()
    print(dado_lido)
    janela.lineEdit.setText("")
    if dado_lido=="":
        QMessageBox.about(janela,"Nome:", "Nenhum nome foi digitado")
    else:
        QMessageBox.about(janela,"Nome:", "Olá, "+dado_lido)

def fechar_tela():
    result = QMessageBox.question(janela, "Saindo do sistema", "Deseja mesmo sair do sistema?", QMessageBox.Yes, QMessageBox.No)
    if result == QMessageBox.Yes:
        janela.close()

def listar_dados():
    dado_lido = janela.lineEdit.text()
    janela.lista.addItem(dado_lido)

def deletar():
    janela.lista.clear()

def contar_itens():
    valor = janela.lista.count()
    # janela.lbconta.setText("Qtde de itens: " + str(valor))

def ordenar():
    janela.lista.sortItems()
    
#programa principal
app=QtWidgets.QApplication([])
janela=uic.loadUi("janelauntitled.ui")
janela.PushButton.clicked.connect(exibir_mensagem)
janela.show()
janela.btfechar.clicked.connect(fechar_tela)
janela.btadicionar.clicked.connect(listar_dados)
janela.btexcluir.clicked.connect(deletar)
janela.btadicionar.clicked.connect(contar_itens)
janela.btordenar.clicked.connect(ordenar)
app.exec()
