# lista_de_listas_de_inteiros = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
#     [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
#     [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
#     [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
#     [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
#     [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
#     [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
#     [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
#     [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
#     [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
#     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
# ]

# def conferir_valores(lista_de_inteiros):
#     lista_checada = set()
#     valores_duplicados = -1
#     for numero in lista_de_inteiros:
#         if numero in lista_checada:
#             valores_duplicados = numero
#             break
#         lista_checada.add(numero)
#     return valores_duplicados
# # for lista in lista_de_listas_de_inteiros:
# #     print(lista,conferir_valores(lista))
# print(set(range(10)))
from itertools import groupby
alunos  = [
    { 'nome' : 'Luiz' , 'nota' : 'A' },
    { 'nome' : 'Letícia' , 'nota' : 'B' },
    { 'nome' : 'Fabrício' , 'nota' : 'A' },
    { 'nome' : 'Alecrim' , 'nota' : 'C' },
    { 'nome' : 'Joana' , 'nota' : 'D' },
    { 'nome' : 'João' , 'nota' : 'A' },
    { 'nome' : 'Eduardo' , 'nota' : 'B' },
    { 'nome' : 'André' , 'nota' : 'A' },
    { 'nome' : 'Anderson' , 'nota' : 'C' },
]
def aluno_nota(aluno):
    return aluno ['nota']
alunos_ord = sorted(alunos,key = aluno_nota)
grupos = groupby(alunos_ord, key= aluno_nota)
for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)