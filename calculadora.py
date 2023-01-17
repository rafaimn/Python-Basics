
print('Bem vindo à Calculex!')

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')


    if not num_1.isnumeric() and not num_2.isnumeric():
        print('Você precisa digitar um número: ')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador inválido.')

    if num_1 and num_2 % 2 == 0:
        print(f"O número é par.")
    else:
        print(f"O número é impar.")

    sair = input('Deseja sair? digite [s] ou [n]: ')
    if sair == 's':
            print('Obrigado por utilizar a Calculex!')
            break