import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import pymysql
from reportlab.pdfgen import canvas

numero_id = 0

try:
    banco = pymysql.connect(host="localhost", user="root", password="", database="sistema", connect_timeout=5)
except Exception as e:
    print("Erro Banco:", e)
    sys.exit()

def logar():
    usuario = flogin.le_usuario.text()
    senha = flogin.le_senha.text()
    cursor = banco.cursor()
    cursor.execute("SELECT senha, usuario FROM usuarios WHERE senha =%s AND usuario = %s", (senha, usuario))
    resultado = cursor.fetchone()
    if resultado:
        flogin.close()
        fmenu.show()
    else:
        QMessageBox.about(flogin, "Aviso", "Dados inválidos!")

def tela_prod():
    fprod.show()

def tela_user():
    fuser.show()

def cadastrar_dados():
    vprod = fprod.lineEdit_2.text()
    vpreco = fprod.lineEdit_3.text()
    vcat = "Outros"
    if fprod.radioButton_1.isChecked(): vcat = "Alimentos"
    elif fprod.radioButton_2.isChecked(): vcat = "Eletronicos"
    elif fprod.radioButton_3.isChecked(): vcat = "Informática"
    cursor = banco.cursor()
    cursor.execute("INSERT INTO produtos (descricao, preco, categoria) VALUES (%s, %s, %s)", (str(vprod), str(vpreco), vcat))
    banco.commit()
    fprod.lineEdit_2.clear()
    fprod.lineEdit_3.clear()
    QMessageBox.information(fprod, "Cadastro", "Produto cadastrado com sucesso!")
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

def excluir_dados():
    linha = flistaprod.tableWidget.currentRow()
    if linha < 0: return QMessageBox.warning(flistaprod, "Erro", "Selecione item")
    flistaprod.tableWidget.removeRow(linha)
    cursor = banco.cursor()
    cursor.execute("SELECT id_produto FROM produtos")
    valor_id = cursor.fetchall()[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id_produto=" + str(valor_id))
    banco.commit()

def editar_dados():
    global numero_id
    linha = flistaprod.tableWidget.currentRow()
    if linha < 0: return QMessageBox.warning(flistaprod, "Erro", "Selecione item")
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

def salvar_valor_editado():
    cursor = banco.cursor()
    cursor.execute(f"UPDATE produtos SET descricao='{feditar.lineEdit_2.text()}', preco='{feditar.lineEdit_3.text()}', categoria='{feditar.lineEdit_4.text()}' WHERE id_produto={numero_id}")
    banco.commit()
    feditar.close()
    flistaprod.close()
    listar_prod()
    QMessageBox.information(flistaprod, "Sucesso", "Atualizado!")

def gerar_pdf():
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
    QMessageBox.information(flistaprod, "PDF", "Gerado com sucesso!")

def cadastro_user():
    usuario = fuser.le_usuario.text()
    senha = fuser.le_senha.text()
    senha2 = fuser.le_senha2.text()
    if senha == senha2:
        cursor = banco.cursor()
        cursor.execute("INSERT INTO usuarios (senha, usuario) VALUES (%s, %s)", (senha, usuario))
        banco.commit()
        QMessageBox.about(fuser, "Aviso", "Usuário cadastrado com sucesso")
        fuser.le_usuario.clear()
        fuser.le_senha.clear()
        fuser.le_senha2.clear()
        fuser.close()
    else:
        QMessageBox.about(fuser, "Atenção", "Senhas incorretas, digite novamente")
        fuser.le_senha.clear()
        fuser.le_senha2.clear()
        fuser.le_senha2.setFocus()

def fechar_telaprod():
    fprod.close()

app = QtWidgets.QApplication([])
flogin = uic.loadUi("login.ui")
fmenu = uic.loadUi("menu.ui")
fprod = uic.loadUi("produtos.ui")
flistaprod = uic.loadUi("listar_produtos.ui")
feditar = uic.loadUi("menu_editar.ui")
fuser = uic.loadUi("cadastro_user.ui")

flogin.bt_login.clicked.connect(logar)
flogin.bt_cadastrar.clicked.connect(tela_user)
fmenu.bt_prod.clicked.connect(tela_prod)
fmenu.bt_usuar.clicked.connect(tela_user)
fmenu.btfechar.clicked.connect(app.quit)
fprod.pushButton.clicked.connect(cadastrar_dados)
fprod.pushButton_2.clicked.connect(listar_prod)
fprod.btfechar.clicked.connect(fechar_telaprod)
flistaprod.btexcluir.clicked.connect(excluir_dados)
flistaprod.bteditar.clicked.connect(editar_dados)
flistaprod.btpdf.clicked.connect(gerar_pdf)
flistaprod.btfechar.clicked.connect(flistaprod.close)
feditar.btsalvar.clicked.connect(salvar_valor_editado)
fuser.bt_salvar.clicked.connect(cadastro_user)
fuser.bt_fechar.clicked.connect(fuser.close)

flogin.show()
app.exec()