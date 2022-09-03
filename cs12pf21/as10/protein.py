"""
Several function regarding proteins and protein synthesis.
"""

__author__ = 'Karen Corscadden a Cabrillo student for CS 12P, kmcorscadden@jeff.cis.cabrillo.edu'

import re


def _load_data():
    """
    Loads data from files. For internal use only, i.e. "private".
    You don't *have* to structure things this way, but it's a recommendation.
    """
    dict_amino = {line.split()[0]: line.split()[2] for line in open('/srv/datasets/amino')}
    dict_mass = {line.split()[0]: float(line.split()[1])
                    for line in open('/srv/datasets/amino-monoisotopic-mass')}
    return dict_amino, dict_mass


_to_amino, _mass = _load_data()  # Use our "private" function to load required file data.


def to_amino(rna_codon):
    """
    Returns either the amino acid letter encoded by the given RNA codon.
    e.g. to_amino('AUG') == 'M' and to_amino('UGA') == 'O' and to_amino('ABC') is None

    :param rna_codon: a string potentially containing a RNA codon
    :return either the letter representing the amino acid encoded by rna_codon, 'O' if rna_codon
    is a stop codon, or None if rna_codon is not a valid RNA codon.
    """
    rna_codon = rna_codon.replace('U', 'T')

    try:
        return _to_amino[rna_codon]
    except KeyError:
        return None


def translate(rna):
    """
    Generates a sequence of letters representing amino acids encoded by a given RNA sequence.
    Encountering a stop codon or the end of the sequence will stop the process.
    e.g. translate('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA') == 'MAMAPRTEINSTRING'
    Inspired by Rosalind PROT: http://rosalind.info/problems/prot/

    :param rna: a RNA string, assumed to consist of 'ACGU' characters
    :yield: single-character strings representing the amino acids in the protein
    :raise: ValueError if no stop codon is found
    """
    for i in range(0, len(rna) - 2, 3):
        amino = to_amino(rna[i:i + 3])
        if amino == 'O':
            return
        else:
            yield amino

    raise ValueError


def mass(protein):
    """
    Computes and returns the mass of a protein, in daltons.
    e.g. abs(mass('SKADYEK') - 821.392) < .001
    Uses the monoisotopic masses in file /srv/datasets/amino-monoisotopic-mass.
    See Rosalind PRTM: http://rosalind.info/problems/mass/

    :param protein: A sequence of single-character strings representing amino acids
    :return the sum of the monoisotopic masses of all amino acids in protein
    """
    total_mass = 0

    for amino in protein:
        total_mass += _mass[amino]

    return total_mass


def potential_proteins(dna):
    """
    Generates a sequence of potential proteins encoded by a given DNA coding strand, in the order
    encountered in the DNA. A potential protein shall have the following characteristics:
    - Its first amino acid is methoionine ('M'), encoded by RNA codon 'AUG'.
    - It is terminated by any of the three stop codons.
    - Its length is at least 11 amino acids.
    (The shortest known protein is length 11: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3864261/)
    Inspired by Rosalind ORF: http://rosalind.info/problems/orf/
    Potential proteins may overlap, e.g.:
    list(potential_proteins('ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA')) == [
      'MAMAPRTEINSTRING', 'MAPRTEINSTRING'
    ]

    :param dna: a DNA coding strand, assumed to be a string consisting of 'ACGT' characters
    :yield: strings of amino-acid characters representing each potential protein in dna
    """
    for x in (m.start() for m in re.finditer(r'ATG|AUG', dna)):
        try:
            translation = ''.join(translate(dna[x:]))
            if len(translation) >= 11:
                assert translation[0] == 'M'
                yield translation
        except ValueError:
            continue


if __name__ == '__main__':
    import inspect  # for some assertions below
    assert to_amino('AUG') == 'M' and to_amino('UGA') == 'O' and to_amino('ABC') is None
    assert abs(mass('SKADYEK') - 821.392) < .001
    assert inspect.isgeneratorfunction(translate)
    assert ''.join(
        translate('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')) == 'MAMAPRTEINSTRING'
    assert inspect.isgeneratorfunction(potential_proteins)
    assert list(potential_proteins('ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA')) == [
        'MAMAPRTEINSTRING', 'MAPRTEINSTRING']
    # Get the SARS-CoV-2 reference genome
    sars_cov_2 = ''.join(filter(lambda c: c in 'ACGT', open('/srv/datasets/sars-cov-2').read()))
    # Get the primary structure of the SARS-CoV-2 spike protein
    sars_cov2_spike = open('/srv/datasets/sars-cov-2-spike-glycoprotein').read().rstrip()
    # Ensure we can find the spike protein (and all other potential proteins) in the genome
    sars_cov2_proteins = list(potential_proteins(sars_cov_2))
    assert sars_cov2_spike in sars_cov2_proteins
    assert len(sars_cov2_proteins) == 485
    # Assume DNA on standard input, and discard invalid (non-ACGT)  characters.
    import sys
    input_dna = ''.join(filter(lambda c: c in 'ACGT', sys.stdin.read()))
    # Print all potential proteins in stdin (and their masses) to stdout, one per line
    for possible_protein in potential_proteins(input_dna):
        print(possible_protein, format(mass(possible_protein), '.4f'))
