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

def tela_prod(): fprod.show()
def tela_user(): fuser.show()
def tela_cli(): fcli.show(); mostra_estados()
def tela_forn(): fforn.show()

def cadastrar_forn():
    nome = fforn.lnome.text()
    cnpj = fforn.lcnpj.text()
    tel = fforn.ltel.text()
    email = fforn.lemail.text()
    try:
        cursor = banco.cursor()
        cursor.execute("INSERT INTO fornecedores (nome, cnpj, telefone, email) VALUES (%s, %s, %s, %s)", (nome, cnpj, tel, email))
        banco.commit()
        QMessageBox.information(fforn, "Sucesso", "Fornecedor cadastrado!")
        fforn.lnome.clear(); fforn.lcnpj.clear(); fforn.ltel.clear(); fforn.lemail.clear()
    except Exception as e:
        QMessageBox.warning(fforn, "Erro", f"Erro: {e}")

def listar_forn():
    flista_forn.show()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM fornecedores")
    dados = cursor.fetchall()
    flista_forn.tableWidget.setRowCount(len(dados))
    flista_forn.tableWidget.setColumnCount(4)
    for i in range(len(dados)):
        flista_forn.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(dados[i][1])))
        flista_forn.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(dados[i][2])))
        flista_forn.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(dados[i][3])))
        flista_forn.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(dados[i][4])))

def excluir_forn():
    linha = flista_forn.tableWidget.currentRow()
    if linha < 0: return QMessageBox.warning(flista_forn, "Erro", "Selecione item")
    flista_forn.tableWidget.removeRow(linha)
    cursor = banco.cursor()
    cursor.execute("SELECT id_fornecedor FROM fornecedores")
    id_val = cursor.fetchall()[linha][0]
    cursor.execute(f"DELETE FROM fornecedores WHERE id_fornecedor={id_val}")
    banco.commit()

def editar_forn():
    global numero_id
    linha = flista_forn.tableWidget.currentRow()
    if linha < 0: return QMessageBox.warning(flista_forn, "Erro", "Selecione item")
    cursor = banco.cursor()
    cursor.execute("SELECT id_fornecedor FROM fornecedores")
    numero_id = cursor.fetchall()[linha][0]
    cursor.execute(f"SELECT * FROM fornecedores WHERE id_fornecedor={numero_id}")
    dado = cursor.fetchall()[0]
    feditar.show()
    
    feditar.label.setText("Editar Fornecedor")
    feditar.label_2.setText("  ID           NOME             CNPJ           TELEFONE") 
    
    feditar.lineEdit.setText(str(dado[0]))
    feditar.lineEdit_2.setText(str(dado[1]))
    feditar.lineEdit_3.setText(str(dado[2]))
    feditar.lineEdit_4.setText(str(dado[3]))

def salvar_edit_forn():
    nome = feditar.lineEdit_2.text()
    cnpj = feditar.lineEdit_3.text()
    tel = feditar.lineEdit_4.text()
    cursor = banco.cursor()
    cursor.execute(f"UPDATE fornecedores SET nome='{nome}', cnpj='{cnpj}', telefone='{tel}' WHERE id_fornecedor={numero_id}")
    banco.commit()
    feditar.close(); flista_forn.close(); listar_forn()
    QMessageBox.information(flista_forn, "Sucesso", "Atualizado!")

def gerar_pdf_forn():
    cursor = banco.cursor(); cursor.execute("SELECT * FROM fornecedores"); dados = cursor.fetchall()
    pdf = canvas.Canvas("relatorio_fornecedores.pdf")
    pdf.setFont("Times-Bold", 25); pdf.drawString(200, 800, "Fornecedores")
    pdf.setFont("Times-Bold", 12); y = 750
    pdf.drawString(10, y, "ID | NOME | CNPJ | TELEFONE | EMAIL")
    for d in dados:
        y -= 50
        pdf.drawString(10, y, f"{d[0]} | {d[1]} | {d[2]} | {d[3]} | {d[4]}")
    pdf.save(); QMessageBox.information(flista_forn, "PDF", "Gerado!")

