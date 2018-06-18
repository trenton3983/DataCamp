import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint as pp
from pathlib import Path
import pandas as pd
import pickle
from sas7bdat import SAS7BDAT
import h5py
import scipy.io
from sqlalchemy import create_engine


pd.options.display.max_columns = 27

# Introduction to flat files:

# In this chapter, you'll learn how to import data into Python from all types of flat files, a simple and prevalent form
# of data storage. You've previously learned how to use NumPy and pandas - you will learn how to use these packages to
# import flat files, as well as how to customize your imports.


def ex_1():
    # Open a file: file
    moby_dick = Path(__file__).parents[0].joinpath('data/moby_dick.txt')
    print(moby_dick)
    file = open(moby_dick, mode='r')

    # Print it
    print(file.read())

    # Check whether file is closed
    print(file.closed)

    # Close file
    file.close()

    # Check whether file is closed
    print(file.closed)


def ex_2():
    # Read & print the first 3 lines
    moby_dick = Path(__file__).parents[0].joinpath('data/moby_dick.txt')
    with open(moby_dick) as file:
        print(file.readline())
        print(file.readline())
        print(file.readline())


def lesson_1():
    # numpy arrays are for data of single datatypes
    # data is from https://pjreddie.com/projects/mnist-in-csv/
    digits_datacamp = Path(__file__).parents[0].joinpath('data/digits_datacamp.csv')
    filename = digits_datacamp
    data = np.loadtxt(filename, delimiter=',', skiprows=0, usecols=None)  # provide a list to usecols e.g. [0, 2]

    print(data[0:2, :])


def ex_3():
    """
    Using NumPy to import flat files
    In this exercise, you're now going to load the MNIST digit recognition dataset using the numpy function loadtxt()
    and see just how easy it can be:

    The first argument will be the filename.
    The second will be the delimiter which, in this case, is a comma.
    You can find more information about the MNIST dataset here (http://yann.lecun.com/exdb/mnist/) on the webpage of
    Yann LeCun, who is currently Director of AI Research at Facebook and Founding Director of the NYU Center for Data
    Science, among many other things.
    :return:
    """
    print('MNIST information at: '
          'http://yann.lecun.com/exdb/mnist/')

    # Assign filename to variable: file
    file = Path(__file__).parents[0].joinpath('data/digits_datacamp.csv')

    # Load file as array: digits
    digits = np.loadtxt(file, delimiter=',')

    # Print datatype of digits
    print(type(digits))

    # Select and reshape a row
    im = digits[21, 1:]
    im_sq = np.reshape(im, (28, 28))

    # Plot reshaped data (matplotlib.pyplot already loaded as plt)
    plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
    plt.show()


def ex_4():
    """
    Customizing your NumPy import
    What if there are rows, such as a header, that you don't want to import? What if your file has a delimiter other
    than a comma? What if you only wish to import particular columns?

    There are a number of arguments that np.loadtxt() takes that you'll find useful: delimiter changes the delimiter
    that loadtxt() is expecting, for example, you can use ',' and '\t' for comma-delimited and tab-delimited
    respectively; skiprows allows you to specify how many rows (not indices) you wish to skip; usecols takes a list of
    the indices of the columns you wish to keep.

    The file that you'll be importing, digits_header.txt,

    has a header
    is tab-delimited.
    :return:
    """
    # Assign the filename: file
    file = Path(__file__).parents[0].joinpath('data/digits_header.txt')

    # Load the data: data
    data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0, 2])

    # Print data
    pp(data, compact=True)


def ex_5():
    """
    The file seaslug.txt
        * has a text header, consisting of strings
        * is tab-delimited.
    These data consists of percentage of sea slug larvae that had metamorphosed in a given time period. Read more here.

    Due to the header, if you tried to import it as-is using np.loadtxt(), Python would throw you a ValueError and tell
    you that it could not convert string to float. There are two ways to deal with this: firstly, you can set the data
    type argument dtype equal to str (for string).

    Alternatively, you can skip the first row as we have seen before, using the skiprows argument.
    :return:
    """

    # Assign filename: file
    file = Path(__file__).parents[0].joinpath('data/seaslug.txt')

    # Import file: data
    data = np.loadtxt(file, delimiter='\t', dtype=str)

    # Print the first element of data
    print(data[0:3])

    # Import data as floats and skip the first row: data_float
    data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

    # Print the 10th element of data_float
    print(data_float[9])

    # Plot a scatterplot of the data
    plt.scatter(data_float[:, 0], data_float[:, 1])
    plt.xlabel('time (min.)')
    plt.ylabel('percentage of larvae')
    plt.show()


