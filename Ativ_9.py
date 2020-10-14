i = 0
soma_idade = 0
while i < quantidade: 
    idade = int(input("Informe a idade: "))
    soma_idade = soma_idade + idade
    i += 1
media_idade = soma_idade / quantidade
print("Média das idades é: ", media_idade)

if 0 <= media_idade <= 25:
    print('Turma jovem')

if 26 <= media_idade < 60:
    print('Turma adulta')

if media_idade >= 60:
    print('Turma idosa')
