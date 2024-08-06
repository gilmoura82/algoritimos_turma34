def calcular():
  
  operacao = input('''Por favor informe o tipo de operação matemática que gostaria de fazer:
    1 Soma
    2 Subtração
    3 Multiplicação
    4 Divisão
    ''')
  num1 = int(input('Entre com o 1º número: '))
  num2 = int(input('Entre com o 2º número: '))

  if operacao == "1":
    print('{} + {} = '.format(num1, num2))
    print(num1 + num2)
  elif operacao == "2":
    print('{} - {} = '.format(num1, num2))
    print(num1 - num2)
  elif operacao == "3":
    print('{} * {} = '.format(num1, num2))
    print(num1 * num2)
  elif operacao == "4":
    if num1 or num2 == 0:
      print("Não é possível dividir por 0")
    else:
      print('{} / {} = '.format(num1, num2))
      print(num1 / num2)
  else:
    print("Operação inválida")    

calcular()