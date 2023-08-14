def count_bases(sequence):
    counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    
    for base in sequence:
        if base in counts:
            counts[base] += 1
    
    return counts

# Ler o arquivo sequence.fasta
filename = 'sequence.fasta'
with open(filename, 'r') as fasta_file:
    lines = fasta_file.readlines()

# Extrair a sequência do arquivo .fasta (remover cabeçalho se existir)
sequence = ''.join(line.strip() for line in lines[1:])

# Contar as bases
base_counts = count_bases(sequence)

# Imprimir os resultados
print(f"Quantidade de A: {base_counts['A']}")
print(f"Quantidade de C: {base_counts['C']}")
print(f"Quantidade de T: {base_counts['T']}")
print(f"Quantidade de G: {base_counts['G']}")

print()
totalBases = base_counts['A'] + base_counts['C'] + base_counts['T'] + base_counts['G']
print(f"Soma de A + C + T + G: {totalBases}")

print()
#Percentual médio
print(f"Percentual médio 'A': {base_counts['A']/(totalBases):.2f}")
print(f"Percentual médio 'C': {base_counts['C']/(totalBases):.2f}")
print(f"Percentual médio 'T': {base_counts['T']/(totalBases):.2f}")
print(f"Percentual médio 'G': {base_counts['G']/(totalBases):.2f}")