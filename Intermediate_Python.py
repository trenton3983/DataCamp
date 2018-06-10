# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint as pp
import pandas as pd


year = [1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2074, 2075, 2076, 2077, 2078, 2079, 2080, 2081, 2082, 2083, 2084, 2085, 2086, 2087, 2088, 2089, 2090, 2091, 2092, 2093, 2094, 2095, 2096, 2097, 2098, 2099, 2100]
pop = [31.889923, 3.600523, 33.333216, 12.420476, 40.301927, 20.434176, 8.199783, 0.708573, 150.448339, 10.392226, 8.078314, 9.119152, 4.552198, 1.639131, 190.010647, 7.322858, 14.326203, 8.390505, 14.131858, 17.696293, 33.390141, 4.369038, 10.238807, 16.284741, 1318.683096, 44.22755, 0.71096, 64.606759, 3.80061, 4.133884, 18.013409, 4.493312, 11.416987, 10.228744, 5.46812, 0.496374, 9.319622, 13.75568, 80.264543, 6.939688, 0.551201, 4.906585, 76.511887, 5.23846, 61.083916, 1.454867, 1.688359, 82.400996, 22.873338, 10.70629, 12.572928, 9.947814, 1.472041, 8.502814, 7.483763, 6.980412, 9.956108, 0.301931, 1110.396331, 223.547, 69.45357, 27.499638, 4.109086, 6.426679, 58.147733, 2.780132, 127.467972, 6.053193, 35.610177, 23.301725, 49.04479, 2.505559, 3.921278, 2.012649, 3.193942, 6.036914, 19.167654, 13.327079, 24.821286, 12.031795, 3.270065, 1.250882, 108.700891, 2.874127, 0.684736, 33.757175, 19.951656, 47.76198, 2.05508, 28.90179, 16.570613, 4.115771, 5.675356, 12.894865, 135.031164, 4.627926, 3.204897, 169.270617, 3.242173, 6.667147, 28.674757, 91.077287, 38.518241, 10.642836, 3.942491, 0.798094, 22.276056, 8.860588, 0.199579, 27.601038, 12.267493, 10.150265, 6.144562, 4.553009, 5.447502, 2.009245, 9.118773, 43.997828, 40.448191, 20.378239, 42.292929, 1.133066, 9.031088, 7.554661, 19.314747, 23.174294, 38.13964, 65.068149, 5.701579, 1.056608, 10.276158, 71.158647, 29.170398, 60.776238, 301.139947, 3.447496, 26.084662, 85.262356, 4.018332, 22.211743, 11.746035, 12.311143]
life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441, 56.728, 65.554, 74.852, 50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 50.43, 80.653, 44.74100000000001, 50.651, 78.553, 72.961, 72.889, 65.152, 46.462, 55.322, 78.782, 48.328, 75.748, 78.273, 76.486, 78.332, 54.791, 72.235, 74.994, 71.33800000000002, 71.878, 51.57899999999999, 58.04, 52.947, 79.313, 80.657, 56.735, 59.448, 79.406, 60.022, 79.483, 70.259, 56.007, 46.38800000000001, 60.916, 70.19800000000001, 82.208, 73.33800000000002, 81.757, 64.69800000000001, 70.65, 70.964, 59.545, 78.885, 80.745, 80.546, 72.567, 82.603, 72.535, 54.11, 67.297, 78.623, 77.58800000000002, 71.993, 42.592, 45.678, 73.952, 59.44300000000001, 48.303, 74.241, 54.467, 64.164, 72.801, 76.195, 66.803, 74.543, 71.164, 42.082, 62.069, 52.90600000000001, 63.785, 79.762, 80.204, 72.899, 56.867, 46.859, 80.196, 75.64, 65.483, 75.53699999999998, 71.752, 71.421, 71.688, 75.563, 78.098, 78.74600000000002, 76.442, 72.476, 46.242, 65.528, 72.777, 63.062, 74.002, 42.56800000000001, 79.972, 74.663, 77.926, 48.159, 49.339, 80.941, 72.396, 58.556, 39.613, 80.884, 81.70100000000002, 74.143, 78.4, 52.517, 70.616, 58.42, 69.819, 73.923, 71.777, 51.542, 79.425, 78.242, 76.384, 73.747, 74.249, 73.422, 62.698, 42.38399999999999, 43.487]
gdp_cap = [974.5803384, 5937.029525999998, 6223.367465, 4797.231267, 12779.37964, 34435.367439999995, 36126.4927, 29796.04834, 1391.253792, 33692.60508, 1441.284873, 3822.137084, 7446.298803, 12569.85177, 9065.800825, 10680.79282, 1217.032994, 430.0706916, 1713.778686, 2042.09524, 36319.23501, 706.016537, 1704.063724, 13171.63885, 4959.114854, 7006.580419, 986.1478792, 277.5518587, 3632.557798, 9645.06142, 1544.750112, 14619.222719999998, 8948.102923, 22833.30851, 35278.41874, 2082.4815670000007, 6025.3747520000015, 6873.262326000001, 5581.180998, 5728.353514, 12154.08975, 641.3695236000002, 690.8055759, 33207.0844, 30470.0167, 13206.48452, 752.7497265, 32170.37442, 1327.60891, 27538.41188, 5186.050003, 942.6542111, 579.2317429999998, 1201.637154, 3548.3308460000007, 39724.97867, 18008.94444, 36180.78919, 2452.210407, 3540.651564, 11605.71449, 4471.061906, 40675.99635, 25523.2771, 28569.7197, 7320.8802620000015, 31656.06806, 4519.461171, 1463.249282, 1593.06548, 23348.139730000006, 47306.98978, 10461.05868, 1569.331442, 414.5073415, 12057.49928, 1044.770126, 759.3499101, 12451.6558, 1042.581557, 1803.151496, 10956.99112, 11977.57496, 3095.7722710000007, 9253.896111, 3820.17523, 823.6856205, 944.0, 4811.060429, 1091.359778, 36797.93332, 25185.00911, 2749.320965, 619.6768923999998, 2013.977305, 49357.19017, 22316.19287, 2605.94758, 9809.185636, 4172.838464, 7408.905561, 3190.481016, 15389.924680000002, 20509.64777, 19328.70901, 7670.122558, 10808.47561, 863.0884639000002, 1598.435089, 21654.83194, 1712.472136, 9786.534714, 862.5407561000002, 47143.17964, 18678.31435, 25768.25759, 926.1410683, 9269.657808, 28821.0637, 3970.095407, 2602.394995, 4513.480643, 33859.74835, 37506.41907, 4184.548089, 28718.27684, 1107.482182, 7458.396326999998, 882.9699437999999, 18008.50924, 7092.923025, 8458.276384, 1056.380121, 33203.26128, 42951.65309, 10611.46299, 11415.80569, 2441.576404, 3025.349798, 2280.769906, 1271.211593, 469.70929810000007]
life_exp1950 = [28.8, 55.23, 43.08, 30.02, 62.48, 69.12, 66.8, 50.94, 37.48, 68.0, 38.22, 40.41, 53.82, 47.62, 50.92, 59.6, 31.98, 39.03, 39.42, 38.52, 68.75, 35.46, 38.09, 54.74, 44.0, 50.64, 40.72, 39.14, 42.11, 57.21, 40.48, 61.21, 59.42, 66.87, 70.78, 34.81, 45.93, 48.36, 41.89, 45.26, 34.48, 35.93, 34.08, 66.55, 67.41, 37.0, 30.0, 67.5, 43.15, 65.86, 42.02, 33.61, 32.5, 37.58, 41.91, 60.96, 64.03, 72.49, 37.37, 37.47, 44.87, 45.32, 66.91, 65.39, 65.94, 58.53, 63.03, 43.16, 42.27, 50.06, 47.45, 55.56, 55.93, 42.14, 38.48, 42.72, 36.68, 36.26, 48.46, 33.68, 40.54, 50.99, 50.79, 42.24, 59.16, 42.87, 31.29, 36.32, 41.72, 36.16, 72.13, 69.39, 42.31, 37.44, 36.32, 72.67, 37.58, 43.44, 55.19, 62.65, 43.9, 47.75, 61.31, 59.82, 64.28, 52.72, 61.05, 40.0, 46.47, 39.88, 37.28, 58.0, 30.33, 60.4, 64.36, 65.57, 32.98, 45.01, 64.94, 57.59, 38.64, 41.41, 71.86, 69.62, 45.88, 58.5, 41.22, 50.85, 38.6, 59.1, 44.6, 43.58, 39.98, 69.18, 68.44, 66.07, 55.09, 40.41, 43.16, 32.55, 42.04, 48.45]
col = ['red', 'green', 'blue', 'blue', 'yellow', 'black', 'green', 'red', 'red', 'green', 'blue', 'yellow', 'green', 'blue', 'yellow', 'green', 'blue', 'blue', 'red', 'blue', 'yellow', 'blue', 'blue', 'yellow', 'red', 'yellow', 'blue', 'blue', 'blue', 'yellow', 'blue', 'green', 'yellow', 'green', 'green', 'blue', 'yellow', 'yellow', 'blue', 'yellow', 'blue', 'blue', 'blue', 'green', 'green', 'blue', 'blue', 'green', 'blue', 'green', 'yellow', 'blue', 'blue', 'yellow', 'yellow', 'red', 'green', 'green', 'red', 'red', 'red', 'red', 'green', 'red', 'green', 'yellow', 'red', 'red', 'blue', 'red', 'red', 'red', 'red', 'blue', 'blue', 'blue', 'blue', 'blue', 'red', 'blue', 'blue', 'blue', 'yellow', 'red', 'green', 'blue', 'blue', 'red', 'blue', 'red', 'green', 'black', 'yellow', 'blue', 'blue', 'green', 'red', 'red', 'yellow', 'yellow', 'yellow', 'red', 'green', 'green', 'yellow', 'blue', 'green', 'blue', 'blue', 'red', 'blue', 'green', 'blue', 'red', 'green', 'green', 'blue', 'blue', 'green', 'red', 'blue', 'blue', 'green', 'green', 'red', 'red', 'blue', 'red', 'blue', 'yellow', 'blue', 'green', 'blue', 'green', 'yellow', 'yellow', 'yellow', 'red', 'red', 'red', 'blue', 'blue']


