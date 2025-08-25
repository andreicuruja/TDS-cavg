from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QMessageBox
from cmath import sqrt

def sair(): #FUNCIONA
    result = QMessageBox.question(calc, "Saindo da calculadora", "Deseja mesmo sair da calculadora?", QMessageBox.Yes, QMessageBox.No)
    if result == QMessageBox.Yes:
        calc.close()

def calcular():
    numeroum = calc.lbnum.text()
    numerodois = calc.lbndois.text()
    numeroum= float(numeroum)
    numerodois= float(numerodois)
#CONFERENCIA E AVISO FUNCIONANDO
    if numeroum=="":
        QMessageBox.about(calc,"Primeiro Número:","Nenhum número foi digitado.")
    else:
        numerodois = calc.lbndois.text()

    if numerodois=="":
        QMessageBox.about(calc,"Segundo Número:", "Nenhum segundo número foi digitado.")
    else:

        if calc.rbmais.isChecked():
            resultado = float(numeroum)+float(numerodois)

        elif calc.rbmenos.isChecked():
            resultado= float(numeroum)-float(numerodois)

        elif calc.rbvezes.isChecked():
            resultado= float(numeroum)*float(numerodois)

        elif calc.rbdiv.isChecked():
            resultado= float(numeroum)/float(numerodois)

        elif calc.rbpote.isChecked():
            resultado= float(numeroum)^float(numerodois)

        elif calc.rbraiz.isChecked():
            resultado= (sqrt(numeroum))
    
        else:
            resultado= 'Nenhuma operação selecionada.'
        calc.lbresultado.setText(str(resultado))
# #Limpar
    calc.lbnum.setText("")
    calc.lbndois.setText("")
def limpar():
    calc.lbresultado.clear()
    # result = QMessageBox.question(calc, "Excluir Itens", "Deseja mesmo excluir todos os itens do Resultado?", QMessageBox.Yes, QMessageBox.No)
    # if result == QMessageBox.Yes:
    #     calc.lbresultado(str.clear())
#programa principal
app=QtWidgets.QApplication([])
calc=uic.loadUi("qtcalc.ui")
calc.btsair.clicked.connect(sair)
calc.btcalc.clicked.connect(calcular)
calc.btlimpar.clicked.connect(limpar)
calc.show()
app.exec()