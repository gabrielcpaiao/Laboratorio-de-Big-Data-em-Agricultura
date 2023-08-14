# encoding:utf-8

def ler_fasta(arquivo):
    sequencia = ''
    lista = []
    with open(arquivo, 'r') as fasta:
            sequencia = ''
            for linha in fasta:
                if not linha.startswith('>'):
                    sequencia += linha
            lista.append(sequencia)

    return lista

# testando...
lista = ler_fasta("sequence.fasta")

#print(lista)

bases = {'A': 0, 'C': 0, 'T': 0, 'G': 0}

for i in range (len(lista)):
    for j in range (len(lista[i])):
        if lista[i][j] == 'A':
            bases['A'] += 1
        elif lista[i][j] == 'C':
            bases['C'] += 1
        elif lista[i][j] == 'T':
            bases['T'] += 1
        elif lista[i][j] == 'G':
            bases['G'] += 1

print(bases)


print()
totalBases = bases['A'] + bases['C'] + bases['T'] + bases['G']
print(f"Soma de A + C + T + G: {totalBases}")

print()
#Percentual médio
print(f"Percentual médio 'A': {bases['A']/(totalBases):.2f}")
print(f"Percentual médio 'C': {bases['C']/(totalBases):.2f}")
print(f"Percentual médio 'T': {bases['T']/(totalBases):.2f}")
print(f"Percentual médio 'G': {bases['G']/(totalBases):.2f}")