programa {
  funcao inicio() {

    // Declara��o das vari�veis
    cadeia nome
    cadeia endereco
    cadeia cidade
    cadeia cpf
    cadeia rg

    // Solicita��o de entrada de dados ao usu�rio
    escreva("Informe seu nome: ")
    leia(nome)
    escreva("Informe seu endere�o: ")
    leia(endereco)
    escreva("Informe sua cidade: ")
    leia(cidade)
    escreva("Informe seu CPF: ")
    leia(cpf)
    escreva("Informe seu RG: ")
    leia(rg)

    // Exibi��o dos dados informados pelo usu�rio
    escreva("\nDados informados:\n")
    escreva("Nome: ", nome, "\n")
    escreva("Endere�o: ", endereco, "\n")
    escreva("Cidade: ", cidade, "\n")
    escreva("CPF: ", cpf, "\n")
    escreva("RG: ", rg)
  }
}