def mostra_estados():
    fcli.cbest.clear(); fcli.cbest.addItems(ufbr.list_uf)
def mostra_cidades():
    fcli.cbcid.clear(); fcli.cbcid.addItems(ufbr.list_cidades(fcli.cbest.currentText()))
def valida_cpf(): return True

def cadastro_clientes():
    if not valida_cpf(): return QMessageBox.warning(fcli, "Erro", "CPF Inválido!")
    try:
        cursor = banco.cursor()
        cursor.execute("INSERT INTO clientes (nome, endereco, telefone, email, cidade, estado, cpf, cep) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", 
                       (fcli.lnome.text(), fcli.lender.text(), fcli.ltel.text(), fcli.lemail.text(), fcli.cbcid.currentText(), fcli.cbest.currentText(), fcli.lcpf.text(), fcli.lcep.text()))
        banco.commit(); QMessageBox.information(fcli, "Sucesso", "Cliente cadastrado!")
        fcli.lnome.clear()
    except Exception as e: QMessageBox.warning(fcli, "Erro", f"Erro: {e}")

def listar_clientes():
    cursor = banco.cursor(); cursor.execute("SELECT * FROM clientes"); print(cursor.fetchall())
    QMessageBox.information(fcli, "Info", "Dados listados no terminal")

def cadastrar_prod():
    vcat = "Outros"
    if fprod.radioButton_1.isChecked(): vcat = "Alimentos"
    elif fprod.radioButton_2.isChecked(): vcat = "Eletronicos"
    elif fprod.radioButton_3.isChecked(): vcat = "Informática"
    cursor = banco.cursor()
    cursor.execute("INSERT INTO produtos (descricao, preco, categoria) VALUES (%s, %s, %s)", (fprod.lineEdit_2.text(), fprod.lineEdit_3.text(), vcat))
    banco.commit(); fprod.lineEdit_2.clear(); fprod.lineEdit_3.clear(); QMessageBox.information(fprod, "Info", "Produto cadastrado!")

def listar_prod():
    flistaprod.show(); cursor = banco.cursor(); cursor.execute("SELECT * FROM produtos"); dados = cursor.fetchall()
    flistaprod.tableWidget.setRowCount(len(dados)); flistaprod.tableWidget.setColumnCount(4)
    for i in range(len(dados)):
        for j in range(4): flistaprod.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))

def excluir_prod():
    row = flistaprod.tableWidget.currentRow()
    if row < 0: return QMessageBox.warning(flistaprod, "Erro", "Selecione item")
    flistaprod.tableWidget.removeRow(row)
    cursor = banco.cursor(); cursor.execute("SELECT id_produto FROM produtos"); id_val = cursor.fetchall()[row][0]
    cursor.execute(f"DELETE FROM produtos WHERE id_produto={id_val}"); banco.commit()

def editar_prod():
    global numero_id
    row = flistaprod.tableWidget.currentRow()
    if row < 0: return QMessageBox.warning(flistaprod, "Erro", "Selecione item")
    cursor = banco.cursor(); cursor.execute("SELECT id_produto FROM produtos"); numero_id = cursor.fetchall()[row][0]
    cursor.execute(f"SELECT * FROM produtos WHERE id_produto={numero_id}"); prod = cursor.fetchall()[0]
    feditar.show()
    
    feditar.label.setText("Edite esse produto:")
    feditar.label_2.setText("  CÓDIGO           PRODUTO           PREÇO        CATEGORIA")
    
    feditar.lineEdit.setText(str(prod[0])); feditar.lineEdit_2.setText(str(prod[1]))
    feditar.lineEdit_3.setText(str(prod[2])); feditar.lineEdit_4.setText(str(prod[3]))

