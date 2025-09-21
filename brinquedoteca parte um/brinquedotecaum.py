import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

dicionario = {}

def addCrianca():
    nome = janela.le_nome.text().strip()
    idade = janela.sp_idade.value()

    if not nome:
        QMessageBox.warning(janela, "Alerta", "O campo 'Nome da criança' deve ser preenchido.")
        return

    dicionario[nome] = idade
    
    janela.le_nome.clear()
    janela.sp_idade.setValue(0)
    janela.le_nome.setFocus()

def listarTodos():
    janela.lista.clear()
    if not dicionario:
        janela.lista.addItem("Nenhuma criança adicionada.")
    else:
        for nome, idade in dicionario.items():
            janela.lista.addItem(f"{nome} - {idade}")

def limparLista():
    janela.lista.clear()

def sair(): 
    result = QMessageBox.question(janela, "Saindo do dicionário", "Deseja mesmo sair?", QMessageBox.Yes, QMessageBox.No)
    if result == QMessageBox.Yes:
        janela.close()

app = QtWidgets.QApplication(sys.argv)
janela = uic.loadUi("brinquedoteca.ui")
janela.btn_adicionar.clicked.connect(addCrianca)
janela.btn_listar.clicked.connect(listarTodos)
janela.btn_limpar.clicked.connect(limparLista)
janela.btn_fechar.clicked.connect(sair)
janela.show()
sys.exit(app.exec_())