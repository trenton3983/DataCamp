import pandas as pd


# User Defined Functions


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

        print(entry)

        # # If the language is in langs_count, add 1
        # if entry in langs_count.keys():
        #     ____
        # # Else add the language to langs_count, set the value to 1
        # else:
        #     ____

    # Print the populated dictionary
    print(langs_count)


tweets()