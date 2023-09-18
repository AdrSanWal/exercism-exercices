def to_rna(dna_strand):
    x, y = 'GCTA', 'CGAU'
    dna_rna = str.maketrans(x, y)
    return dna_strand.translate(dna_rna)
