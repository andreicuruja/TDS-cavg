import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

dicionario = {}

def adicionar_crianca():
    nome = janela.le_nome.text().strip()
    idade = janela.sp_idade.value()

    if not nome:
        QMessageBox.warning(janela, "Alerta", "O campo 'Nome da criança' deve ser preenchido.")
        return
    
    if nome in dicionario:
        QMessageBox.warning(janela, "Alerta", f"A criança '{nome}' já está cadastrada.")
        return

    dicionario[nome] = idade
    
    janela.le_nome.clear()
    janela.sp_idade.setValue(0)
    janela.le_nome.setFocus()
   # listar_todos() 

def listar_todos():
    janela.lista.clear()
    if not dicionario:
        janela.lista.addItem("Nenhuma criança adicionada.")
    else:
        for nome in sorted(dicionario):
            idade = dicionario[nome]
            janela.lista.addItem(f"{nome} - {idade}")
    janela.cb_filtro.setCurrentIndex(0)

def limpar_lista_visual():
    janela.lista.clear()

def fechar_programa(): 
    result = QMessageBox.question(janela, "Saindo do Sistema", "Deseja mesmo sair?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if result == QMessageBox.Yes:
        janela.close()

def filtrar_por_idade():
    idade_selecionada = janela.cb_filtro.currentText()
    
    if idade_selecionada == "Todos":
        listar_todos()
        return

    janela.lista.clear()
    
    idade_filtro = int(idade_selecionada)
    encontrou_alguem = False

    for nome, idade in dicionario.items():
        if idade == idade_filtro:
            janela.lista.addItem(f"{nome} - {idade}")
            encontrou_alguem = True
    
    if not encontrou_alguem:
        janela.lista.addItem(f"Nenhuma criança com {idade_filtro} anos.")

def remover_item(item):
    texto_completo = item.text()
    
    if " - " not in texto_completo:
        return
        
    nome_para_remover = texto_completo.split(' - ')[0]
    
    confirmacao = QMessageBox.question(janela, 
                                       "Confirmar Remoção", 
                                       f"Tem certeza que deseja remover '{nome_para_remover}'?",
                                       QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)

    if confirmacao == QMessageBox.Yes:
        if nome_para_remover in dicionario:
            del dicionario[nome_para_remover]
        
        filtrar_por_idade()

app = QtWidgets.QApplication(sys.argv)
janela = uic.loadUi("brinquedotecadois.ui")

janela.cb_filtro.addItem("Todos")
for idade_opcao in range(1, 13):
    janela.cb_filtro.addItem(str(idade_opcao))

janela.btn_adicionar.clicked.connect(adicionar_crianca)
janela.btn_listar.clicked.connect(listar_todos)
janela.btn_limpar.clicked.connect(limpar_lista_visual)
janela.btn_fechar.clicked.connect(fechar_programa)

janela.cb_filtro.currentIndexChanged.connect(filtrar_por_idade)
janela.lista.itemDoubleClicked.connect(remover_item)

listar_todos()
janela.show()

sys.exit(app.exec_())

