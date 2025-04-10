# Exercicio 1

#Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias multiplicadas por dia, com base em um processo de duplicação diária e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).

lista_dias_crescimento = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

# Lista para armazenar as porcentagens
lista_percentual_crescimento = []

# Vamos percorrer toda a lista, lembrando de utilizar o len() na range() para percorrer os indices da lista!
for i in range(1, len(lista_dias_crescimento)):
  # Aplicação da equação sugerida.
  percentual = 100 * (lista_dias_crescimento[i] - lista_dias_crescimento[i-1]) / (lista_dias_crescimento[i-1])
  # Adicionando cada resultado na lista das porcentagens
  lista_percentual_crescimento.append(percentual)

# Decidi não usar o método round() para não alterar os valores e sim só exibir com duas casas decimais para melhor visualização!
for valor in lista_percentual_crescimento:
    print(f"{valor:.2f}%")
  
# Exercicio 2

#Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros, sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.

import random

itens_id = []

# Percorre uma range de até 10 números
for i in range(10):
  # Adiciona à lista números randômicos de 1 à 100
  itens_id.append(random.randint(0,100))

print(itens_id)

# Verificação dos itens que são par
qtd_doces = len([qtd for qtd in itens_id if qtd % 2 == 0])
# Verificação dos itens que não são par
qtd_amargos = len([qtd for qtd in itens_id if qtd % 2 != 0])

print(f'Quantidade de itens doces: {qtd_doces}')
print(f'Quantidade de itens amargos: {qtd_amargos}')

# Exercicio 3
# Dicionário com o gabarito oficial da prova: chave é o número da questão, valor é a resposta correta
gabarito = {1:'D', 2:'A', 3:'C', 4:'B', 5:'A', 6:'D', 7:'C', 8:'C', 9:'A', 10:'B'}

# Dicionário vazio onde vamos armazenar as respostas do usuário
respostas = {}

# Loop de 1 a 10 (inclusive), representando as 10 questões da prova
for i in range(1,11):
  # Solicita a resposta do usuário para a questão i e converte para maiúscula
  resposta = input(f'Digite a resposta da questão {i}: ').upper()
  
  # Enquanto a resposta não for uma letra válida (A, B, C ou D), pede novamente
  while resposta not in ['A','B','C','D']:
    resposta = input(f'Resposta inválida. Digite a resposta da questão {i}: ').upper()
  
  # Adiciona a resposta válida no dicionário de respostas, com a chave sendo o número da questão
  respostas[i] = resposta

# Mostra todas as respostas digitadas pelo usuário
print(respostas)

# Lista por compreensão: expressão -> percorre as chaves (questões) -> conta quantas respostas estão corretas
qtd_acertos = len([qtd for qtd in respostas if respostas[qtd] == gabarito[qtd]])

# Mesma lógica acima, mas contando as respostas erradas
qtd_erros = len([qtd for qtd in respostas if respostas[qtd] != gabarito[qtd]])

# Exibe a quantidade de acertos e erros do usuário
print(f'Quantidade de acertos: {qtd_acertos}')
print(f'Quantidade de erros: {qtd_erros}')
