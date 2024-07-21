
LOOKUP = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}

def to_rna(dna_strand):
    return ''.join(LOOKUP[char] for char in dna_strand)