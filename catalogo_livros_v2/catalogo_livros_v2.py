import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi

class CatalogoLivrosApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        try:
            loadUi("catalogo_livros_v2.ui", self)
        except FileNotFoundError:
            self.mostrar_mensagem("Erro Crítico", "Arquivo 'catalogo_livros_v2.ui' não encontrado.")
            sys.exit(1)
        except Exception as e:
            self.mostrar_mensagem("Erro Crítico", f"Erro ao carregar UI: {e}")
            sys.exit(1)

        self.configurar_tabela()
        self.conectar_sinais()

    def configurar_tabela(self):
        self.livrosTabela.setColumnCount(5)
        self.livrosTabela.setHorizontalHeaderLabels(['Título', 'Autor', 'Ano', 'Gênero', 'Formato'])
        
        self.livrosTabela.setColumnWidth(0, 150)
        self.livrosTabela.setColumnWidth(1, 100)
        self.livrosTabela.setColumnWidth(3, 80)
        self.livrosTabela.setColumnWidth(4, 70)

    def conectar_sinais(self):
        self.btnAdicionar.clicked.connect(self.adicionar_livro)
        self.btnLimpar.clicked.connect(self.limpar_campos)
        
        self.btnRemover.clicked.connect(self.remover_livro)
        self.btnMostrar.clicked.connect(self.carregar_livros)
        
        self.btnSair.clicked.connect(self.close) 

        try:
            self.btnResumo.clicked.connect(self.mostrar_resumo)
        except AttributeError:
            pass

    def carregar_livros(self):
        pass

    def adicionar_livro(self):
        titulo = self.leTitulo.text().strip()
        autor = self.leAutor.text().strip()
        ano_str = self.leAno.text().strip()
        
        genero = self.cbGen.currentText()
        
        formato = ""
        if self.rbFisico.isChecked():
            formato = "Físico"
        elif self.rbDigital.isChecked():
            formato = "Digital"
        elif self.rbAudiobook.isChecked():
            formato = "Audiobook"
        
        if not titulo or not autor:
            self.mostrar_mensagem("Campo Obrigatório", "Os campos 'Título' e 'Autor' não podem estar vaziais.")
            return
        
        ano = 0
        if ano_str:
            try:
                ano = int(ano_str)
            except ValueError:
                self.mostrar_mensagem("Dado Inválido", "O ano deve ser um número inteiro (Ex: 2024).")
                return

        row_position = self.livrosTabela.rowCount()
        self.livrosTabela.insertRow(row_position)
        
        self.livrosTabela.setItem(row_position, 0, QTableWidgetItem(titulo))
        self.livrosTabela.setItem(row_position, 1, QTableWidgetItem(autor))
        self.livrosTabela.setItem(row_position, 2, QTableWidgetItem(str(ano)))
        self.livrosTabela.setItem(row_position, 3, QTableWidgetItem(genero))
        self.livrosTabela.setItem(row_position, 4, QTableWidgetItem(formato))
        
        self.limpar_campos()

    def limpar_campos(self):
        self.leTitulo.clear()
        self.leAutor.clear()
        self.leAno.clear()
        self.cbGen.setCurrentIndex(0)
        self.rbFisico.setChecked(True) 

    def remover_livro(self):
        linha_selecionada = self.livrosTabela.currentRow()
        
        if linha_selecionada < 0:
            self.mostrar_mensagem("Atenção", "Por favor, selecione um livro na tabela para remover.")
            return

        titulo = self.livrosTabela.item(linha_selecionada, 0).text()

        confirma = QMessageBox.question(self, "Confirmar Remoção",
                                        f"Tem certeza que deseja remover o livro '{titulo}'?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if confirma == QMessageBox.Yes:
            self.livrosTabela.removeRow(linha_selecionada)
            self.mostrar_mensagem("Sucesso", f"Livro '{titulo}' removido.")

    def mostrar_resumo(self):
        contagem_formatos = {
            "Físico": 0,
            "Digital": 0,
            "Audiobook": 0,
            "Não especificado": 0
        }
        
        total_linhas = self.livrosTabela.rowCount()
        
        for row in range(total_linhas):
            item_formato = self.livrosTabela.item(row, 4)
            if item_formato:
                formato = item_formato.text()
                if formato in contagem_formatos:
                    contagem_formatos[formato] += 1
                elif formato.strip() == "":
                    contagem_formatos["Não especificado"] += 1
                else:
                    contagem_formatos[formato] = 1
            else:
                contagem_formatos["Não especificado"] += 1
                
        resumo_texto = "Resumo do Catálogo por Formato:\n\n"
        
        if total_linhas == 0:
            resumo_texto = "Nenhum livro cadastrado no catálogo."
        else:
            for formato, contagem in contagem_formatos.items():
                if contagem > 0:
                    resumo_texto += f"- {formato}: {contagem} livro(s)\n"
        
        resumo_texto += f"\nTotal de livros: {total_linhas}"
        
        self.mostrar_mensagem("Resumo do Catálogo", resumo_texto)

    def mostrar_mensagem(self, titulo, mensagem):
        msg = QMessageBox()
        msg.setWindowTitle(titulo)
        msg.setText(mensagem)
        msg.setIcon(QMessageBox.Information)
        if "Erro" in titulo:
            msg.setIcon(QMessageBox.Critical)
        elif "Atenção" in titulo:
            msg.setIcon(QMessageBox.Warning)
        
        msg.exec_()

    def closeEvent(self, event):
        confirma = QMessageBox.question(self, "Confirmar Saída",
                                        "Tem certeza que deseja sair do catálogo?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if confirma == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

app = QApplication(sys.argv)
window = CatalogoLivrosApp()
window.show()
sys.exit(app.exec_())