# Desafio 49 — Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, entretanto, agora
# um laço for.
try:
    num = int(input("Informe um número: "))

    print("*-" * 10)
    for i in range(0,11):
        print("{0} * {1} = {2}".format(i, num, i * num))
    print("*-" * 10)
except Exception as e:
    print(f'Não foi possível executar o programa pelo seguinte erro: {e}')
finally:
    print("Hello World!")
#--------------------------------------------------------------------------------------------#
# Desafio 63 — Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
# de uma Sequência de Fibonacci
#   Ex: 0 —> 1 —> 1 —> 2 —> 3 —> 5 —> 8
while True:
    try:
        n = int(input("informe um número N para ver os N primeiros termos da Sequência de Fibonacci: "))
        if n <= 0:
            raise ValueError
        a, b = 0, 1
        if n == 1:
            print(f"Sequencia de Fibonacci com {n} termos:")
            print(a)
        else:
            print(f"Sequencia de Fibonacci com {n} termos:")
            print(f"{a} -> {b}", end=" -> ")
            for i in range(2, n):
                c = a + b
                print(c, end=" -> ")
                a, b = b, c
        break
    except ValueError:
        print("Informe um número inteiro positivo.")