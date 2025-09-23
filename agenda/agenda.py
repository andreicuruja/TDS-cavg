import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

agenda = []
arquivoUi = "agenda.ui"

def adicionar():
    nome = janela.contatoNome.text().strip()
    telefone = janela.contatoTel.text().strip()
    email = janela.contatoEmail.text().strip()

    if not nome:
        QMessageBox.warning(janela, "Atenção", "O campo 'Nome' é obrigatório.")
        return

    contatoExistente = None
    for c in agenda:
        if c['nome'].lower() == nome.lower():
            contatoExistente = c
            break
    
    if contatoExistente:
        contatoExistente['telefone'] = telefone
        contatoExistente['email'] = email
    else:
        agenda.append({"nome": nome, "telefone": telefone, "email": email})
    
    listar()
    limpar()

def listar():
    termoBusca = janela.buscarpornome.text().strip().lower()
    janela.contatosTabela.setRowCount(0)

    for contato in agenda:
        if not termoBusca or termoBusca in contato['nome'].lower():
            linha = janela.contatosTabela.rowCount()
            janela.contatosTabela.insertRow(linha)
            janela.contatosTabela.setItem(linha, 0, QTableWidgetItem(contato["nome"]))
            janela.contatosTabela.setItem(linha, 1, QTableWidgetItem(contato["telefone"]))
            janela.contatosTabela.setItem(linha, 2, QTableWidgetItem(contato["email"]))

def limpar():
    janela.contatoNome.clear()
    janela.contatoTel.clear()
    janela.contatoEmail.clear()
    janela.contatoNome.setFocus()

def remover():
    linhaSelecionada = janela.contatosTabela.currentRow()

    if linhaSelecionada < 0:
        QMessageBox.warning(janela, "Atenção", "Selecione um contato para remover.")
        return

    nomeSelecionado = janela.contatosTabela.item(linhaSelecionada, 0).text()
    
    confirmar = QMessageBox.question(janela, "Confirmar", f"Deseja remover o contato '{nomeSelecionado}'?", QMessageBox.Yes | QMessageBox.No)

    if confirmar == QMessageBox.Yes:
        for contato in agenda:
            if contato['nome'] == nomeSelecionado:
                agenda.remove(contato)
                break
        listar()

def sair():
    confirmar = QMessageBox.question(janela, "Sair", "Deseja realmente sair?", QMessageBox.Yes | QMessageBox.No)
    if confirmar == QMessageBox.Yes:
        janela.close()

app = QtWidgets.QApplication(sys.argv)
janela = uic.loadUi(arquivoUi)

janela.contatoAddAtt.clicked.connect(adicionar)
janela.contatoLimpar.clicked.connect(limpar)
janela.listar.clicked.connect(listar)
janela.buscarpornome.textChanged.connect(listar)
janela.contatosRemove.clicked.connect(remover)
janela.contatosSair.clicked.connect(sair)

listar()
janela.show()
sys.exit(app.exec_())