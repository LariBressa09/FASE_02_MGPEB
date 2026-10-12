# usando bibliotecas necessárias para conversão de data e de operações matemáticas nas listas
import numpy as np
from datetime import datetime

# Criar a lista de módulos
lista_modulos = [
    "REATORES NUCLEARES/MATRIZ SOLAR",
    "SUPORTE À VIDA",
    "HABITACIONAL BLINDADO",
    "MÉDICO",
    "ESTUFA AGRÍCOLA",
    "MATERIAIS E MINERAÇÃO",
    "LABORATÓRIO CIENTÍFICO",
]

# Criar a lista de datas e horário dos módulos
lista_datas = [
    datetime(2026, 10, 25, 12, 15),
    datetime(2026, 10, 26, 15, 20),
    datetime(2026, 10, 25, 12, 15),
    datetime(2026, 10, 24, 10, 36),
    datetime(2026, 10, 27, 16, 58),
    datetime(2026, 10, 24, 10, 36),
    datetime(2026, 10, 27, 16, 58),
]

# Criar a lista de massas/peso dos módulos
lista_massa = [1500, 3000, 1697, 1598, 2568, 1697, 1500]

# Criar a lista de combustível de cada módulo
lista_combustivel = [6789, 7548, 6984, 7951, 6789, 6984, 7998]

# Criando a lista de índice já setando os valores calculados através da lista de massas e combustíveis
lista_indice = np.array(lista_massa) / np.array(lista_combustivel)

# Primeiro laço de repetição na lista de módulos
for i in range(len(lista_modulos)):
    # Segundo laço de repetição, para conseguirmos comparar sempre um registro com o seguinte registro da lista
    for j in range(len(lista_modulos) - i - 1):
        # Comparação para ver se o índice de massa/combustível é maior que o seguinte para realizar as trocas de posição necessárias nas listas
        if lista_indice[j] > lista_indice[j + 1]:
            lista_datas[j], lista_datas[j + 1] = lista_datas[j + 1], lista_datas[j]
            lista_modulos[j], lista_modulos[j + 1] = lista_modulos[j + 1], lista_modulos[j]
            lista_indice[j], lista_indice[j + 1] = lista_indice[j + 1], lista_indice[j]

# Primeiro laço de repetição na lista de módulos
for i in range(len(lista_modulos)):
    # Segundo laço de repetição, para conseguirmos comparar sempre um registro com o seguinte registro da lista
    for j in range(len(lista_modulos) - i - 1):
        # Comparação para ver se a data e hora é maior que o seguinte para realizar as trocas de posição necessárias nas listas
        if lista_datas[j] > lista_datas[j + 1]:
            lista_datas[j], lista_datas[j + 1] = lista_datas[j + 1], lista_datas[j]
            lista_modulos[j], lista_modulos[j + 1] = lista_modulos[j + 1], lista_modulos[j]
            lista_indice[j], lista_indice[j + 1] = lista_indice[j + 1], lista_indice[j]

print("-" * 50 + "ORDEM DE PRIORIDADE DE POUSO ESTABELECIDA:" + "-" * 50 + "\n")
print("Módulo: MGPEB\n")

for i in range(len(lista_modulos)):
    print(
        f"Módulo: {lista_modulos[i]} \nData e horário: {lista_datas[i]} \nÍndice massa/combustível: {lista_indice[i]:.4f}\n\n"
    )

print("-" * 50 + "INICIANDO FASE DE POUSO" + "-" * 50 + "\n")

print("INICIANDO POUSO DO MÓDULO: MGPEB\n")
#Setando variável de controle se módulo já foi pousado
pousado = False

# enquanto módulo não estiver pousado, repetimos o laço
while not pousado:
    # Valores que seriam determinados por sensores automáticos da nave
    altitude = float(input("DIGITE A ALTITUDE (m): "))
    velocidade = float(input("DIGITE A VELOCIDADE (m/s): "))

    # Código das portas lógicas necessárias para determinar em qual fase de pouso o módulo está disponível
    if (altitude <= 125000 and altitude > 11000) and (velocidade <= 5800 and velocidade > 440):
        print("ATIVAÇÃO DE ESCUDO TÉRMICO\n")
    elif (altitude <= 11000 and altitude > 1800) and (velocidade <= 440 and velocidade > 83):
        print("ACIONAR PARAQUEDAS SUPERSÔNICO\n")
    elif altitude <= 1800 and (velocidade <= 83 and velocidade > 0.75):
        print("ACIONAMENTO DE RETROFOGUETES\n")
    elif velocidade <= 0.75:
        print("ACIONAMENTO DOS AMORTECEDORES E TRENS DE POUSO\n")
        pousado = True
    else:
        print("MÓDULO NÃO DISPONÍVEL PARA INICIAR FASE DE POUSO\n")

print("MÓDULO MGPEB FOI POUSADO COM SUCESSO")
