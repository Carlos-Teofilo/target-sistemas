# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo
# valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1,
# 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar
# onde, informado um número, ele calcule a sequência de Fibonacci e retorne
# uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(num: int) -> bool:
    x = 0
    y = 1

    for i in range(num):
        if x == num:
            return True
        x, y = y, y + x

    return False


num = 13
print(fibonacci(num))
