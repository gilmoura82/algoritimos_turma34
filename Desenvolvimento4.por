programa {
  funcao inicio() {

    // Declaração das variáveis
    cadeia nome
    cadeia endereco
    cadeia cidade
    cadeia cpf
    cadeia rg

    // Solicitação de entrada de dados ao usuário
    escreva("Informe seu nome: ")
    leia(nome)
    escreva("Informe seu endereço: ")
    leia(endereco)
    escreva("Informe sua cidade: ")
    leia(cidade)
    escreva("Informe seu CPF: ")
    leia(cpf)
    escreva("Informe seu RG: ")
    leia(rg)

    // Exibição dos dados informados pelo usuário
    escreva("\nDados informados:\n")
    escreva("Nome: ", nome, "\n")
    escreva("Endereço: ", endereco, "\n")
    escreva("Cidade: ", cidade, "\n")
    escreva("CPF: ", cpf, "\n")
    escreva("RG: ", rg)
  }
}
