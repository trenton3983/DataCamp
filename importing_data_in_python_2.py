import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint as pp
from pathlib import Path
import pandas as pd
from urllib.request import urlretrieve


pd.options.display.max_columns = 27


# Importing data from the Internet
# The web is a rich source of data from which you can extract various types of insights and findings. In this chapter,
# you will learn how to get data from the web, whether it be stored in files or in HTML. You'll also learn the basics
# of scraping and parsing web data.


def lesson_1_files_from_web():
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
    save_name = 'winequality-white.csv'
    urlretrieve(url, save_name)
    print(f'{save_name} saved!')


def ex_1_red_wine():
    """
    Importing flat files from the web: your turn!
    You are about to import your first file from the web! The flat file you will import will be 'winequality-red.csv'
    from the University of California, Irvine's Machine Learning repository. The flat file contains tabular data of
    physiochemical properties of red wine, such as pH, alcohol content and citric acid content, along with wine quality
    rating.

    After you import it, you'll check your working directory to confirm that it is there and then you'll load it into a
    pandas DataFrame.

    :return:
    """
    print('Files from: http://archive.ics.uci.edu/ml/index.php')

    # Assign url of file: url
    url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

    # Save file locally
    urlretrieve(url, 'winequality-red.csv')

    # Read file into a DataFrame and print its head
    df = pd.read_csv('winequality-red.csv', sep=';')
    print(df.head())


def ex_2_red_wine_pd():
    """
    You have just imported a file from the web, saved it locally and loaded it into a DataFrame. If you just wanted to
    load a file from the web into a DataFrame without first saving it locally, you can do that easily using pandas. In
    particular, you can use the function pd.read_csv() with the URL as the first argument and the separator sep as the
    second argument.
    :return:
    """
    # Assign url of file: url
    url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

    # Read file into a DataFrame: df
    df = pd.read_csv(url, sep=';')

    # Print the head of the DataFrame
    print(df.head())

    # Plot first column of df
    pd.DataFrame.hist(df.ix[:, 0:1])
    plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
    plt.ylabel('count')
    plt.show()


def ex_3_red_wine_excel():
    """
    Congrats! You've just loaded a flat file from the web into a DataFrame without first saving it locally using the
    pandas function pd.read_csv(). This function is super cool because it has close relatives that allow you to load
    all types of files, not only flat ones. In this interactive exercise, you'll use pd.read_excel() to import an Excel
    spreadsheet.

    Your job is to use pd.read_excel() to read in all of its sheets, print the sheet names and then print the head of
    the first sheet using its name, not its index.

    Note that the output of pd.read_excel() is a Python dictionary with sheet names as keys and corresponding DataFrames
    as corresponding values.

    :return:
    """
    # Assign url of file: url
    url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

    # Read in all sheets of Excel file: xl
    xl = pd.read_excel(url, sheet_name=None)

    # Print the sheetnames to the shell
    print(xl.keys())

    # Print the head of the first sheet (using its name, NOT its index)
    print(xl['1700'].head())


if __name__ == '__main__':

    # print('\nOutput of lesson_1_files_from_web:')
    # lesson_1_files_from_web()

    # print('\nOutput of ex_1_red_wine:')
    # ex_1_red_wine()

    # print('\nOutput of ex_2_red_wine_pd:')
    # ex_2_red_wine_pd()

    print('\nOutput of ex_3_red_wine_excel:')
    ex_3_red_wine_excel()