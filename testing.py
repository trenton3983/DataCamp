import pandas as pd
import numpy as np


def test_1():
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


def test_2():
    marketing = {'ID': [1, 2, 3, 4],
                 'Views': [1000, 1200, 800, 1500],
                 'Clicks': [300, 800, 500, 990]}

    marketing_df = pd.DataFrame(marketing)

    print(marketing_df)


def test_3():
    group = ['fruit', 'fruit', 'fruit', 'vegetable', 'vegetable', 'vegetable']
    name = ['apple', 'banana', 'oragne', 'broccoli', 'kale', 'lettuce']
    count = [90, 150, 130, 80, 70, 125]
    prod_dict = {'group': group, 'name': name, 'count': count}
    df = pd.DataFrame(prod_dict)
    print(df, '\n')
    print(df[np.invert(df['group'] == 'fruit')])


test_2()

