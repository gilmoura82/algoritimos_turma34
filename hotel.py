# for usando range
for andares_hotel in range (20, 0):

  if andares_hotel == 13:
    continue

  print(f'Andar Nº {andares_hotel}')

# For dentro da lista
andares_hotel = [1,"2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]

for num in andares_hotel[:]:
  if num == "13": 
    andares_hotel.remove(num)
  else:
    print(num)

#Desafio para mostrar a lista decrescente, removendo o item 13
  for andares_hotel in range (20, 0, -1):    
    
    if andares_hotel == 13:
      continue

  print(f'Andar Nº {andares_hotel}')
  

  

