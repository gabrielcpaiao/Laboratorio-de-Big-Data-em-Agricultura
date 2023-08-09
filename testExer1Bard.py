import sys

def count_nucleotides(sequence):
  """Counts the number of each nucleotide in a DNA sequence.

  Args:
    sequence: The name of a .fasta file.

  Returns:
    A dictionary mapping each nucleotide to the number of times it appears in the sequence.
  """
  with open(sequence, "r") as file:
    sequencea = file.read()

  counts = {}
  for nucleotide in "ACGT":
    counts[nucleotide] = sequencea.count(nucleotide)
  return counts

if __name__ == "__main__":
  sequence = sys.argv[1]
  counts = count_nucleotides(sequence)
  for nucleotide in "ACGT":
    print(nucleotide, counts[nucleotide])


#python count_nucleotides.py sequence.fasta
