num = int(input("Digite o número referente ao dia da semana de hoje:  "))
match num: 
    case 1: print("Domingo")
    case 2: print("Segunda-feira")
    case 3: print("Terça-feira")
    case 4: print("Quarta-feira")
    case 5: print("Quinta-feira")
    case 6: print("Sexta-feira")
    case 7: print("Sábado")
    case _: print("Número inválido. Por favor, digite um número entre 1 e 7.")           

# 2) Construa um algoritmo que solicite um mês do ano (01 a 12) e, de acordo com as condições abaixo, dizer : 01 (Férias), 
# 02 a 06 (1º semestre letivo), 07 (Recesso), 08 a 11 (2º semestre letivo), 12 (Férias)

mes = int(input("Digite um número referente a um mês do ano: "))
match mes:
    case 1:
        print("Férias")
    case mes if mes in range(2, 7):  
        print("1º semestre letivo")
    case 7:
        print("Recesso")
    case mes if mes in range(8, 12):  
        print("2º semestre letivo")
    case 12:
         print("Férias") 


# 3) Escreva um algoritmo que leia o código de um determinado produto e mostre a sua classificação. Utilize a seguinte tabela como referência:
# Código Classificação
# 1 Alimento não perecível
# 2, 3 ou 4 Alimento perecível
# 5 ou 6 Vestuário
# 7 Higiene pessoal
# 8 até 15 Limpeza e utensílios domésticos
# Qualquer outro código Inválido

cod=(int(input("Digite o código do produto: ")))
match cod:
    case 1:
        print("Alimento não perecível")
    case cod if cod in range(2, 5):
        print("Alimento perecível")
    case cod if cod in range(5, 7):
         print("Vestuário")
    case 7:
        print("Higiene pessoal")    
    case cod if cod in range(8, 16):
        print("Limpeza e utensílios domésticos")
    case _:
      print("Código inválido, digite novamente.") 

# 4) Elabore um algoritmo que, dada a idade de um nadador, classifique-o em uma das seguintes categorias.
# Idade Categoria
# 5 até 7 anos Infantil A
# 8 até 10 anos Infantil B
# 11 até 13 anos Juvenil A
# 14 até 17 anos Juvenil B
# Maior de 18 anos Adulto

id=(int(input("Digite o numero equivalente à sua idade: ")))
match id:
    case id if id in range(5, 8):
      print("Categoria Infantil A")
    case id if id in range(8, 10):
      print("Categoria Infantil B")
    case id if id in range(11, 14):
      print("Categoria Juvenil A")
    case id if id in range(14, 18):
      print("Categoria Juvenil B")
    case id if id >= 18:
     print("Categoria Adulta")
    case _:
     print("Idade inválida, digite novamente.")   

# 5) O programa de uma loja de móveis mostra o seguinte menu na tela de vendas:
# 1-Venda a Vista
# 2-Venda a Prazo 30 dias
# 3-Venda a Prazo 60 dias
# 4-Venda a Prazo com 90 dias
# 5-Venda com cartão de débito
# 6-Venda com cartão de crédito

# Escolha a opção
# Faça um programa que receba o valor da venda, escolha a condição de pagamento
# no menu e mostre o total da venda final conforme condições a seguir:
# Venda a Vista - desconto de 10%
# Venda a Prazo 30 dias - desconto de 5%
# Venda a Prazo 60 dias - mesmo preço
# Venda a Prazo 90 dias - acréscimo de 5%
# Venda com cartão de débito - desconto de 8%
# Venda com cartão de crédito - desconto de 7%

print("Aceitamos as formas de pagamento: ")
import pprint
print("Opção 1 - Venda à vista.") 
print("Opção 2 - Venda a prazo 30 dias.")
print("Opção 3 - Venda a prazo 60 dias.") 
print("Opção 4 - Venda a prazo 90 dias.")
print("Opção 5 - Venda com cartão de débito.")
print("Opção 6 - Venda com cartão de crédito.")

valor=(float(input("Insira o valor da venda: ")))


pay=(int(input("Escolha a opção (1 à 6) de pagamento desejado: ")))

# avista = 1
# p30 = 2
# p60 = 3
# p90 = 4
# debito = 5
# credito = 6

match pay: 
    case 1:
        print(f"Valor da venda: R$ {valor}")
        print(f"Desconto de 10%: R$ {valor * 0.10}")
        print(f"Valor final à vista: R$ {valor * 0.90}")
    case 2:
        print(f"Valor da venda: R$ {valor}")
        print(f"Desconto de 5%: R$ {valor * 0.05}")
        print(f"Valor final a prazo 30 dias: R$ {valor * 0.05}")
    case 3:
        print(f"Valor da venda: R$ {valor}")
        print(f"Valor final a prazo 60 dias: R$ {valor}")
    case 4:
        print(f"Valor da venda: R$ {valor}")
        print(f"Acréscimo de 5%: R$ {valor * 1.05}")
        print(f"Valor final a prazo 90 dias: R$ {valor * 1.05}")
    case 5:
        print(f"Valor da venda: R$ {valor}")
        print(f"Desconto de 8%: R$ {valor * 0.08}")
        print(f"Valor final com cartão de débito: R$ {valor * 0.92}")
    case 6:
        print(f"Valor da venda: R$ {valor}")
        print(f"Desconto de 7%: R$ {valor * 0.07}")
        print(f"Valor final com cartão de crédito: R$ {valor * 0.93}")
    case _:
        print("Opção inválida, tente novamente.")





