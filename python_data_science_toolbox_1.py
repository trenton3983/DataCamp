import pandas as pd
import csv
from pprint import pprint as pp
from functools import reduce


def read_out_csv():
    with open('tweets.csv') as fp:
        reader = csv.reader(fp)
        for row in reader:
            print(row)


def make_df(file_name):
    return pd.read_csv(file_name)


def square(value: float) -> float:  # Function Header with parameters and type hints
    """
    Return the square of a value
    :param value: float
    :return: float
    """
    new_value = value ** 2
    print(new_value)  # Function Body
    return new_value


in_num = 3.0
num = square(in_num)
print('\nOutput from the function square:')
print(f'The square of {in_num} is {num} and its type is {type(num)}\n')


def raise_to_power(value1: float, value2: float) -> tuple:
    """
    Raise value1 to the power of value2 and vise versa
    :param value1: float
    :param value2: float
    :return: tuple of floats
    """
    new_value1 = value1 ** value2
    new_value2 = value2 ** value1
    return new_value1, new_value2


in_num = [10.0, 40.5]
num1, num2 = raise_to_power(in_num[0], in_num[1])
print('\nOutput from the function raise_to_power:')
print(f'Value1^Value2: {num1}\nValue2^Value1: {num2}\n')


def tweets():
    # Import Twitter data as DataFrame: df
    df = pd.read_csv('tweets.csv')

    # Initialize an empty dictionary: langs_count
    langs_count = {}

    # Extract column from DataFrame: col
    col = df['lang']

    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] = langs_count[entry] + 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Print the populated dictionary
    print(langs_count)


print('\nOutput from the function tweets:')
tweets()


def count_entries(df, col_name):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: langs_count
    langs_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over lang column in DataFrame
    for entry in col:

        # If the language is in langs_count, add 1
        if entry in langs_count.keys():
            langs_count[entry] = langs_count[entry] + 1
        # Else add the language to langs_count, set the value to 1
        else:
            langs_count[entry] = 1

    # Return the langs_count dictionary
    return langs_count


# Call count_entries(): result
result = count_entries(make_df('tweets.csv'), 'lang')

# Print the result
print('\nOutput from the function count_entries:')
print(result)


def count_entries2(df, col_name='lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Extract column from DataFrame: col
    col = df[col_name]

    # Iterate over the column in DataFrame
    for entry in col:

        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1

        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count


tweets_df = make_df('tweets.csv')

# Call count_entries(): result1
result1 = count_entries2(tweets_df)

# Call count_entries(): result2
result2 = count_entries2(tweets_df, col_name='source')

# Print result1 and result2
print('\nOutput from the function count_entries2:')
print('Result1:')
pp(result1)
print('Result2:')
pp(result2)


def count_entries3(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""

    # Initialize an empty dictionary: cols_count
    cols_count = {}

    # Iterate over column names in args
    for col_name in args:

        # Extract column from DataFrame: col
        col = df[col_name]

        # Iterate over the column in DataFrame
        for entry in col:

            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1

            # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1

    # Return the cols_count dictionary
    return cols_count


# Call count_entries(): result1
result1 = count_entries3(tweets_df, 'lang')

# Call count_entries(): result2
result2 = count_entries3(tweets_df, 'lang', 'source')

# Print result1 and result2
print('\nOutput from the function count_entries3:')
print('Result1:')
pp(result1)
print('Result2:')
pp(result2)
print('\n')


# Lambda Functions
print('\n')
print('Lambda Functions: https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/')
print('\n')


def ex_1():
    nums = [48, 6, 9, 21, 1]
    square_all = map(lambda num: num ** 2, nums)
    print('Using Lambda Functions:')
    print(square_all)
    print(list(square_all))
    print('\n')


ex_1()


def ex_2():
    add_bangs = (lambda a: a + '!!!')
    print(add_bangs('hello'))


ex_2()


def ex_3():
    # Define echo_word as a lambda function: echo_word
    echo_word = (lambda word1, echo: word1 * echo)

    # Call echo_word: result
    result_ex_3 = echo_word('hey', 5)

    # Print result
    print('\nResult ex_3:')
    print(result_ex_3)


ex_3()


def ex_4():
    # Create a list of strings: spells
    spells = ["protego", "accio", "expecto patronum", "legilimens"]

    # Use map() to apply a lambda function over spells: shout_spells
    shout_spells = map(lambda x: x + '!!!', spells)

    # Convert shout_spells to a list: shout_spells_list
    shout_spells_list = list(shout_spells)

    # Convert shout_spells into a list and print it
    print('\nResult ex_4: shout_spells')
    print(shout_spells_list)


ex_4()


def ex_5():
    # Create a list of strings: fellowship
    fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

    # Use filter() to apply a lambda function over fellowship: result
    result_ex_5 = filter(lambda x: (len(x) > 6), fellowship)

    # Convert result to a list: result_list
    result_list = list(result_ex_5)

    # Convert result into a list and print it
    print('\nResult ex_5: fellowship')
    print(result_list)


ex_5()


def ex_6():
    # Import reduce from functools -> above

    # Create a list of strings: stark
    stark = ['robb', 'sansa', 'arya', 'eddard', 'jon']

    # Use reduce() to apply a lambda function over stark: result
    result_ex_6 = reduce((lambda item1, item2: (item1 + item2)), stark)

    # Print the result
    print('\nResult ex_6: starks')
    print(result_ex_6)


ex_6()


# Error Handling
print('\nError Handling:\n')


def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""

    # Raise an error with raise
    if echo < 0:
        raise ValueError('echo must be greater than 0')

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word


# Call shout_echo
print('\nResult shout_echo')
result_shout_echo = shout_echo("particle", echo=5)
print(result_shout_echo)


# Bring it all together
print('\nBring it all together!\n')


