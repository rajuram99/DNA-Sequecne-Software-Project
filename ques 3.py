# 1. Transcribing the DNA

def Transcribing_DNA():
    # reading the dna
    with open('e_coli.txt') as f:
        contents = f.read()
    rna = ""
    dna = contents

    """
    dna : string literal, which stores the dna read from the file
    rna : string literal, which stores the transcribed RNA from dna
    """

    # iterating over every base of dna and replacing it with the complementary base to get the rna

    for i in range(len(dna)):
        if (dna[i] == 'G'):
            rna += 'C'
        elif (dna[i] == 'C'):
            rna += 'G'
        elif (dna[i] == 'T'):
            rna += 'A'
        else:
            rna += 'U'
    return rna


# 2. Reading encodings

def Reading_encodings():
    lines = []

    # reading the encodings from the given file

    with open('genetic_code.txt') as f:
        lines = f.readlines()
        dict = {}
    """
    lines : variable which stores all the lines in the encodings file
    dict : a dictionary variable which will store all encodings
    """
    for line in lines:
        s1 = ""
        s2 = ""
        c = 0

        # generating a single encoding

        for i in range(len(line)):
            if (line[i] != '\t' and line[i] != '\n'):
                if (c != 3):
                    s1 += line[i]
                    c = c + 1
                else:
                    s2 += line[i]
        dict[s1] = s2
    return dict


# 3. Translating RNA

def Translating_RNA():
    # getting the complete rna sequence from the corresponding input file by using the Transcribing_DNA function
    rna = Transcribing_DNA()
    # getting the encodings in dict (a dictionary) from genetic_code.txt by using the Reading_encodings function
    dict = Reading_encodings()

    all_Protein_Sequence(rna,dict)


# 4. Creating a protein sequence

def one_Protein_Sequence(rna, dict):
    seq = ""
    """
    seq : a string literal, which stores the generated protein sequence 
    """
    for i in range(len(rna)):
        if (i % 3 == 0):
            s = ""
        s += rna[i]
        if (i % 3 == 2):
            seq+=' '
            seq += dict[s]
    print(seq)


# 5. Creating all protein sequences

def all_Protein_Sequence(rna, dict):
    # genertaing the 3 offsets

    for i in range(3):
        rna1 = ""
        """
        rna1 : stores the rna sequence from index i to len(rna)

        """
        for j in range(i, len(rna)):
            rna1 += rna[j]
        # generating the protein sequence from the current offset
        one_Protein_Sequence(rna1, dict)
        print('\n')

def main():
    Translating_RNA()

if __name__ == "__main__" :
  main()
