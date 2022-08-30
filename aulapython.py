'''from functools import reduce

lista = [1,2,3,4]
soma = reduce(lambda x, y: x+y, lista, 5)
print (soma)

def foo(value):
    print(f'Olá, esse é o meu parametro: {value}')

foo('LuizaCode')


def ExercicioExtra(meu_dia):
   print(f'Hoje é o meu {meu_dia}')
  
ExercicioExtra ('aniversário!')


def ExercicioExtra(minha_data, meu_dia):
   print(f'Hoje, dia {minha_data} é o meu {meu_dia}!')
  
ExercicioExtra ('30 de agosto','aniversário')'''

valor_energia = float(input("Informe o valor da conta de energia."))
qtd_moradores = input("Quantos moradores:")
qtd_moradores = int(qtd_moradores)
valor_por_morador = valor_energia / qtd_moradores
print((valor_por_morador))