# matplotlib section
def ex_1():
    # Print the last item from year and pop
    print(year[-1])
    print(pop[-1])

    # Make a line plot: year on the x-axis, pop on the y-axis
    plt.plot(year, pop)

    # Display the plot with plt.show()
    plt.grid()
    plt.show()


def ex_2():
    # Print the last item of gdp_cap and life_exp
    print(gdp_cap[-1])
    print(life_exp[-1])

    # Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
    plt.plot(gdp_cap, life_exp)
    plt.grid()

    # Display the plot
    plt.show()


def ex_3():
    # Change the line plot below to a scatter plot
    plt.scatter(gdp_cap, life_exp)

    # Put the x-axis on a logarithmic scale
    plt.xscale('log')

    # Display the plot
    plt.grid()
    plt.show()


def ex_4():
    # Build Scatter plot
    plt.scatter(pop, life_exp)

    # Show plot
    plt.grid()
    plt.show()


def ex_5():
    # Create histogram of life_exp data
    plt.hist(life_exp)

    # Display histogram
    plt.show()


def ex_6():
    # Create histogram of life_exp data with 5 bins
    plt.hist(life_exp, bins=5)

    # Show and clean up plot
    plt.show()
    plt.clf()

    # Build histogram with 20 bins
    plt.hist(life_exp, bins=20)

    # Show and clean up again
    plt.show()
    plt.clf()