def salvar_edit_prod():
    if "Fornecedor" in feditar.label.text():
        salvar_edit_forn()
    else:
        cursor = banco.cursor()
        cursor.execute(f"UPDATE produtos SET descricao='{feditar.lineEdit_2.text()}', preco='{feditar.lineEdit_3.text()}', categoria='{feditar.lineEdit_4.text()}' WHERE id_produto={numero_id}")
        banco.commit(); feditar.close(); flistaprod.close(); listar_prod()

def gerar_pdf_prod():
    cursor = banco.cursor(); cursor.execute("SELECT * FROM produtos"); dados = cursor.fetchall()
    pdf = canvas.Canvas("cadastro_produtos.pdf"); pdf.setFont("Times-Bold", 25); pdf.drawString(200, 800, "Produtos"); y = 750
    for d in dados: y -= 50; pdf.drawString(10, y, f"{d[0]} | {d[1]} | {d[2]} | {d[3]}")
    pdf.save(); QMessageBox.information(flistaprod, "PDF", "Gerado!")

def cadastro_user():
    if fuser.le_senha.text() == fuser.le_senha2.text():
        cursor = banco.cursor()
        cursor.execute("INSERT INTO usuarios (senha, usuario) VALUES (%s, %s)", (fuser.le_senha.text(), fuser.le_usuario.text()))
        banco.commit(); QMessageBox.information(fuser, "Aviso", "Cadastrado!"); fuser.close()
    else: QMessageBox.warning(fuser, "Erro", "Senhas diferentes!")

def fechar_telaprod(): fprod.close()

app = QtWidgets.QApplication([])

try:
    flogin = uic.loadUi("login.ui")
    fmenu = uic.loadUi("menu.ui")
    fprod = uic.loadUi("produtos.ui")
    flistaprod = uic.loadUi("listar_produtos.ui")
    feditar = uic.loadUi("menu_editar.ui")
    fuser = uic.loadUi("cadastro_user.ui")
    fcli = uic.loadUi("clientes.ui")
    fforn = uic.loadUi("fornecedores.ui")
    flista_forn = uic.loadUi("listar_fornecedores.ui")
except Exception as e:
    print("ERRO AO CARREGAR UI:", e)
    sys.exit()

flogin.bt_login.clicked.connect(logar); flogin.bt_cadastrar.clicked.connect(tela_user)
fmenu.bt_prod.clicked.connect(tela_prod); fmenu.bt_usuar.clicked.connect(tela_user)
fmenu.bt_clien.clicked.connect(tela_cli)
fmenu.bt_forn.clicked.connect(tela_forn)
fmenu.btfechar.clicked.connect(app.quit)

fprod.pushButton.clicked.connect(cadastrar_prod); fprod.pushButton_2.clicked.connect(listar_prod); fprod.btfechar.clicked.connect(fechar_telaprod)
flistaprod.btexcluir.clicked.connect(excluir_prod); flistaprod.bteditar.clicked.connect(editar_prod)
flistaprod.btpdf.clicked.connect(gerar_pdf_prod); flistaprod.btfechar.clicked.connect(flistaprod.close)
feditar.btsalvar.clicked.connect(salvar_edit_prod)

fuser.bt_salvar.clicked.connect(cadastro_user); fuser.bt_fechar.clicked.connect(fuser.close)
fcli.btcadastrar.clicked.connect(cadastro_clientes); fcli.btlistar.clicked.connect(listar_clientes)
fcli.btfechar.clicked.connect(fcli.close); fcli.cbest.currentIndexChanged.connect(mostra_cidades)

fforn.bt_cadastrar.clicked.connect(cadastrar_forn)
fforn.bt_listar.clicked.connect(listar_forn)
fforn.bt_fechar.clicked.connect(fforn.close)

flista_forn.bt_excluir.clicked.connect(excluir_forn)
flista_forn.bt_editar.clicked.connect(editar_forn)
flista_forn.bt_pdf.clicked.connect(gerar_pdf_forn)
flista_forn.bt_fechar.clicked.connect(flista_forn.close)

flogin.show()
app.exec()