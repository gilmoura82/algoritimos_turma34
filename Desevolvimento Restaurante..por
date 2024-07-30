programa {
  funcao inicio() {

      inteiro opcao
    
      escreva("Escolha uma opção: O cliente fumante? digite 1: " + "\n" + "O cliente trouxe algum pet? digite 2: " + "\n" + "O cliente trouxe 5 pessoas ou mais? digite 3: ")
      leia(opcao)

      escolha(opcao) {
        caso 1: 
        escreva("Clientes fumantes devem ser alocados na área externa do restaurante")
        pare
        caso 2:
        escreva("Clientes com animais devem ser alocados na área externa do restaurante")
        pare
        caso 3:
        escreva("Grupo de 5 ou mais pessoas deve ser alocados no 1º andar")
        pare
        caso contrario:
        escreva("Cliente pode ser alocado no térreo")
        pare
      }
      
  }
}
