import sys
import re
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymysql
from reportlab.pdfgen import canvas
from pyUFbr.baseuf import ufbr

try:
    banco = pymysql.connect(host="localhost", user="root", password="", database="sistema", connect_timeout=5)
except Exception as e:
    print("Erro Banco:", e)
    sys.exit()

def logar():
    usuario = flogin.le_usuario.text()
    senha = flogin.le_senha.text()
    cursor = banco.cursor()
    cursor.execute("SELECT senha, usuario FROM usuarios WHERE usuario = %s AND senha = %s", (usuario, senha))
    if cursor.fetchone():
        flogin.close()
        fmenu.show()
    else:
        QMessageBox.warning(flogin, "Erro", "Dados inválidos!")

def tela_prod():
    fprod.show()

def tela_user():
    fuser.show()

def tela_cli():
    fcli.show()
    mostra_estados()

def mostra_estados():
    estados = ufbr.list_uf
    fcli.cbest.clear()
    fcli.cbest.addItems(estados)

def mostra_cidades():
    fcli.cbcid.clear()
    filtro = fcli.cbest.currentText()
    cidades = ufbr.list_cidades(filtro)
    fcli.cbcid.addItems(cidades)

def valida_cpf():
    return True

def cadastro_clientes():
    if not valida_cpf():
        return QMessageBox.warning(fcli, "Erro", "CPF Inválido!")
    nome = fcli.lnome.text()
    ender = fcli.lender.text()
    email = fcli.lemail.text()
    tel = fcli.ltel.text()
    cpf = fcli.lcpf.text()
    cep = fcli.lcep.text()
    est = fcli.cbest.currentText()
    cid = fcli.cbcid.currentText()
    try:
        cursor = banco.cursor()
        sql = "INSERT INTO clientes (nome, endereco, telefone, email, cidade, estado, cpf, cep) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (nome, ender, tel, email, cid, est, cpf, cep))
        banco.commit()
        QMessageBox.information(fcli, "Sucesso", "Cliente cadastrado!")
        fcli.lnome.clear()
        fcli.lender.clear()
        fcli.lemail.clear()
        fcli.ltel.clear()
        fcli.lcpf.clear()
        fcli.lcep.clear()
    except Exception as e:
        QMessageBox.warning(fcli, "Erro", f"Erro ao cadastrar: {e}")

def listar_clientes():
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM clientes")
    dados = cursor.fetchall()
    print(dados) 
    QMessageBox.information(fcli, "Listar", "Dados listados no terminal!")

def cadastrar_prod():
    vprod = fprod.lineEdit_2.text()
    vpreco = fprod.lineEdit_3.text()
    vcat = "Outros"
    if fprod.radioButton_1.isChecked():
        vcat = "Alimentos"
    elif fprod.radioButton_2.isChecked():
        vcat = "Eletronicos"
    elif fprod.radioButton_3.isChecked():
        vcat = "Informática"
    cursor = banco.cursor()
    cursor.execute("INSERT INTO produtos (descricao, preco, categoria) VALUES (%s, %s, %s)", (str(vprod), str(vpreco), vcat))
    banco.commit()
    fprod.lineEdit_2.clear()
    fprod.lineEdit_3.clear()
    QMessageBox.information(fprod, "Cadastro", "Produto cadastrado!")
    fprod.show()

def listar_prod():
    flistaprod.show()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM produtos")
    dados = cursor.fetchall()
    flistaprod.tableWidget.setRowCount(len(dados))
    flistaprod.tableWidget.setColumnCount(4)
    for i in range(len(dados)):
        for j in range(4):
            flistaprod.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))