def ex_7():
    # Histogram of life_exp, 15 bins
    plt.hist(life_exp, bins=15)

    # Show and clear plot
    plt.show()
    plt.clf()

    # Histogram of life_exp1950, 15 bins
    plt.hist(life_exp1950, bins=15)

    # Show and clear plot again
    plt.show()
    plt.clf()


def ex_8():
    # Basic scatter plot, log scale
    plt.scatter(gdp_cap, life_exp)
    plt.xscale('log')

    # Strings
    xlab = 'GDP per Capita [in USD]'
    ylab = 'Life Expectancy [in years]'
    title = 'World Development in 2007'

    # Add axis labels
    plt.xlabel(xlab)
    plt.ylabel(ylab)

    # Add title
    plt.title(title)

    # After customizing, display the plot
    plt.show()


def ex_9():
    # Scatter plot
    plt.scatter(gdp_cap, life_exp)

    # Previous customizations
    plt.xscale('log')
    plt.xlabel('GDP per Capita [in USD]')
    plt.ylabel('Life Expectancy [in years]')
    plt.title('World Development in 2007')

    # Definition of tick_val and tick_lab
    tick_val = [1000, 10000, 100000]
    tick_lab = ['1k', '10k', '100k']

    # Adapt the ticks on the x-axis
    plt.xticks(tick_val, tick_lab)

    # After customizing, display the plot
    plt.show()