def ex_6():
    """
    Working with mixed datatypes (1)
    Much of the time you will need to import datasets which have different datatypes in different columns; one column
    may contain strings and another floats, for example. The function np.loadtxt() will freak at this. There is another
    function, np.genfromtxt(), which can handle such structures. If we pass dtype=None to it, it will figure out what
    types each column should be.

    Import 'titanic.csv' using the function np.genfromtxt() as follows:

    data = np.genfromtxt('titanic.csv', delimiter=',', names=True, dtype=None)

    Here, the first argument is the filename, the second specifies the delimiter , and the third argument names tells us
    there is a header. Because the data are of different types, data is an object called a structured array
    (https://docs.scipy.org/doc/numpy/user/basics.rec.html). Because numpy arrays have to contain elements that are all
    the same type, the structured array solves this by being a 1D array, where each element of the array is a row of the
    flat file imported. You can test this by checking out the array's shape in the shell by executing np.shape(data).

    Accessing rows and columns of structured arrays is super-intuitive: to get the ith row, merely execute data[i] and
    to get the column with name 'Fare', execute data['Fare'].

    Print the entire column with name Survived to the shell. What are the last 4 values of this column?
    :return:
    """
    file = Path(__file__).parents[0].joinpath('data/titanic.csv')
    data = np.genfromtxt(file, delimiter=',', names=True, dtype=None, encoding=None)
    print(data[0:3])
    print(type(data[0][0]))
    print(type(data[0][3]))
    print('Shape: ', np.shape(data))
    print(data['Fare'])
    print(data['Survived'])


def ex_7():
    """
    You have just used np.genfromtxt() to import data containing mixed datatypes. There is also another function
    np.recfromcsv() that behaves similarly to np.genfromtxt(), except that its default dtype is None. In this exercise,
    you'll practice using this to achieve the same result.
    :return:
    """
    file = Path(__file__).parents[0].joinpath('data/titanic.csv')
    d = np.recfromcsv(file, encoding=None)
    print(d[:3])


def ex_8():
    """
    Customizing your pandas import
    The pandas package is also great at dealing with many of the issues you will encounter when importing data as a data
    scientist, such as comments occurring in flat files, empty lines and missing values. Note that missing values are
    also commonly referred to as NA or NaN. To wrap up this chapter, you're now going to import a slightly corrupted
    copy of the Titanic dataset titanic_corrupt.txt, which

    contains comments after the character '#'
    is tab-delimited.

    Complete the sep (the pandas version of delim), comment and na_values arguments of pd.read_csv(). comment takes
    characters that comments occur after in the file, which in this case is '#'. na_values takes a list of strings to
    recognize as NA/NaN, in this case the string 'Nothing'.
    :return:
    """
    file = Path(__file__).parents[0].joinpath('data/titanic_corrupt.txt')
    # Import file: data
    data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')

    # Print the head of the DataFrame
    print(data.head())

    # Plot 'Age' variable in a histogram
    pd.DataFrame.hist(data[['Age']])
    plt.xlabel('Age (years)')
    plt.ylabel('count')
    plt.show()


def lesson_2():
    """
    Importing Excel Spreadsheets and List Sheets
    Whether you like it or not, any working data scientist will need to deal with Excel spreadsheets at some point in
    time. You won't always want to do so in Excel, however!

    Here, you'll learn how to use pandas to import Excel spreadsheets and how to list the names of the sheets in any
    loaded .xlsx file.

    Recall from the video that, given an Excel file imported into a variable spreadsheet, you can retrieve a list of
    the sheet names using the attribute spreadsheet.sheet_names.

    Specifically, you'll be loading and checking out the spreadsheet 'battledeath.xlsx', modified from the Peace
    Research Institute Oslo's (PRIO) dataset
    (https://www.prio.org/Data/Armed-Conflict/Battle-Deaths/The-Battle-Deaths-Dataset-version-30/).
    This data contains age-adjusted mortality rates due to war in various countries over several years.
    """
    file = Path(__file__).parents[0].joinpath('data/battledeath.xlsx')
    data = pd.ExcelFile(file)
    print(data.sheet_names)
    df1 = data.parse(0)
    print(df1.head())
    df2 = data.parse('2004')
    print(df2.head())


