# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo
# valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1,
# 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar
# onde, informado um número, ele calcule a sequência de Fibonacci e retorne
# uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(num: int) -> bool:
    x = 0
    y = 1
    fib = []

    for i in range(num):
        # A cada laço, "fib" adiciona "x" (o valor principal) à pilha
        # e em seguida recebe o valor de "y" (o valor depois de "x")
        # e y é somado ao valor antecessor
        fib.append(x)
        x, y = y, y + x

    # Retorna falso se o número não exister na lista "fib"
    if num not in fib:
        return False

    return True


num = 400
print(fibonacci(num))
