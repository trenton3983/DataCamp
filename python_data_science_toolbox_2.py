import pandas as pd
from pprint import pprint as pp
from pathlib import Path

pd.options.display.max_columns = 15

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
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']


tweets_df = pd.read_csv('tweets.csv')


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
#
# https://www.datacamp.com/community/tutorials/python-list-comprehension

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


def ex_6():
    print('https://www.datacamp.com/community/tutorials/python-list-comprehension')
    # Create a list of strings: fellowship -> at the top
    # Create list comprehension: new_fellowship
    new_fellowship_if = [member for member in fellowship if len(member) >= 7]
    new_fellowship_if_else_ = [member if len(member) >= 7 else '' for member in fellowship]

    # Print the new list
    print(new_fellowship_if)
    print(new_fellowship_if_else_)


print('\nOutput for ex_6:')
ex_6()


def dict_comprehension():
    # Create dict comprehension: new_fellowship
    new_fellowship = {member: len(member) for member in fellowship}

    # Print the new list
    print(new_fellowship)


print('\nOutput of dict_comprehension:')
dict_comprehension()

# Generator Expressions
print('\nGenerator Expressions')


def num_sequence(n):
    """
    Generate values from o to n
    :param n: int
    :return:
    """
    i = 0
    while i < n:
        yield i
        i += 1


print('\nOutput of num_sequence:')
lesson_num_sequence = num_sequence(100)
print(lesson_num_sequence)
for item in lesson_num_sequence:
    print(item)


def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)


# Print the values generated by get_lengths()
print('\nOutput of get_lengths:')
for value in get_lengths(lannister):
    print(value)


def time_stamp_tweets(df):
    # Extract the created_at column from df: tweet_time
    tweet_time = df['created_at']
    # Extract the clock time: tweet_clock_time
    tweet_clock_time = [entry[11:19] for entry in tweet_time]
    tweet_clock_time_19 = [entry[11:19] for entry in tweet_time if entry[17:19] == '19']
    print('Tweet Times:')
    pp(tweet_clock_time, compact=True)
    print('\nTweet Times 19:')
    pp(tweet_clock_time_19, compact=True)


print('\nOutput of time_stamp_tweets:')
time_stamp_tweets(tweets_df)

# Bring it all Together!

# This chapter will allow you to apply your newly acquired skills towards wrangling and extracting meaningful
# information from a real-world dataset - the World Bank's World Development Indicators dataset! You'll have the
# chance to write your own functions and list comprehensions as you work with iterators and generators and solidify
# your Python Data Science chops. Enjoy!

print("\n\nWorld Bank's World Development Indicators dataset:")

# https://datacatalog.worldbank.org/dataset/world-development-indicators
# http://databank.worldbank.org/data/download/WDI_csv.zip
world_dev_ind = Path(__file__).parents[4].joinpath('PythonProjects/Data/WDIData.csv')
# https://raw.githubusercontent.com/johnashu/datacamp/master/ind_pop.csv
ind_pop = Path(__file__).parents[4].joinpath('PythonProjects/Data/ind_pop.csv')
# wdi_data_df = pd.read_csv(world_dev_ind)

