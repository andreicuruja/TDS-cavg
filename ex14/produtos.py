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

def cadastrar_dados():
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
    QMessageBox.information(fprod, "Cadastro", "Salvo com sucesso!")

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
    if linha < 0:
        return QMessageBox.warning(flistaprod, "Erro", "Selecione item")
    flistaprod.tableWidget.removeRow(linha)
    cursor = banco.cursor()
    cursor.execute("SELECT id_produto FROM produtos")
    valor_id = cursor.fetchall()[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id_produto=" + str(valor_id))
    banco.commit()

def editar_dados():
    global numero_id
    linha = flistaprod.tableWidget.currentRow()
    if linha < 0:
        return QMessageBox.warning(flistaprod, "Erro", "Selecione item")
    cursor = banco.cursor()
    cursor.execute("SELECT id_produto FROM produtos")
    valor_id = cursor.fetchall()[linha][0]
    cursor.execute("SELECT * FROM produtos WHERE id_produto=" + str(valor_id))
    prod = cursor.fetchall()[0]
    tela_editar.show()
    tela_editar.lineEdit.setText(str(prod[0]))
    tela_editar.lineEdit_2.setText(str(prod[1]))
    tela_editar.lineEdit_3.setText(str(prod[2]))
    tela_editar.lineEdit_4.setText(str(prod[3]))
    numero_id = valor_id

def salvar_valor_editado():
    cursor = banco.cursor()
    cursor.execute(f"UPDATE produtos SET descricao='{tela_editar.lineEdit_2.text()}', preco='{tela_editar.lineEdit_3.text()}', categoria='{tela_editar.lineEdit_4.text()}' WHERE id_produto={numero_id}")
    banco.commit()
    tela_editar.close()
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

def fechar_telaprod():
    fprod.close()
    try:
        flistaprod.close()
        tela_editar.close()
    except:
        pass

app = QtWidgets.QApplication([])
fprod = uic.loadUi("produtos.ui")
flistaprod = uic.loadUi("listar_produtos.ui")
tela_editar = uic.loadUi("menu_editar.ui")

fprod.pushButton.clicked.connect(cadastrar_dados)
fprod.pushButton_2.clicked.connect(listar_prod)
fprod.btfechar.clicked.connect(fechar_telaprod)
flistaprod.btexcluir.clicked.connect(excluir_dados)
flistaprod.bteditar.clicked.connect(editar_dados)
flistaprod.btpdf.clicked.connect(gerar_pdf)
flistaprod.btfechar.clicked.connect(flistaprod.close)
tela_editar.btsalvar.clicked.connect(salvar_valor_editado)

fprod.show()
app.exec()