#lista-de-exercicios-3.py - unid 9-erros_e_excecoes

## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?

# def calcular_media(valores):
#     tamanho = 1
#     soma = 0.0
#     for i, valor in enumerate(valores):
#         soma += valor
#         i += 1
#     media = soma / tamanho

# continuar = True
# valores = []
# while continuar:
#     valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
#     if valor.lower() == 'ok':
#         continuar = false

# media = calcular_media(valores)
# print('A média calculada para os valores {} foi de {}'.format(valores, media))


def calcular_media(valores):
    tamanho = 0 #precisa começar com zero, para não dar erro na conta no final
    soma = 0.0
    for valor in valores: #modifivar para volor in valores
        soma += valor
        tamanho += 1 #definir que o meu tamanho é o total de itens que coloco na lista
    media = soma / tamanho
    return media #colocar return da média

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar = False #erro de escrita >>> False e não false
    else:
        valores.append(float (valor))

media = calcular_media(valores)

print('A média calculada para os valores {} foi de {}'.format(valores, media))
