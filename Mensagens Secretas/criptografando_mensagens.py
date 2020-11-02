alfabeto = 'abcdefghijklmnopqrstuvwxyz'

chave = 3

letra = input('Por favor, entre com uma letra para criptografar: ')

posicao = alfabeto.find(letra)

nova_posicao = (posicao + chave) % 26

letra_criptografada = alfabeto[nova_posicao]

print('Sua letra criptografada é', letra_criptografada)