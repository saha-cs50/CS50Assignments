import csv
from sys import argv


def main():

    # checking that correct command line arguments are given
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")

    # reading database file given in command line argument
    with open(argv[1]) as a:
        reader = csv.reader(a)
        database = list(reader)

    # reading dna file in command line argument
    with open(argv[2]) as f:
        strs = f.read()

    # finding longest dna str sequence
    match = []
    for j in range(1, len(database[0])):
        match.append(longest_match(strs, database[0][j]))

    # matching sequence to people
    person = 'No Match'
    personcounter = 0

    for i in range(1, len(database)):
        for j in range(len(match)):
            # converting all ints to strings
            if match[j] == int(database[i][j+1]):
                personcounter += 1

        if personcounter == len(match):
            person = database[i][0]
            break
        else:
            personcounter = 0
    print(person)

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
