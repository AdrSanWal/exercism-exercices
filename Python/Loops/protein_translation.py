codons = {
    'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
    'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine',
    'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
    'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan', 'UAA': 0,
    'UAG': 0, 'UGA': 0
}


def proteins(strand, codon=True):
    protein = []
    while strand and (codon := codons[strand[:3]]):
        protein.append(codon)
        strand = strand[3:]
    return protein
