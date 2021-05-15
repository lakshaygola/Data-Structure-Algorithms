"""Problem statement: - We have a gene which reperesent as a string and contain 'A', 'C', 'T' and 'G'. Gene should be
                steady and it can only be steady if all the character in gene repeat (length.gene / 4) times.
                We have to find the lenght of the substring which can be replace to make the string steay."""
import collections

# Function to solve the problem
def steadGene(gene):
    geneLength = len(gene)
    steadFactor = geneLength / 4

    # Dict to count the occurance of all the characters in gene
    characters = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for i in gene:
        characters[i] += 1

    if (characters['A'] == steadFactor and characters['C'] == steadFactor and characters['T'] == steadFactor and
            characters['G'] == steadFactor):
        return 0

    upper = lower = 0
    minLength = geneLength

    while upper < geneLength and lower < geneLength:
        # If some of the character have occurrence grater then the steadFactor then we move the upper pointer and
        # decrement the values of the occurrence
        while (characters['A'] > steadFactor or characters['C'] > steadFactor or characters['T'] > steadFactor or
               characters['G'] > steadFactor) and upper < geneLength:

            characters[gene[upper]] -= 1
            upper += 1

        while (characters['A'] <= steadFactor and characters['C'] <= steadFactor and characters['T'] <= steadFactor and
               characters['G'] <= steadFactor):

            characters[gene[lower]] += 1
            lower += 1

        minLength = min(minLength, upper - lower + 1)
    return minLength


# Test Case 1
string1 = 'GAAATAAA'
print(steadGene(string1))

# Test Case 2
string2 = 'TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC'
print(steadGene(string2))