nome = input("Informe seu nome completo: ")
ano = int(input("Informe o ano do seu nascimento: "))
ano_atual = 2024
ano_final = 0

if ano >= 1922 and ano <= 2024:
  ano_final = ano_atual - ano
  print("Nome: " + nome + " completou ou completará " + str(ano_final) + " anos em " + str(ano_atual))