def excluir_prod():
    linha = flistaprod.tableWidget.currentRow()
    if linha < 0:
        return QMessageBox.warning(flistaprod, "Erro", "Selecione item")
    flistaprod.tableWidget.removeRow(linha)
    cursor = banco.cursor()
    cursor.execute("SELECT id_produto FROM produtos")
    valor_id = cursor.fetchall()[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id_produto=" + str(valor_id))
    banco.commit()

def editar_prod():
    global numero_id
    linha = flistaprod.tableWidget.currentRow()
    if linha < 0:
        return QMessageBox.warning(flistaprod, "Erro", "Selecione item")
    cursor = banco.cursor()
    cursor.execute("SELECT id_produto FROM produtos")
    valor_id = cursor.fetchall()[linha][0]
    cursor.execute("SELECT * FROM produtos WHERE id_produto=" + str(valor_id))
    prod = cursor.fetchall()[0]
    feditar.show()
    feditar.lineEdit.setText(str(prod[0]))
    feditar.lineEdit_2.setText(str(prod[1]))
    feditar.lineEdit_3.setText(str(prod[2]))
    feditar.lineEdit_4.setText(str(prod[3]))
    numero_id = valor_id

def salvar_edit_prod():
    cursor = banco.cursor()
    cursor.execute(f"UPDATE produtos SET descricao='{feditar.lineEdit_2.text()}', preco='{feditar.lineEdit_3.text()}', categoria='{feditar.lineEdit_4.text()}' WHERE id_produto={numero_id}")
    banco.commit()
    feditar.close()
    flistaprod.close()
    listar_prod()
    QMessageBox.information(flistaprod, "Sucesso", "Atualizado!")

def gerar_pdf_prod():
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM produtos")
    dados = cursor.fetchall()
    pdf = canvas.Canvas("cadastro_produtos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200, 800, "Produtos cadastrados:")
    pdf.setFont("Times-Bold", 18)
    pdf.drawString(10, 750, "ID")
    pdf.drawString(110, 750, "PRODUTO")
    pdf.drawString(210, 750, "PREÇO")
    pdf.drawString(310, 750, "CATEGORIA")
    y = 750
    for d in dados:
        y -= 50
        pdf.drawString(10, y, str(d[0]))
        pdf.drawString(110, y, str(d[1]))
        pdf.drawString(210, y, str(d[2]))
        pdf.drawString(310, y, str(d[3]))
    pdf.save()
    QMessageBox.information(flistaprod, "PDF", "Gerado!")

def cadastro_user():
    if fuser.le_senha.text() == fuser.le_senha2.text():
        cursor = banco.cursor()
        cursor.execute("INSERT INTO usuarios (senha, usuario) VALUES (%s, %s)", (fuser.le_senha.text(), fuser.le_usuario.text()))
        banco.commit()
        QMessageBox.information(fuser, "Aviso", "Usuário cadastrado!")
        fuser.close()
    else:
        QMessageBox.warning(fuser, "Erro", "Senhas não conferem!")

def fechar_telaprod():
    fprod.close()

app = QtWidgets.QApplication([])

flogin = uic.loadUi("login.ui")
fmenu = uic.loadUi("menu.ui")
fprod = uic.loadUi("produtos.ui")
flistaprod = uic.loadUi("listar_produtos.ui")
feditar = uic.loadUi("menu_editar.ui")
fuser = uic.loadUi("cadastro_user.ui")
fcli = uic.loadUi("clientes.ui")

flogin.bt_login.clicked.connect(logar)
flogin.bt_cadastrar.clicked.connect(tela_user)
fmenu.bt_prod.clicked.connect(tela_prod)
fmenu.bt_usuar.clicked.connect(tela_user)
fmenu.bt_clien.clicked.connect(tela_cli)
fmenu.btfechar.clicked.connect(app.quit)
fprod.pushButton.clicked.connect(cadastrar_prod)
fprod.pushButton_2.clicked.connect(listar_prod)
fprod.btfechar.clicked.connect(fechar_telaprod)
flistaprod.btexcluir.clicked.connect(excluir_prod)
flistaprod.bteditar.clicked.connect(editar_prod)
flistaprod.btpdf.clicked.connect(gerar_pdf_prod)
flistaprod.btfechar.clicked.connect(flistaprod.close)
feditar.btsalvar.clicked.connect(salvar_edit_prod)
fuser.bt_salvar.clicked.connect(cadastro_user)
fuser.bt_fechar.clicked.connect(fuser.close)
fcli.btcadastrar.clicked.connect(cadastro_clientes)
fcli.btlistar.clicked.connect(listar_clientes)
fcli.btfechar.clicked.connect(fcli.close)
fcli.cbest.currentIndexChanged.connect(mostra_cidades)

flogin.show()
app.exec()