row_lists = [['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298'], ['Arab World', 'ARB', 'Age dependency ratio (% of working-age population)', 'SP.POP.DPND', '1960', '87.7976011532547'], ['Arab World', 'ARB', 'Age dependency ratio, old (% of working-age population)', 'SP.POP.DPND.OL', '1960', '6.634579191565161'], ['Arab World', 'ARB', 'Age dependency ratio, young (% of working-age population)', 'SP.POP.DPND.YG', '1960', '81.02332950839141'], ['Arab World', 'ARB', 'Arms exports (SIPRI trend indicator values)', 'MS.MIL.XPRT.KD', '1960', '3000000.0'], ['Arab World', 'ARB', 'Arms imports (SIPRI trend indicator values)', 'MS.MIL.MPRT.KD', '1960', '538000000.0'], ['Arab World', 'ARB', 'Birth rate, crude (per 1,000 people)', 'SP.DYN.CBRT.IN', '1960', '47.697888095096395'], ['Arab World', 'ARB', 'CO2 emissions (kt)', 'EN.ATM.CO2E.KT', '1960', '59563.9892169935'], ['Arab World', 'ARB', 'CO2 emissions (metric tons per capita)', 'EN.ATM.CO2E.PC', '1960', '0.6439635478877049'], ['Arab World', 'ARB', 'CO2 emissions from gaseous fuel consumption (% of total)', 'EN.ATM.CO2E.GF.ZS', '1960', '5.041291753975099'], ['Arab World', 'ARB', 'CO2 emissions from liquid fuel consumption (% of total)', 'EN.ATM.CO2E.LF.ZS', '1960', '84.8514729446567'], ['Arab World', 'ARB', 'CO2 emissions from liquid fuel consumption (kt)', 'EN.ATM.CO2E.LF.KT', '1960', '49541.707291032304'], ['Arab World', 'ARB', 'CO2 emissions from solid fuel consumption (% of total)', 'EN.ATM.CO2E.SF.ZS', '1960', '4.72698138789597'], ['Arab World', 'ARB', 'Death rate, crude (per 1,000 people)', 'SP.DYN.CDRT.IN', '1960', '19.7544519237187'], ['Arab World', 'ARB', 'Fertility rate, total (births per woman)', 'SP.DYN.TFRT.IN', '1960', '6.92402738655897'], ['Arab World', 'ARB', 'Fixed telephone subscriptions', 'IT.MLT.MAIN', '1960', '406833.0'], ['Arab World', 'ARB', 'Fixed telephone subscriptions (per 100 people)', 'IT.MLT.MAIN.P2', '1960', '0.6167005703199'], ['Arab World', 'ARB', 'Hospital beds (per 1,000 people)', 'SH.MED.BEDS.ZS', '1960', '1.9296220724398703'], ['Arab World', 'ARB', 'International migrant stock (% of population)', 'SM.POP.TOTL.ZS', '1960', '2.9906371279862403'], ['Arab World', 'ARB', 'International migrant stock, total', 'SM.POP.TOTL', '1960', '3324685.0']]
feature_names = ['CountryName', 'CountryCode', 'IndicatorName', 'IndicatorCode', 'Year', 'Value']


# Define lists2dict()
def lists2dict(list1, list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return (rs_dict)


# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names, row_lists[0])

# Print rs_fxn
print('\nSample Output of lists2dict:')
print(rs_fxn)

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print('\nList of Dicts')
pp(list_of_dicts[0:3])

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print(df.head(10))


# Iteratively read WDIData.csv
def iterative_parse(filename):
    # Open a connection to the file
    with open(filename) as file:

        # Skip the column names
        file.readline()

        # Initialize an empty dictionary: counts_dict
        counts_dict = {}

        # Process only the first 1000 rows
        for j in range(10000):

            # Split the current line into a list: line
            line = file.readline().split(',')

            # Get the value for the first column: first_col
            first_col = line[0]

            # If the column value is in the dict, increment its value
            if first_col in counts_dict.keys():
                counts_dict[first_col] += 1

            # Else, add to the dict and set value to 1
            else:
                counts_dict[first_col] = 1

    # Print the resulting dictionary
    pp(counts_dict)
    file.close()


print('\nOutput of iterative_parse:')
iterative_parse(world_dev_ind)


# Writing a generator to load data in chunks (2)
# Define read_large_file()
def read_large_file(file_object):
    """
    A generator function to read a large file lazily.

    In the previous exercise, you processed a file line by line for a given number of lines. What if, however, you want
    to do this for the entire file?

    In this case, it would be useful to use generators. Generators allow users to lazily evaluate data. This concept of
    lazy evaluation is useful when you have to deal with very large datasets because it lets you generate values in an
    efficient manner by yielding only chunks of data at a time instead of the whole thing at once.
    http://www.blog.pythonlibrary.org/2014/01/27/python-201-an-intro-to-generators/

    In this exercise, you will define a generator function read_large_file() that produces a generator object which
    yields a single line from a file each time next() is called on it. The csv file 'world_dev_ind.csv' is in your
    current directory for your use.

    Note that when you open a connection to a file, the resulting file object is already a generator! So out in the
    wild, you won't have to explicitly create generator objects in cases such as this. However, for pedagogical
    reasons, we are having you practice how to do this here with the read_large_file() function. Go for it!
    :param file_object:
    :return:
    """

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data


# Open a connection to the file
with open(world_dev_ind) as file:
    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print('\nOutput of read_large_file:')
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))
    file.close()


