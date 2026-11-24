######################################################################
# Author(s): Alain Irumva
# Username(s): irumvaa
#
# Assignment: HW08: It's in Your Genes
#
# Purpose: Determine an amino acid sequence given an input DNA sequence
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
#   Ideas borrowed from j. ben Schafer: https://www.cs.uni.edu/~schafer/
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

# TODO   I highly recommend STARTING by building more test cases for each function in the test suite file.
# TODO   If you can build accurate test cases, you can be confident that you understand
# TODO   the intended functionality of each function.


def is_nucleotide(sequence):
    """
    Checks that the string sequence provided is a valid string
    consisting only of the 4 nucleotides A, C, G, and T
    Returns True if so, and False otherwise

    :param sequence: string of DNA sequence
    :return: True if the sequence contains only A, C, G, and T; otherwise False.
    """
# Use Dictionary
    acceptable_pairing = { "A", "C", "G", "T"
        }
    if len(sequence) == 0:
        return False
    for seq in sequence:
        if seq not in acceptable_pairing:
            return False
    return True

    # FIXME: Finish the docstring above by providing a brief description
    #        of the parameter 'sequence' and what the function returns

    # FIXME: Add your code here to complete this function

    # FIXME: Clearly this should not always return True
    return True


def complement_strand(sequence):
    """
    Returns the string which will be the second strand of the DNA sequence
    given that Ts complement As, and Cs complement Gs. If given
    a bad input, the function returns "Sequencing Error"

    :param sequence: A DNA sequence of A C G T
    :return: complement sequence or error
    """
    # FIXME: Finish the docstring above by providing a brief description
    #        of the parameter 'sequence' and what the function returns
    if not is_nucleotide(sequence):
        return "sequencing error"
    comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complement = ""         # This can be used to "build" the complement

    for seq in sequence:
        complement += comp[seq]
    return complement

    # FIXME: Add your code here to complete this function

    # FIXME: Obviously, this should not always return ""



def mRNA(sequence):
    """
    Replaces each occurrence of the nucleotide T replaced with the nucleotide U.

    :param sequence: A C G T
    :return: A C G U
    """
    # FIXME: Finish the docstring above by providing a brief description
    #        of the parameter 'sequence' and what the function returns

    # FIXME: Add your code here to complete this function
    if not is_nucleotide(sequence):
        return ""
    mrna = ""
    for seq in sequence:
        if seq == "T":
            mrna += "U"
        else:
            mrna += seq

    # FIXME: Obviously, this should not always return ""
    return mrna


def chunk_amino_acid(sequence):
    """
    Uses output of mRNA(sequence) and divides it into substrings of length 3,
    ignoring any "extra DNA" at the far end returning the relevant substrings in a list.

    :param sequence: A C G U
    :return:list of 3 substrings
    """
    # FIXME: Finish the docstring above by providing a brief description of the parameter 'sequence'

    # FIXME: Add your code here to complete this function

    list_of_chunks = []
    for i in range (0, len(sequence) - 2, 3):
        list_of_chunks.append(sequence[i:i+3])

    # FIXME: Obviously, this should not always return an empty string
    return list_of_chunks


def translate_amino_acid(three_char_seq):
    """
    Expects a three character string as a parameter and returns
    the corresponding single character amino acid

    :param three_char_seq: a sequence of three characters
    :return: A string representing the amino acid chunk for that sequence
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #

    translator = {"GCA": "A", "GCC": "A", "GCG": "A", "GCU": "A",
                  "AGA": "R", "AGG": "R", "CGA": "R", "CGC": "R", "CGG": "R", "CGU": "R",
                  "GAC": "D", "GAU": "D",
                  "AAC": "N", "AAU": "N",
                  "UGC": "C", "UGU": "C",
                  "GAA": "E", "GAG": "E",
                  "CAA": "Q", "CAG": "Q",
                  "GGA": "G", "GGC": "G", "GGU": "G", "GGG": "G",
                  "CAC": "H", "CAU": "H",
                  "AUA": "I", "AUC": "I", "AUU": "I",
                  "UUA": "L", "UUG": "L", "CUA": "L", "CUC": "L", "CUG": "L", "CUU": "L",
                  "AAA": "K", "AAG": "K",
                  "AUG": "M",
                  "UUC": "F", "UUU": "F",
                  "CCA": "P", "CCC": "P", "CCG": "P", "CCU": "P",
                  "AGC": "S", "AGU": "S", "UCA": "S", "UCC": "S", "UCG": "S", "UCU": "S",
                  "ACA": "T", "ACC": "T", "ACG": "T", "ACU": "T",
                  "UGG": "W",
                  "UAC": "Y", "UAU": "Y",
                  "GUA": "V", "GUC": "V", "GUG": "V", "GUU": "V",
                  "UAA": "*", "UAG": "*", "UGA": "*"
                 }

    if three_char_seq in translator.keys():
        return translator[three_char_seq]  # Given any 3 letter sequence, this returns the amino acid for that sequence
    else:
        return "?"                          # Returns a question mark if the input is invalid


def sequence_gene(sequence):
    """
    The sequence_gene() function takes a sequence of nucleotides and returns
    the corresponding amino acid sequence.

    :param sequence: a string representing a sequence of nucleotides
    :return: a string representing the amino acid sequence
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #

    aaseq=""                                                # Amino acid sequence
    if is_nucleotide(sequence):                             # Checks for a valid sequence
        comp_strand = complement_strand(sequence)           # Finds the complement sequence
        mrna = mRNA(comp_strand)                            # Finds the mRNA of the complement
        amino_acid_list = chunk_amino_acid(mrna)            # Chunks the mRNA sequence

        for amino_acid in amino_acid_list:                  # Loops through each chunk
            aaseq = aaseq + translate_amino_acid(amino_acid)   # Creates the final amino acid sequence
    return aaseq                                            # Returns an empty string for any illegal input


def main():
    """
    The main() function runs the sequence_gene code, which calls all other parts of this code

    :return: None
    """

    # ###################################################################### #
    # #  This function is already completed correctly! No changes needed!  # #
    # ###################################################################### #
    print("The original sequence {0} returns {1}".format("CACGT", sequence_gene("CACGT")))


if __name__ == "__main__":
    main()          # call to main() function
