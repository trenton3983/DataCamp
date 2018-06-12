import pandas as pd
import numpy as np


def exer_1():
    logins = {'MONTH': ['JAN', 'FEB'],
              'day': [7, 8],
              'year': [2015, 2015],
              'session_id': [17357, 10011]}

    logins_df = pd.DataFrame(logins)
    print(logins_df, '\n')

    # add 'month' to the DataFrame and give it the value of 'MONTH' at index j
    for j, p in logins_df.iterrows():
        logins_df.loc[j, 'month'] = p['MONTH'].lower()

    print(logins_df)


print('Output of exer_1:')
exer_1()


def exer_2():
    marketing = {'ID': [1, 2, 3, 4],
                 'Views': [1000, 1200, 800, 1500],
                 'Clicks': [300, 800, 500, 990]}

    marketing_df = pd.DataFrame(marketing)

    print(marketing_df)


print('\nOutput of exer_2:')
exer_2()


def exer_3():
    group = ['fruit', 'fruit', 'fruit', 'vegetable', 'vegetable', 'vegetable']
    name = ['apple', 'banana', 'oragne', 'broccoli', 'kale', 'lettuce']
    count = [90, 150, 130, 80, 70, 125]
    prod_dict = {'group': group, 'name': name, 'count': count}
    df = pd.DataFrame(prod_dict)
    print(df, '\n')
    print(df[np.invert(df['group'] == 'fruit')])


print('\nOutput of exer_3:')
exer_3()


def nth_root(n):
    """Returns the actual_root function"""
    def actual_root(x):
        """Returns the nth root of x"""
        root = x ** (1/n)
        return root
    return actual_root


print('\nOutput of nth_root:')
square_root = nth_root(2)
cube_root = nth_root(3)
print(square_root(16), cube_root(27))


def easy_print(**kwargs):
    for p, q in kwargs.items():
        print('The value of ' + str(p) + " is " + str(q))


print('\nResult of easy_print')
easy_print(x=10, y=20)


def add_zeros(string):
    """Returns a string padded with zeros to ensure consistent length"""
    updated_string = string + '0'

    def add_more():
        """Adds more zeros if necessary"""
        nonlocal updated_string
        updated_string = updated_string + '0'

    while len(updated_string) < 6:
        add_more()
    return updated_string


print('\nResult of add_zeros: nonlocal variable updates')
(add_zeros('2.3'), add_zeros('5.678'))