# Writing a generator to load data in chunks (3)
def ex_7():
    """
    Great! You've just created a generator function that you can use to help you process large files.

    Now let's use your generator function to process the World Bank dataset like you did previously. You will process
    the file line by line, to create a dictionary of the counts of how many times each country appears in a column in
    the dataset. For this exercise, however, you won't process just 1000 rows of data, you'll process the entire
    dataset!

    The generator function read_large_file() and the csv file 'world_dev_ind.csv' are preloaded and ready for your use.
    :return:
    """
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Open a connection to the file
    with open(world_dev_ind) as file_ex_7:

        # Iterate over the generator from read_large_file()
        for line in read_large_file(file_ex_7):

            row = line.split(',')
            first_col = row[0]

            if first_col in counts_dict.keys():
                counts_dict[first_col] += 1
            else:
                counts_dict[first_col] = 1

    # Print
    pp(counts_dict)


print('\nOutput of ex_7:')
ex_7()


# Writing an iterator to load data in chunks (1)
def ex_8():
    """
    Another way to read data too large to store in memory in chunks is to read the file in as DataFrames of a certain
    length, say, 100. For example, with the pandas package (imported as pd), you can do pd.read_csv(filename,
    chunksize=100). This creates an iterable reader object, which means that you can use next() on it.

    In this exercise, you will read a file in small DataFrame chunks with read_csv(). You're going to use the World Bank
    Indicators data 'ind_pop.csv', available in your current directory, to look at the urban population indicator for
    numerous countries and years.
    :return:
    """

    # Initialize reader object: df_reader
    df_reader = pd.read_csv(ind_pop, chunksize=10)

    # Print two chunks
    pp(next(df_reader))
    pp(next(df_reader))


print('\nOutput of ex_8:')
ex_8()


# Writing an iterator to load data in chunks (2)
def ex_9():
    """
    In the previous exercise, you used read_csv() to read in DataFrame chunks from a large dataset. In this exercise,
    you will read in a file using a bigger DataFrame chunk size and then process the data from the first chunk.

    To process the data, you will create another DataFrame composed of only the rows from a specific country. You will
    then zip together two of the columns from the new DataFrame, 'Total Population' and 'Urban population (% of total)'. Finally, you will create a list of tuples from the zip object, where each tuple is composed of a value from each of the two columns mentioned.

    You're going to use the data from 'ind_pop_data.csv', available in your current directory. Pandas has been imported
    as pd.
    :return:
    """
    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(ind_pop, chunksize=1000)

    # Get the first DataFrame chunk: df_urb_pop
    df_urb_pop = next(urb_pop_reader)

    # Check out the head of the DataFrame
    print(df_urb_pop.head())

    # Check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

    # Zip DataFrame columns of interest: pops
    pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])

    # Turn zip object into list: pops_list
    pops_list = list(pops)

    # Print pops_list
    print(pops_list)


print('\nOutput of ex_9:')
ex_9()


# Writing an iterator to load data in chunks (3)
def ex_10():
    """
    You're getting used to reading and processing data in chunks by now. Let's push your skills a little further by
    adding a column to a DataFrame.

    In this exercise, you will be using a list comprehension to create the values for a new column 'Total Urban
    Population' from the list of tuples that you generated earlier. Recall from the previous exercise that the first a
    nd second elements of each tuple consist of, respectively, values from the columns 'Total Population' and 'Urban
    population (% of total)'. The values in this new column 'Total Urban Population', therefore, are the product of the
    first and second element in each tuple. Furthermore, because the 2nd element is a percentage, you need to divide
    the entire result by 100, or alternatively, multiply it by 0.01.

    You will also plot the data from this new column to create a visualization of the urban population data.

    You're going to use the data from 'ind_pop_data.csv', available in your current directory. The packages pandas and
    matplotlib.pyplot have been imported as pd and plt respectively for your use.
    :return:
    """
    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(ind_pop, chunksize=1000)

    # Get the first DataFrame chunk: df_urb_pop
    df_urb_pop = next(urb_pop_reader)

    # Check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

    # Zip DataFrame columns of interest: pops
    pops = zip(df_pop_ceb['Total Population'],
               df_pop_ceb['Urban population (% of total)'])

    # Turn zip object into list: pops_list
    pops_list = list(pops)

    # Use list comprehension to create new DataFrame column 'Total Urban Population'
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    print(df_pop_ceb.head())

    # Plot urban population data
    df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')