def pickle_dict(dict_to_pickle, file_name):
    """
    Pickle the dict
    :param dict_to_pickle: a dict
    :param file_name: str
    """
    outfile = open(file_name, 'wb')
    pickle.dump(dict_to_pickle, outfile)
    outfile.close()


def ex_9():
    """
    Loading a pickled file
    There are a number of datatypes that cannot be saved easily to flat files, such as lists and dictionaries. If you
    want your files to be human readable, you may want to save them as text files in a clever manner. JSONs, which you
    will see in a later chapter, are appropriate for Python dictionaries.

    However, if you merely want to be able to import them into Python, you can serialize
    (https://en.wikipedia.org/wiki/Serialization) them. All this means is converting the object into a sequence of
    bytes, or a bytestream.

    In this exercise, you'll import the pickle package, open a previously pickled data structure from a file and
    load it.
    :return:
    """
    print('Searialize: https://en.wikipedia.org/wiki/Serialization')

    # Open pickle file and load data: d
    with open('data.pkl', 'rb') as file:
        d = pickle.load(file)

    # Print d
    print(d)

    # Print datatype of d
    print(type(d))


def ex_10():
    """
    Customizing your spreadsheet import
    Here, you'll parse your spreadsheets and use additional arguments to skip rows, rename columns and select only
    particular columns.

    The spreadsheet 'battledeath.xlsx' is already loaded as xl.

    As before, you'll use the method parse(). This time, however, you'll add the additional arguments skiprows, names
    and parse_cols. These skip rows, name the columns and designate which columns to parse, respectively. All these a
    rguments can be assigned to lists containing the specific row numbers, strings and column numbers, as appropriate.

    Parse the first sheet by index. In doing so, skip the first row of data and name the columns 'Country' and 'AAM due
    to War (2002)' using the argument names. The values passed to skiprows and names all need to be of type list.

    Parse the second sheet by index. In doing so, parse only the first column with the parse_cols parameter, skip the
    first row and rename the column 'Country'. The argument passed to parse_cols also needs to be of type list.
    :return:
    """
    file = Path(__file__).parents[0].joinpath('data/battledeath.xlsx')
    xl = pd.ExcelFile(file)

    # Parse the first sheet and rename the columns: df1
    df1 = xl.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

    # Print the head of the DataFrame df1
    print(df1.head())

    # Parse the first column of the second sheet and rename the column: df2
    df2 = xl.parse(1, usecols=[0], skiprows=[0], names=['Country'])

    # Print the head of the DataFrame df2
    print(df2.head())


def ex_11():
    """
    Importing SAS files
    In this exercise, you'll figure out how to import a SAS file as a DataFrame using SAS7BDAT and pandas. The file
    'sales.sas7bdat' is already in your working directory and both pandas and matplotlib.pyplot have already been
    imported as follows:

    import pandas as pd
    import matplotlib.pyplot as plt

    The data are adapted from the website of the undergraduate text book Principles of Economics by Hill, Griffiths
    and Lim.
    :return:
    """
    # from sas7bdat import SAS7BDAT -> at the top with the imports

    # Save file to a DataFrame: df_sas
    with SAS7BDAT('sales.sas7bdat') as file:
        df_sas = file.to_data_frame()

    # Print head of DataFrame
    print(df_sas.head())

    # Plot histogram of DataFrame features (pandas and pyplot already imported)
    pd.DataFrame.hist(df_sas[['P']])
    plt.ylabel('count')
    plt.show()


def ex_12():
    """
    Here, you'll gain expertise in importing Stata files as DataFrames using the pd.read_stata() function from pandas.
    The last exercise's file, 'disarea.dta', is still in your working directory.
    :return:
    """
    file = Path(__file__).parents[0].joinpath('data/disarea.dta')
    # Load Stata file into a pandas DataFrame: df
    df = pd.read_stata(file)

    # Print the head of the DataFrame df
    print(df.head())

    # Plot histogram of one column of the DataFrame
    pd.DataFrame.hist(df[['disa10']])
    plt.xlabel('Extent of disease')
    plt.ylabel('Number of coutries')
    plt.show()


