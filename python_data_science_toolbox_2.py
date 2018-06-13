import pandas as pd
from pprint import pprint as pp

# Using Iterators in Python

# Here, you'll learn all about iterators and iterables, which you have already worked with before when writing for
# loops! You'll learn about some very useful functions that will allow you to effectively work with iterators and
# finish the chapter with a use case that is pertinent to the world of Data Science - dealing with large amounts of
# data - in this case, data from Twitter that you will load in chunks using iterators!

avengers = ['hawkeye', 'iron man', 'thor', 'quicksliver']
names = ['barton', 'stark', 'odinson', 'maximoff']
mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pride']
mutants_tuple = ('charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pride')
aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']
powers_tuple = ('telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility')


def lesson_enumerate():
    print('Part 1:')
    e = enumerate(avengers)
    print(type(e))
    e_list = list(e)
    print(e_list)
    print('\nPart 2:')
    for i, v in enumerate(avengers, start=10):
        print(i, v)


print('Output of lesson_enumerate:')
lesson_enumerate()


def lesson_zip():
    print('Part 1:')
    z = zip(avengers, names)
    print(type(z))
    z_list = list(z)
    print(z_list)

    print('\nPart 2:')
    for z1, z2 in zip(avengers, names):
        print(z1, z2)

    print('\nPart 3:')
    z = zip(avengers, names)  # z has to be repacked because the iter object was used in part 1
    print(*z)


print('\nOutput of lesson_zip:')
lesson_zip()


def ex_1():
    # Create a list of strings: mutants -> above
    # Create a list of tuples: mutant_list
    # Create a list of tuples: mutant_list
    mutant_list = list(enumerate(mutants))

    # Print the list of tuples
    print(mutant_list)

    # Unpack and print the tuple pairs
    for index1, value1 in mutant_list:
        print(index1, value1)

    # Change the start index
    for index2, value2 in enumerate(mutants, start=1):
        print(index2, value2)


print('\nOutput of ex_1:')
ex_1()


def ex_2():
    # Create a list of tuples: mutant_data
    mutant_data = list(zip(mutants, aliases, powers))

    # Print the list of tuples
    print(mutant_data)

    # Create a zip object using the three lists: mutant_zip
    mutant_zip = zip(mutants, aliases, powers)

    # Print the zip object
    print(mutant_zip)

    # Unpack the zip object and print the tuple values
    for value1, value2, value3 in mutant_zip:
        print(value1, value2, value3)


print('\nOutput of ex_2:')
ex_2()


def ex_3():
    # Create a zip object from mutants and powers: z1
    z1 = zip(mutants_tuple, powers_tuple)

    # Print the tuples in z1 by unpacking with *
    print(*z1)

    # Re-create a zip object from mutants and powers: z1
    z1 = zip(mutants, powers)

    # 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
    result1, result2 = zip(*z1)

    # Check if unpacked tuples are equivalent to original tuples
    print(result1 == mutants_tuple)
    print(result2 == powers_tuple)


print('\nOutput of ex_3:')
ex_3()


def lesson_iter_data():
    #No output
    # Part 1:
    result = []
    for chunk in pd.read_csv('data.csv', chunsize=1000):
        result.append(sum(chunk['x']))

    total = sum(result)
    print(total)

    # Part 2:
    total = 0
    for chunk in pd.read_csv('data.csv', chunsize=1000):
        total += sum(chunk['x'])

    print(total)


def ex_4():
    # Initialize an empty dictionary: counts_dict
    counts_dict = dict()

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv('tweets.csv', chunksize=10):

        # Iterate over the column in DataFrame
        for entry in chunk['lang']:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Print the populated dictionary
    pp(counts_dict, compact=True)


print('\nOutput of ex_4:')
ex_4()


def count_entries_1(csv_file, c_size=10, colname='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict


print('\nOutput for count_entries_1:')
result_counts = count_entries_1('tweets.csv')
print(result_counts)


# List Comprehensions and Generators

# In this chapter, you'll build on your knowledge of iterators and be introduced to list comprehensions, which allow
# you to create complicated lists and lists of lists in one line of code! List comprehensions can dramatically
# simplify your code and make it more efficient, and will become a vital part of your Python Data Science toolbox.
# You'll then learn about generators, which are extremely helpful when working with large sequences of data that you
# may not want to store in memory but instead generate on the fly.

# List Comprehensions:
# * Create list from other lists, DataFrame columns, etc.
# * Single line of code
# * More efficient than using a for loop
#
# Collapse for loops for building lists into a single line
# * Components
#   * Iterable
#   * Iterator variable (represent members of iterable)
#   * Output expression


def lesson_nested():
    pairs_2 = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)]
    print(pairs_2)


print('\nOutput of lesson_nested:')
lesson_nested()


def ex_5():
    # Create a 5 x 5 matrix using a list of lists: matrix
    matrix = [[col for col in range(5)] for row in range(5)]

    pp(matrix)


print('\nOutput of ex_5:')
ex_5()


def lesson_comp_conditional():
    example = [num ** 2 if num % 2 == 0 else 0 for num in range(21)]
    print(example)


print('\nOutput for lesson_comp_conditional:')
lesson_comp_conditional()


def lesson_comp_dict():
    pos_neg = {num: -num for num in range(9)}
    print(pos_neg)


print('\nOutput for lesson_comp_dict:')
lesson_comp_dict()


# Bring it all Together!

# This chapter will allow you to apply your newly acquired skills towards wrangling and extracting meaningful
# information from a real-world dataset - the World Bank's World Development Indicators dataset! You'll have the
# chance to write your own functions and list comprehensions as you work with iterators and generators and solidify
# your Python Data Science chops. Enjoy!
