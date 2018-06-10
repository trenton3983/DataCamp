import pandas as pd


def test_1():
    logins = {'MONTH': ['JAN', 'FEB'],
              'day': [7, 8],
              'year': [2015, 2015],
              'session_id': [17357, 10011]}

    logins_df = pd.DataFrame.from_dict(logins)

    for j, p in logins_df.iterrows():
        logins_df.loc[j, 'month'] = p['MONTH'].lower()

    print(logins_df)


def test_2():
    marketing = {'ID': [1, 2, 3, 4],
                 'Views': [1000, 1200, 800, 1500],
                 'Clicks': [300, 800, 500, 990]}

    marketing_df = pd.DataFrame.from_dict(marketing)

    print(marketing_df)


test_2()