def lesson_3():
    """
    HDF5 - hierarchical data format version 5
    Using h5py to import HDF5 files
    The file 'LIGO_data.hdf5' is already in your working directory. In this exercise, you'll import it using the h5py
    library. You'll also print out its datatype to confirm you have imported it correctly. You'll then study the
    structure of the file in order to see precisely what HDF groups it contains.

    https://losc.ligo.org/events/GW150914/
    https://losc.ligo.org/s/events/GW150914/GW150914_tutorial.html

    You can find the LIGO data plus loads of documentation and tutorials here. There is also a great tutorial on Signal
    Processing with the data here.
    :return:
    """
    print('https://losc.ligo.org/events/GW150914/')
    print('https://losc.ligo.org/s/events/GW150914/GW150914_tutorial.html')

    file = Path(__file__).parents[0].joinpath('data/LIGO_data.hdf5')
    data = h5py.File(file, 'r')
    print(type(data))

    # Structure
    for key in data.keys():
        print('Key: ', key)

    print('\nMeta:')
    print(type(data['meta']))
    for key in data['meta'].keys():
        print('Key: ', key)

    print('\nDescription:\n', data['meta']['Description'].value, '\nDetector:\n', data['meta']['Detector'].value)

    print('\nStrain:\n', data['strain'])
    for key in data['strain'].keys():
        print('Key: ', key)

    strain = data['strain']['Strain'].value
    print('\nStrain Value:\n', strain)

    # Set number of time points to sample: num_samples
    num_samples = 10000

    # Set time vector
    time = np.arange(0, 1, 1 / num_samples)

    # Plot data
    plt.plot(time, strain[:num_samples])
    plt.xlabel('GPS Time (s)')
    plt.ylabel('strain')
    plt.show()


def lesson_4_matlab_files():
    """
    keys = MATLAB variable names
    values = objects assigned to variables
    The structure of .mat in Python
    Here, you'll discover what is in the MATLAB dictionary that you loaded in the previous exercise.

    The file 'albeck_gene_expression.mat' is already loaded into the variable mat. The following libraries have already
    been imported as follows:

    import scipy.io
    import matplotlib.pyplot as plt
    import numpy as np

    Once again, this file contains gene expression data from the Albeck Lab at UCDavis.
    :return:
    """
    print('Data and Documentation: https://www.mcb.ucdavis.edu/faculty-labs/albeck/workshop.htm')

    # import scipy.io -> at the top
    file = Path(__file__).parents[0].joinpath('data/albeck_gene_expression.mat')
    mat = scipy.io.loadmat(file)
    print(type(mat), '\n')

    # Print the keys of the MATLAB dictionary
    print('Keys:\n', mat.keys())

    # Print the type of the value corresponding to the key 'CYratioCyt'
    print('\nType:', type(mat['CYratioCyt']))

    # Print the shape of the value corresponding to the key 'CYratioCyt'
    print('\nShape:', np.shape(mat['CYratioCyt']))

    # Subset the array and plot it
    data = mat['CYratioCyt'][25, 5:]
    fig = plt.figure()
    plt.plot(data)
    plt.xlabel('time (min.)')
    plt.ylabel('normalized fluorescence (measure of expression)')
    plt.show()


# Introduction to Relational Databases

