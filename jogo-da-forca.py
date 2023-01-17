# Jogo da forca

secreto = 'casa'  #preencha este campo com a palavra secreta para começar.
digitadas = []
chances = 5

while True:
    if chances <= 0:
        print('Você perdeu!!')
        repetir = input('Deseja repetir? digite [s] ou [n]: ')
        if repetir == 'n':
            print('Obrigado por jogar!')
            break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhuuul, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Vish, a letra "{letra}" não existe na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'


    if secreto_temporario == secreto:
        print('Parabéns, você ganhou!!!')
        print(f'A palavra era {secreto_temporario.upper()}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario.upper()}.')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()