#!/usr/bin/env python3

# Codon table for DNA to protein conversion
CODON_TABLE = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'-', 'TAG':'-', 'TGC':'C', 'TGT':'C', 'TGA':'-', 'TGG':'W'
}

def amino_acid_lookup(codon: str) -> str:
    """ Return amino acid for a codon
    """
    return CODON_TABLE.get(codon)

def dna_to_protein(dna: str, frame: int = 0) -> str:
    """ Translate DNA sequence into protein sequence
    """
    protein_seq = ""
    dna_seq = dna[frame:]    
    for i in range(0, len(dna_seq) - 2, 3):  # Iterate over the DNA sequence in steps of 3 to get codons
        codon = dna_seq[i:i+3] 
        amino_acid = amino_acid_lookup(codon)
        protein_seq += amino_acid
        if amino_acid == '-':
            return protein_seq    
    return protein_seq

dna_seq = "ATGGTAATGGGCCGCTGAAAGGGTGC"
reading_frame = 0
protein_seq = dna_to_protein(dna_seq, reading_frame)
print(f"DNA sequence: {dna_seq}")
print(f"Protein sequence for reading frame {reading_frame}: {protein_seq}")