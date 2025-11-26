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

def tela_vendas():
    fvend.show()
    fvend.cbprod.clear()
    cursor = banco.cursor()
    cursor.execute("SELECT descricao FROM produtos")
    for p in cursor.fetchall():
        fvend.cbprod.addItem(str(p[0]))
    fvend.cbclien.clear()
    cursor.execute("SELECT nome FROM clientes")
    for c in cursor.fetchall():
        fvend.cbclien.addItem(str(c[0]))

def calcular_total():
    try:
        quantidade = fvend.quant.value()
        preco = float(fvend.preco.text().replace(",", "."))
        total = quantidade * preco
        fvend.total.setText(f"{total:.2f}")
    except ValueError:
        QMessageBox.warning(fvend, "Erro", "Digite um preço válido!")

def cadastro_vendas():
    try:
        prod_nome = fvend.cbprod.currentText()
        cli_nome = fvend.cbclien.currentText()
        quant = fvend.quant.value()
        preco = fvend.preco.text().replace(",", ".")
        
        if not prod_nome or not cli_nome:
            return QMessageBox.warning(fvend, "Atenção", "Selecione Produto e Cliente!")

        cursor = banco.cursor()
        cursor.execute("SELECT id_produto FROM produtos WHERE descricao=%s", (prod_nome,))
        id_prod = cursor.fetchall()[0][0]
        
        cursor.execute("SELECT id_cliente FROM clientes WHERE nome=%s", (cli_nome,))
        id_cli = cursor.fetchall()[0][0]
        
        sql = "INSERT INTO vendas (id_produto, id_cliente, quantidade, valor_unit) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (id_prod, id_cli, quant, preco))
        banco.commit()
        
        QMessageBox.information(fvend, "Sucesso", "Venda registrada!")
        fvend.quant.setValue(0)
        fvend.preco.clear()
        fvend.total.clear()
    except Exception as e:
        QMessageBox.warning(fvend, "Erro Crítico", f"Erro ao gravar: {e}")

def gerar_relatorio_vendas():
    try:
        cursor = banco.cursor()
        sql = """
        SELECT vendas.id_vendas, clientes.nome, produtos.descricao, vendas.valor_unit, vendas.quantidade
        FROM vendas 
        INNER JOIN clientes ON vendas.id_cliente = clientes.id_cliente 
        INNER JOIN produtos ON vendas.id_produto = produtos.id_produto
        """
        cursor.execute(sql)
        dados = cursor.fetchall()
        
        if not dados:
            return QMessageBox.information(fvend, "Aviso", "Nenhuma venda encontrada.")

        pdf = canvas.Canvas("Controle_de_Vendas.pdf")
        pdf.setFont("Times-Bold", 25)
        pdf.drawString(200, 800, "Relatório de Vendas")
        pdf.setFont("Times-Bold", 12)
        pdf.drawString(10, 750, "ID")
        pdf.drawString(50, 750, "PRODUTO")
        pdf.drawString(200, 750, "CLIENTE")
        pdf.drawString(350, 750, "QTD")
        pdf.drawString(400, 750, "UNITÁRIO")
        pdf.drawString(500, 750, "TOTAL")
        
        y = 750
        pdf.setFont("Times-Roman", 10)
        for linha in dados:
            y -= 30
            if y < 50:
                pdf.showPage()
                y = 800
            id_v, cli, prod, val, qtd = linha
            total_item = val * qtd
            pdf.drawString(10, y, str(id_v))
            pdf.drawString(50, y, str(prod)[:25])
            pdf.drawString(200, y, str(cli)[:25])
            pdf.drawString(350, y, str(qtd))
            pdf.drawString(400, y, f"R$ {val:.2f}")
            pdf.drawString(500, y, f"R$ {total_item:.2f}")
            
        pdf.save()
        QMessageBox.information(fvend, "PDF", "Relatório gerado com sucesso!")
    except PermissionError:
        QMessageBox.warning(fvend, "Erro", "Feche o arquivo PDF aberto!")
    except Exception as e:
        QMessageBox.warning(fvend, "Erro", f"Erro ao gerar PDF: {e}")

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
    feditar.show(); feditar.lineEdit.setText(str(prod[0])); feditar.lineEdit_2.setText(str(prod[1])); feditar.lineEdit_3.setText(str(prod[2])); feditar.lineEdit_4.setText(str(prod[3]))

def salvar_edit_prod():
    cursor = banco.cursor(); cursor.execute(f"UPDATE produtos SET descricao='{feditar.lineEdit_2.text()}', preco='{feditar.lineEdit_3.text()}', categoria='{feditar.lineEdit_4.text()}' WHERE id_produto={numero_id}")
    banco.commit(); feditar.close(); flistaprod.close(); listar_prod()

def gerar_pdf_prod():
    cursor = banco.cursor(); cursor.execute("SELECT * FROM produtos"); dados = cursor.fetchall()
    pdf = canvas.Canvas("cadastro_produtos.pdf"); pdf.setFont("Times-Bold", 25); pdf.drawString(200, 800, "Produtos"); y = 750
    for d in dados: y -= 50; pdf.drawString(10, y, f"{d[0]} | {d[1]} | {d[2]} | {d[3]}")
    pdf.save(); QMessageBox.information(flistaprod, "PDF", "Gerado!")

def cadastro_user():
    if fuser.le_senha.text() == fuser.le_senha2.text():
        cursor = banco.cursor(); cursor.execute("INSERT INTO usuarios (senha, usuario) VALUES (%s, %s)", (fuser.le_senha.text(), fuser.le_usuario.text()))
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
    fvend = uic.loadUi("vendas.ui")
except Exception as e:
    print("ERRO AO CARREGAR UI:", e)
    sys.exit()

flogin.bt_login.clicked.connect(logar)
flogin.bt_cadastrar.clicked.connect(tela_user)
fmenu.bt_prod.clicked.connect(tela_prod)
fmenu.bt_usuar.clicked.connect(tela_user)
fmenu.bt_clien.clicked.connect(tela_cli)
fmenu.bt_vendas.clicked.connect(tela_vendas)
fmenu.btfechar.clicked.connect(app.quit)
fprod.pushButton.clicked.connect(cadastrar_prod)
fprod.pushButton_2.clicked.connect(listar_prod)
fprod.btfechar.clicked.connect(fechar_telaprod)
flistaprod.btexcluir.clicked.connect(excluir_prod)
flistaprod.bteditar.clicked.connect(editar_prod)
flistaprod.btpdf.clicked.connect(gerar_pdf_prod)
flistaprod.btfechar.clicked.connect(flistaprod.close)
feditar.btsalvar.clicked.connect(salvar_edit_prod)
fuser.bt_salvar.clicked.connect(cadastro_user); fuser.bt_fechar.clicked.connect(fuser.close)
fcli.btcadastrar.clicked.connect(cadastro_clientes); fcli.btlistar.clicked.connect(listar_clientes)
fcli.btfechar.clicked.connect(fcli.close); fcli.cbest.currentIndexChanged.connect(mostra_cidades)
fvend.btcadastrar.clicked.connect(cadastro_vendas)
fvend.btlistar.clicked.connect(gerar_relatorio_vendas)
fvend.btfechar.clicked.connect(fvend.close)
fvend.bt_calc.clicked.connect(calcular_total)

flogin.show()
app.exec()