print('\nOutput of ex_10:')
ex_10()


# Writing an iterator to load data in chunks (4)
def ex_11():
    """
    In the previous exercises, you've only processed the data from the first DataFrame chunk. This time, you will
    aggregate the results over all the DataFrame chunks in the dataset. This basically means you will be processing the
    entire dataset now. This is neat because you're going to be able to process the entire large dataset by just working
    on smaller pieces of it!

    You're going to use the data from 'ind_pop_data.csv', available in your current directory. The packages pandas and
    matplotlib.pyplot have been imported as pd and plt respectively for your use.
    :return:
    """
    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(ind_pop, chunksize=1000)

    # Initialize empty DataFrame: data
    data = pd.DataFrame()

    # Iterate over each DataFrame chunk
    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

        # Zip DataFrame columns of interest: pops
        pops = zip(df_pop_ceb['Total Population'],
                   df_pop_ceb['Urban population (% of total)'])

        # Turn zip object into list: pops_list
        pops_list = list(pops)

        # Use list comprehension to create new DataFrame column 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1]) for tup in pops_list]

        # Append DataFrame chunk to data: data
        data = data.append(df_pop_ceb)

    # Plot urban population data
    data.plot(kind='scatter', x='Year', y='Total Urban Population')


print('\nOutput of ex_11:')
ex_11()


# Writing an iterator to load data in chunks (5)
def ex_12():
    """
    This is the last leg. You've learned a lot about processing a large dataset in chunks. In this last exercise, you
    will put all the code for processing the data into a single function so that you can reuse the code without having
    to rewrite the same things all over again.

    You're going to define the function plot_pop() which takes two arguments: the filename of the file to be processed,
    and the country code of the rows you want to process in the dataset.

    Because all of the previous code you've written in the previous exercises will be housed in plot_pop(), calling the
    function already does the following:

    Loading of the file chunk by chunk,
    Creating the new column of urban population values, and
    Plotting the urban population data.
    That's a lot of work, but the function now makes it convenient to repeat the same process for whatever file and
    country code you want to process and visualize!

    You're going to use the data from 'ind_pop_data.csv', available in your current directory. The packages pandas and
    matplotlib.pyplot has been imported as pd and plt respectively for your use.

    After you are done, take a moment to look at the plots and reflect on the new skills you have acquired. The journey
    doesn't end here! If you have enjoyed working with this data, you can continue exploring it using the pre-processed
    version available on Kaggle.
    :return:
    """

    # Define plot_pop()
    def plot_pop(filename, country_code):
        # Initialize reader object: urb_pop_reader
        urb_pop_reader = pd.read_csv(filename, chunksize=1000)

        # Initialize empty DataFrame: data
        data = pd.DataFrame()

        # Iterate over each DataFrame chunk
        for df_urb_pop in urb_pop_reader:
            # Check out specific country: df_pop_ceb
            df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

            # Zip DataFrame columns of interest: pops
            pops = zip(df_pop_ceb['Total Population'],
                       df_pop_ceb['Urban population (% of total)'])

            # Turn zip object into list: pops_list
            pops_list = list(pops)

            # Use list comprehension to create new DataFrame column 'Total Urban Population'
            df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1]) for tup in pops_list]

            # Append DataFrame chunk to data: data
            data = data.append(df_pop_ceb)

        # Plot urban population data
        data.plot(kind='scatter', x='Year', y='Total Urban Population')

    # Set the filename: fn
    fn = 'ind_pop_data.csv'

    # Call plot_pop for country code 'CEB'
    plot_pop(ind_pop, 'CEB')

    # Call plot_pop for country code 'ARB'
    plot_pop(ind_pop, 'ARB')


print('\nOutput of ex_12:')
ex_12()