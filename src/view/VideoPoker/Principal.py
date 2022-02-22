from Funcoes import Mesa, fichas

pessoa = input('digite seu nome: ')
pessoa = fichas(nome=pessoa)

print(f'Olá {pessoa.nome} você possui: {pessoa.fichas} Fichas')

print('Digite quantas fichas você deseja apostar')
a = int(input(': '))

if a <= 100:
    print('limite minimo é de 100 fichas')

pessoa.apostas(quantidade=a)
pessoa.listar_combos()
print('\n Que os Jogos Comecem\n')


mesa, cartas = Mesa()

for lista in cartas:
    for c in lista:
        print('\t', c, end='\t')
    print()
print('\t    [1]    \t\t    [2]    \t\t    [3]    \t\t    [4]    \t\t    [5]   ')
e = input('Quais cartas irão ficar: ')

mesa, cartas = Mesa(mesa, e.split(' '))

for lista in cartas:
    for c in lista:
        print('\t', c, end='\t')
    print()