def lesson_5_sql():
    """
    Creating a database engine
    Here, you're going to fire up your very first SQL engine. You'll create an engine to connect to the SQLite database
    'Chinook.sqlite', which is in your working directory. Remember that to create an engine to connect to
    'Northwind.sqlite', Hugo executed the command

    engine = create_engine('sqlite:///Northwind.sqlite')
    Here, 'sqlite:///Northwind.sqlite' is called the connection string to the SQLite database Northwind.sqlite. A little
    bit of background on the Chinook database: the Chinook database (https://archive.codeplex.com/?p=chinookdatabase)
    contains information about a semi-fictional digital media store in which media data is real and customer, employee
    and sales data has been manually created.

    Workflow:
    * Import packages and functions
    * Create the database engine
    * Connect to the engine
    * Query the database
    * Save query results to a DataFrame
    * Close the connection
    :return:
    """
    print('Chinook Database: https://archive.codeplex.com/?p=chinookdatabase')
    # from sqlalchemy import create_engine -> imports at top
    # engine = create_engine('sqlite:///Northwind.db3')  # http://nucleonsoftware.com/download/SQLiteNorthwind.zip
    engine = create_engine('sqlite:///Chinook.sqlite')

    print('\nTable Names:')
    table_names = engine.table_names()
    print(table_names)

    print('\nCreate Connection with context manager:')
    with engine.connect() as con:  # replaces con = engine.connect() & no longer requires con.close()

        print('\nQuerying:')
        # rs = con.execute('SELECT * FROM Orders')  # if using Northwind.db3
        # rs = con.execute('SELECT * FROM Album')  # if using Chinook.sqlite
        # rs = con.execute('SELECT LastName, Title FROM Employee')  # if using Chinook.sqlite
        # print('Filter using WHERE:')
        # rs = con.execute('SELECT * FROM Employee WHERE EmployeeId >= 6')  # if using Chinook.sqlite
        print('Order results with ORDER BY:')
        rs = con.execute('SELECT * FROM Employee ORDER BY BirthDate ASC')  # if using Chinook.sqlite

        df = pd.DataFrame(rs.fetchall())
        # df = pd.DataFrame(rs.fetchmany(size=5))  # alternative to previous line
        print(df.head())

        print('\nFix Column Headers:')
        df.columns = rs.keys()
        print(df.head())


def lesson_6_sql_df():
    """
    Pandas and The Hello World of SQL Queries!
    Here, you'll take advantage of the power of pandas to write the results of your SQL query to a DataFrame in one
    swift line of Python code!

    You'll first import pandas and create the SQLite 'Chinook.sqlite' engine. Then you'll query the database to select
    all records from the Album table.

    Recall that to select all records from the Orders table in the Northwind database, Hugo executed the following
    command:

    df = pd.read_sql_query("SELECT * FROM Orders", engine)

    :return:
    """
    # from sqlalchemy import create_engine -> imports at top

    # Create engine: engine
    engine = create_engine('sqlite:///Chinook.sqlite')

    # Execute query and store records in DataFrame: df
    df = pd.read_sql_query("SELECT * FROM Album", engine)
    print('\nDataFrame - Album:\n', df.head())
    df2 = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate ASC', engine)
    print('\nDataFrame 2 - Employee:\n', df2)

    # Print head of DataFrame
    print(df.head())

    # Open engine in context manager
    # Perform query and save results to DataFrame: df1
    with engine.connect() as con:
        rs = con.execute("SELECT * FROM Album")
        df1 = pd.DataFrame(rs.fetchall())
        df1.columns = rs.keys()

    # Confirm that both methods yield the same result: does df = df1 ?
    print('\nDoes the Pandas DF query == the query produced by the context manager?: ', df.equals(df1))


if __name__ == '__main__':

    # print('\nOutput of ex_1:')
    # ex_1()
    #
    # print('\nOutput of ex_2:')
    # ex_2()
    #
    # print('\nOutput of lesson_1:')
    # lesson_1()
    #
    # print('\nOutput of ex_3:')
    # ex_3()
    #
    # print('\nOutput of ex_4:')
    # ex_4()

    # print('\nOutput of ex_5:')
    # ex_5()

    # print('\nOutput of ex_6:')
    # ex_6()

    # print('\nOutput of ex_7:')
    # ex_7()

    # print('\nOutput of ex_8:')
    # ex_8()

    # print('\nOutput of lesson_2 - Importing Excel Spreadsheets and List Sheets:')
    # lesson_2()

    # print('\nOutput of pickle_dict:')
    # pickle_dict({'June': '69.4', 'Mar': '84.4', 'Aug': '85', 'Airline': '8'}, 'data.pkl')

    # print('\nOutput of ex_9:')
    # ex_9()

    # print('\nOutput of ex_10:')
    # ex_10()

    # print('\nOutput of ex_11 - Importing SAS files:')
    # ex_11()

    # print('\nOutput of ex_12 - Importing Stata files:')
    # ex_12()

    # print('\nOutput of lesson_3 - Using h5py to import HDF5 files - LIGO Data:')
    # lesson_3()

    # print('\nOutput of lesson_4_matlab_files - Working with MATLAB files:')
    # lesson_4_matlab_files()

    # print('\nOutput of lesson_5_sql - Working with SQL:')
    # lesson_5_sql()

    print('\nOutput of lesson_6_sql_df - Working with SQL:')
    lesson_6_sql_df()
