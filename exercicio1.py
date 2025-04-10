#Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias multiplicadas por dia, com base em um processo de duplicação diária e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).

lista_dias_crescimento = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

#lista para armazenar as porcentagens
lista_percentual_crescimento = []

#vamos percorrer toda a lista, lembrando de utilizar o len() na range() para percorrer os indices da lista!
for i in range(1, len(lista_dias_crescimento)):
  #aplicação da equação sugerida
  percentual = 100 * (lista_dias_crescimento[i] - lista_dias_crescimento[i-1]) / (lista_dias_crescimento[i-1])
  #adicionando cada resultado na lista das porcentagens
  lista_percentual_crescimento.append(percentual)

#decidi não usar o método round() para não alterar os valores e sim só exibir com duas casas decimais para melhor visualização!
for valor in lista_percentual_crescimento:
    print(f"{valor:.2f}%")