def ex_10():
    # Store pop as a numpy array: np_pop
    np_pop = np.array(pop)

    # Double np_pop
    np_pop = np_pop * 2

    # Update: set s argument to np_pop
    plt.scatter(gdp_cap, life_exp, s=np_pop)

    # Previous customizations
    plt.xscale('log')
    plt.xlabel('GDP per Capita [in USD]')
    plt.ylabel('Life Expectancy [in years]')
    plt.title('World Development in 2007')
    plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

    # Display the plot
    plt.show()


def ex_11():
    # Specify c and alpha inside plt.scatter()
    plt.scatter(x=gdp_cap, y=life_exp, s=np.array(pop) * 2, c=col, alpha=0.8)

    # Previous customizations
    plt.xscale('log')
    plt.xlabel('GDP per Capita [in USD]')
    plt.ylabel('Life Expectancy [in years]')
    plt.title('World Development in 2007')
    plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

    # Show the plot
    plt.show()


def ex_12():
    # Scatter plot
    plt.scatter(x=gdp_cap, y=life_exp, s=np.array(pop) * 2, c=col, alpha=0.8)

    # Previous customizations
    plt.xscale('log')
    plt.xlabel('GDP per Capita [in USD]')
    plt.ylabel('Life Expectancy [in years]')
    plt.title('World Development in 2007')
    plt.xticks([1000, 10000, 100000], ['1k', '10k', '100k'])

    # Additional customizations
    plt.text(1550, 71, 'India')
    plt.text(5700, 80, 'China')

    # Add grid() call
    plt.grid(True)

    # Show the plot
    plt.show()


# Dictionaries

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']


def ex_13():
    # Get index of 'germany': ind_ger
    ind_ger = countries.index('germany')

    # Use ind_ger to print out capital of Germany
    print(capitals[ind_ger])


def ex_14():
    # From string in countries and capitals, create dictionary europe
    europe = dict(zip(countries, capitals))

    # Print europe
    print(europe)
    return europe


def ex_15():
    europe = ex_14()

    # Print out the keys in europe
    print(europe.keys())

    # Print out value that belongs to key 'norway'
    print(europe['norway'])


def ex_16():
    europe = ex_14()

    # Add italy to europe
    europe['italy'] = 'rome'

    # Print out italy in europe
    print('italy' in europe)

    # Add poland to europe
    europe['poland'] = 'warsaw'

    # Print europe
    print(europe)


def ex_17():
    # Definition of dictionary
    europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'brinn',
              'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw',
              'australia': 'vienna'}

    # Update capital of germany
    europe['germany'] = 'berlin'

    # Remove australia
    del(europe['australia'])

    # Print europe
    print(europe)


def ex_18():
    # Dictionary of dictionaries
    europe = {'spain': {'capital': 'madrid', 'population': 46.77},
              'france': {'capital': 'paris', 'population': 66.03},
              'germany': {'capital': 'berlin', 'population': 80.62},
              'norway': {'capital': 'oslo', 'population': 5.084}}

    # Print out the capital of France
    print(europe['france']['capital'])

    # Create sub-dictionary data
    data = {'capital': 'rome', 'population': 59.83}

    # Add data to europe under key 'italy'
    europe['italy'] = data

    # Print europe
    pp(europe)


def ex_19():
    # Pre-defined lists
    names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
    dr = [True, False, False, False, True, True, True]
    cpc = [809, 731, 588, 18, 200, 70, 45]

    # Create dictionary my_dict with three key:value pairs: my_dict
    my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

    # Build a DataFrame cars from my_dict: cars
    cars = pd.DataFrame(my_dict)

    # Print cars
    print(cars)


ex_19()
