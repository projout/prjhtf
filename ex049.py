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