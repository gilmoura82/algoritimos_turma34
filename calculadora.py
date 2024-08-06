def calcular():
  
  operacao = input('''Por favor informe o tipo de operação matemática que gostaria de fazer:
    + Soma
    - Subtração
    * Multiplicação
    / Divisão
    ''')
  num1 = int(input('Entre com o 1º número: '))
  num2 = int(input('Entre com o 2º número: '))

  if operacao == "+":
    print('{} + {} = '.format(num1, num2))
    print(num1 + num2)
  elif operacao == "-":
    print('{} - {} = '.format(num1, num2))
    print(num1 - num2)
  elif operacao == "*":
    print('{} * {} = '.format(num1, num2))
    print(num1 * num2)
  elif operacao == "/":
    print('{} / {} = '.format(num1, num2))
    print(num1 / num2)
  else:
    print("Operação inválida")    

calcular()