"""
Exercicio 1

Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias multiplicadas por dia, com base em um processo de duplicação diária e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).

"""
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

"""
Exercicio 2

Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros, sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.

"""
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

"""
Exercicio 3

Desenvolva um programa que informa a nota de um aluno de acordo com suas respostas. Ele deve pedir a resposta de um aluno para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem alternativas: A, B, C ou D.

Gabarito da Prova:
01 - D
02 - A
03 - C
04 - B
05 - A
06 - D
07 - C
08 - C
09 - A
10 - B

"""

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

"""
Exercício 4

Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram, mostrando os meses por extenso: Janeiro, Fevereiro, etc.

"""
import random

# Lista com os 12 meses
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

temp_media = {}

# Gera temperaturas aleatórias para cada mês
for mes in meses:
    temperatura = round(random.uniform(0, 50), 1)
    temp_media[mes] = temperatura

# Calcula média anual
media_anual = round(sum(temp_media.values()) / len(temp_media), 2)

# Cria dicionário com meses acima da média
meses_acima_media = {mes: temp for mes, temp in temp_media.items() if temp > media_anual}

# Exibe todas as temperaturas
print("📆 Temperaturas médias por mês:")
for mes, temp in temp_media.items():
    print(f"{mes:<10}: {temp}°C")

# Exibe média anual
print(f"\n🌡️ Média anual: {media_anual}°C")

# Exibe apenas os meses com temperatura acima da média
print("\n📈 Meses com temperatura acima da média anual:")
for mes, temp in meses_acima_media.items():
    print(f"{mes:<10}: {temp}°C")

"""
Exercicio 5

Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:

{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

"""

dados_produtos = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

total_vendas = sum(dados_produtos.values())
mais_vendido = max(dados_produtos, key=dados_produtos.get)

print(f'📊 Total de vendas: {total_vendas}')
print(f'🛒 Produto mais vendido: {mais_vendido}')

"""
Exercicio 6

Uma pesquisa de mercado foi feita para decidir qual design de uma marca infantil mais agrada crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:


Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos

Adapte os dados fornecidos a você para uma estrutura de dicionário e a partir dele, informe o design vencedor e a porcentagem de votos recebidos.

"""

# Dicionário com os votos recebidos por cada design
tabela_votos = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811}

# Soma o total de votos de todos os designs
total_votos = sum(tabela_votos.values())

# Cria um novo dicionário com a porcentagem de votos de cada design
# Fórmula: (votos de cada design / total de votos) * 100
porcentagem_votos = {design: (votos / total_votos) * 100 for design, votos in tabela_votos.items()}

# Exibe o design com maior porcentagem de votos usando max()
# A função key=porcentagem_votos.get garante que a comparação será feita pelos valores (porcentagens)
print(f'🏆 Design vencedor: {max(porcentagem_votos, key=porcentagem_votos.get)}')

# Exibe a porcentagem do vencedor com duas casas decimais
print(f'📊 Porcentagem de votos: {max(porcentagem_votos.values()):.2f}%')

# Percorre o dicionário de porcentagens
# Imprime apenas os designs que não são o "Design 5"
for design, porcentagem in porcentagem_votos.items():
    if design != 'Design 5':
        print(f'\nRestante: {design} - {porcentagem:.2f}%')

"""
Exercicio 7

Os funcionários de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do seu salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada funcionário não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos funcionários receberam o abono mínimo e qual o maior valor de abono fornecido.

"""

# Lista com os salários dos funcionários
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]

# Dicionário vazio para armazenar o abono de cada funcionário, com base no salário
abonos = {}

# Percorre cada salário da lista
for salario in salarios:
    # Se 10% do salário for menor que 200, define o abono como R$200 (valor mínimo)
    if salario * 0.1 < 200:
        abonos[salario] = 200
    # Caso contrário, o abono será 10% do salário
    else:
        abonos[salario] = salario * 0.1

# Calcula o total gasto com todos os abonos (soma dos valores do dicionário)
total_abono = sum(abonos.values())

# Conta o número total de funcionários (ou seja, o número de abonos registrados)
qtd_funcionarios = len(abonos)

# Encontra o maior valor de abono pago
maior_abono = max(abonos.values())

# Exibe o total de gastos com abono, formatado com duas casas decimais
print(f'\n💰 Total de gastos com abono: R$ {total_abono:.2f}')

# Exibe o maior valor de abono fornecido
print(f'\n💰 Maior valor de abono fornecido: R$ {maior_abono:.2f}')

# Inicializa o contador de funcionários que receberam o abono mínimo
qtd_abono_minimo = 0

# Percorre os pares (salário, abono) no dicionário
for salario, abono in abonos.items():
    # Se o abono for igual a 200, incrementa o contador
    if abono == 200:
        qtd_abono_minimo += 1

# Exibe quantos funcionários receberam o abono mínimo
print(f'\n👥 Funcionários com abono mínimo: {qtd_abono_minimo}')

"""
Exercicio 8

Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área da floresta e armazenaram essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.

{'Área Norte': [2819, 7236],
 'Área Leste': [1440, 9492],
 'Área Sul': [5969, 7496],
 'Área Oeste': [14446, 49688],
 'Área Centro': [22558, 45148]}

Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica. Dica: use as funções built-in sum() e len().
"""

areas = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}

# Calcula a média diretamente no dicionário
media_especies = {area: sum(valores) / len(valores) for area, valores in areas.items()}

# Encontra a área com maior média usando max com key
diversidade_biologica = max(media_especies, key=media_especies.get)

# Exibe os resultados

for area, media in media_especies.items():
    print(f'\n🏙️ {area}: {media:.2f} espécies')

print(f'\n📊 Área com maior diversidade biológica: {diversidade_biologica}')

"""
Exercicio 9

O setor de RH da sua empresa te pediu uma ajuda para analisar as idades dos funcionários de 4 setores da empresa. Para isso, ele te forneceu os seguintes dados:

{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
Sabendo que cada setor tem 10 funcionários, construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.

"""

# Dicionário contendo listas de idades para cada setor
setor_idades = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
                'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
                'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
                'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

# Calcula a média de idade para cada setor e armazena no dicionário 'media_idade_setor'
media_idade_setor = {setor: sum(idades) / len(idades) for setor, idades in setor_idades.items()}

# Calcula a média geral de idade (soma de todas as idades dividido pelo total de pessoas)
media_idade_geral = sum([sum(idades) for idades in setor_idades.values()]) / sum([len(idades) for idades in setor_idades.values()])

# Conta quantas pessoas estão acima da média geral — esse valor será sobrescrito depois
qtd_acima_media = sum([len([idade for idade in idades if idade > media_idade_geral]) for idades in setor_idades.values()])

# Imprime a média de idade por setor
for setor, media in media_idade_setor.items():
    print(f'\n Média do {setor}: {media:.2f} anos')

# Reinicia o contador de pessoas acima da média para contar de forma mais clara abaixo
qtd_acima_media = 0

# Laço para contar quantas pessoas de todos os setores estão acima da média geral
for setor, idades in setor_idades.items():
    for idade in idades:
        if idade > media_idade_geral:
            qtd_acima_media += 1

# Imprime a média geral de idade
print(f'\n 📊 Média geral: {media_idade_geral:.2f} anos')

# Imprime o número total de pessoas acima da média geral
print(f'\n 👥 Quantidade de pessoas acima da média geral: {qtd_acima_media}')
