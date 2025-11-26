from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="sistema"
)

def cadastrar_dados():

    vprod = fprod.lineEdit_2.text()
    vpreco = fprod.lineEdit_3.text()

    vcat = ""
    if fprod.radioButton_1.isChecked() :
        vcat ="Alimentos"
    elif fprod.radioButton_2.isChecked() :
        vcat ="Eletrônicos"
    else:
        vcat ="Informática"

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (descricao,preco,categoria) VALUES (%s,%s,%s)"
    dados = (str(vprod),str(vpreco),vcat)
    cursor.execute(comando_SQL,dados)
    banco.commit() 

    fprod.lineEdit_2.setText("")
    fprod.lineEdit_3.setText("")

def fechar_telaprod():

    result = QMessageBox.question(fprod, "Saindo do sistema", "Deseja mesmo sair do sistema?", QMessageBox.Yes, QMessageBox.No)
    if result == QMessageBox.Yes:
        fprod.close()

def listar_prod():

    flistaprod.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()


    flistaprod.tb_listaprod.setRowCount(len(dados_lidos))
    flistaprod.tb_listaprod.setColumnCount(4) 

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            flistaprod.tb_listaprod.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app=QtWidgets.QApplication([])


fprod=uic.loadUi("produtos.ui")
flistaprod=uic.loadUi("produtoslistar.ui")

fprod.pushButton.clicked.connect(cadastrar_dados)
fprod.pushButton_2.clicked.connect(listar_prod)
fprod.btfechar.clicked.connect(fechar_telaprod)

fprod.show()
app.exec()