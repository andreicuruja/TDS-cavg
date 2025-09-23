import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox

lista_criancas = []

def addCrianca():
    nome = janela.le_nome.text().strip()
    idade = janela.sp_idade.value()
    responsavel = janela.le_nome_2.text().strip()

    if not nome or not responsavel:
        QMessageBox.warning(janela, "Alerta", "Os campos 'Nome da criança' e 'Responsável' devem ser preenchidos.")
        return
    
    nova_crianca = {"nome": nome, "idade": idade, "responsavel": responsavel}
    lista_criancas.append(nova_crianca)
    
    janela.le_nome.clear()
    janela.sp_idade.setValue(0)
    janela.le_nome_2.clear()
    janela.le_nome.setFocus()
    # listarTodos()

def listarTodos():
    janela.lista.clear()
    if not lista_criancas:
        janela.lista.addItem("Nenhuma criança adicionada.")
    else:
        for crianca in lista_criancas:
            janela.lista.addItem(f"{crianca['nome']} - {crianca['idade']} anos - Responsavel: {crianca['responsavel']}")
    janela.cb_filtro.setCurrentIndex(0)

def limparLista():
    janela.lista.clear()

def sair(): 
    result = QMessageBox.question(janela, "Saindo do Sistema", "Deseja mesmo sair?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if result == QMessageBox.Yes:
        janela.close()

def filtrar_por_idade():
    idade_selecionada = janela.cb_filtro.currentText()
    
    if idade_selecionada == "Todos":
        listarTodos()
        return

    janela.lista.clear()
    
    try:
        idade_filtro = int(idade_selecionada)
        encontrou_alguem = False

        for crianca in lista_criancas:
            if crianca['idade'] == idade_filtro:
                janela.lista.addItem(f"{crianca['nome']} - {crianca['idade']} - Responsavel: {crianca['responsavel']}")
                encontrou_alguem = True
        
        if not encontrou_alguem:
            janela.lista.addItem(f"Nenhuma criança com {idade_filtro} anos.")
    except ValueError:
        listarTodos()


def remover_item(item):
    texto_completo = item.text()
    
    if " - " not in texto_completo or "Responsavel:" not in texto_completo:
        return
        
    partes = texto_completo.split(' - ')
    nome_para_remover = partes[0]
    
    confirmacao = QMessageBox.question(janela, "Confirmar Remoção",f"Tem certeza que deseja remover o registro de '{nome_para_remover}'?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)

    if confirmacao == QMessageBox.Yes:
        item_para_remover = None
        idade_para_remover = int(partes[1])
        responsavel_para_remover = partes[2].replace('Responsavel: ', '')

        for crianca in lista_criancas:
            if (crianca['nome'] == nome_para_remover and 
                crianca['idade'] == idade_para_remover and 
                crianca['responsavel'] == responsavel_para_remover):
                item_para_remover = crianca
                break
        
        if item_para_remover:
            lista_criancas.remove(item_para_remover)
        
        filtrar_por_idade()

app = QtWidgets.QApplication(sys.argv)
janela = uic.loadUi("brinquedotecatres.ui")

janela.cb_filtro.addItem("Todos")
for idade_opcao in range(1, 13):
    janela.cb_filtro.addItem(str(idade_opcao))

janela.btn_adicionar.clicked.connect(addCrianca)
janela.btn_listar.clicked.connect(listarTodos)
janela.btn_limpar.clicked.connect(limparLista)
janela.btn_fechar.clicked.connect(sair)

janela.cb_filtro.currentIndexChanged.connect(filtrar_por_idade)
janela.lista.itemDoubleClicked.connect(remover_item)

listarTodos()
janela.show()
sys.exit(app.exec_())