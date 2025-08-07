cinconumeros = []
for i in range (5):
    num =input(f"Digite o {i + 1} ° número: ")
    cinconumeros.append(num)

print("\nNúmero digitados:")
for num in cinconumeros:
    print("-",num)
