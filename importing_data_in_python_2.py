import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint as pp
import pandas as pd
from urllib.request import urlretrieve, urlopen, Request
import requests
from bs4 import BeautifulSoup
import json
import re
import tweepy
from api_keys import get_api_key
from twitter import MyStreamListener


pd.options.display.max_columns = 27
pd.options.display.max_colwidth = 280

omdb_api_key, *_ = get_api_key('omdb')
tw_api_key, tw_api_secret, tw_access_token, tw_access_token_secret, _ = get_api_key('twitter')

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


def ex_4_urlopen():
    """
    Performing HTTP requests in Python using urllib
    Now that you know the basics behind HTTP GET requests, it's time to perform some of your own. In this interactive
    exercise, you will ping our very own DataCamp servers to perform a GET request to extract information from our teach
    page, "http://www.datacamp.com/teach/documentation".

    In the next exercise, you'll extract the HTML itself. Right now, however, you are going to package and send the
    request and then catch the response.
    :return:
    """
    # Specify the url
    url = "http://www.datacamp.com/teach/documentation"

    # This packages the request: request
    request = Request(url)

    # Sends the request and catches the response: response
    response = urlopen(request)

    # Print the datatype of response
    print(type(response))

    # Be polite and close the response!
    response.close()


def ex_5_print_html():
    """
    Printing HTTP request results in Python using urllib
    You have just packaged and sent a GET request to "http://www.datacamp.com/teach/documentation" and then caught the
    response. You saw that such a response is a http.client.HTTPResponse object. The question remains: what can you do
    with this response?

    Well, as it came from an HTML page, you could read it to extract the HTML and, in fact, such a
    http.client.HTTPResponse object has an associated read() method. In this exercise, you'll build on your previous
    great work to extract the response and print the HTML.
    :return:
    """
    # Specify the url
    url = "http://www.datacamp.com/teach/documentation"

    # This packages the request
    request = Request(url)

    # Sends the request and catches the response: response
    response = urlopen(request)

    # Extract the response: html
    html = response.read()

    # Print the html
    pp(html)

    # Be polite and close the response!
    response.close()


def ex_6_requests():
    """
    Performing HTTP requests in Python using requests
    Now that you've got your head and hands around making HTTP requests using the urllib package, you're going to figure
    out how to do the same using the higher-level requests library. You'll once again be pinging DataCamp servers for
    their "http://www.datacamp.com/teach/documentation" page.

    Note that unlike in the previous exercises using urllib, you don't have to close the connection when using requests!
    :return:
    """
    # Import package
    # import requests  # -> imported at the top

    # Specify the url: url
    url = 'http://www.datacamp.com/teach/documentation'

    # Packages the request, send the request and catch the response: r
    r = requests.get(url)

    # Extract the response: text
    text = r.text

    # Print the html
    pp(text)


def lesson_2_beautiful_soup():
    """
    Explore BeautifulSoup and some of its methods
    :return:
    """
    url = 'https://www.crummy.com/software/BeautifulSoup'
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'lxml')
    print(soup.prettify())
    print('\nTitle:\n', soup.title)
    print('\nText:\n', soup.get_text())
    print('\nLinks:')
    for link in soup.find_all('a'):
        print(link.get('href'))


def ex_7_parsing_html_bs():
    """
    Parsing HTML with BeautifulSoup
    In this interactive exercise, you'll learn how to use the BeautifulSoup package to parse, prettify and extract
    information from HTML. You'll scrape the data from the webpage of Guido van Rossum, Python's very own Benevolent
    Dictator for Life (https://en.wikipedia.org/wiki/Benevolent_dictator_for_life). In the following exercises, you'll
    prettify the HTML and then extract the text and the hyperlinks.

    The URL of interest is url = 'https://www.python.org/~guido/'.
    :return:
    """
    # Import packages
    # import requests  -> imported above
    # from bs4 import BeautifulSoup  -> imported above

    # Specify url: url
    url = 'https://www.python.org/~guido/'

    # Package the request, send the request and catch the response: r
    r = requests.get(url)

    # Extracts the response as html: html_doc
    html_doc = r.text

    # Create a BeautifulSoup object from the HTML: soup
    soup = BeautifulSoup(html_doc, 'lxml')

    # Prettify the BeautifulSoup object: pretty_soup
    pretty_soup = soup.prettify()

    # Print the response
    pp(pretty_soup)


def ex_8_getting_text_bs():
    """
    Turning a webpage into data using BeautifulSoup: getting the text
    As promised, in the following exercises, you'll learn the basics of extracting information from HTML soup. In this
    exercise, you'll figure out how to extract the text from the BDFL's webpage, along with printing the webpage's
    title.
    :return:
    """
    # Specify url: url
    url = 'https://www.python.org/~guido/'

    # Package the request, send the request and catch the response: r
    r = requests.get(url)

    # Extract the response as html: html_doc
    html_doc = r.text

    # Create a BeautifulSoup object from the HTML: soup
    soup = BeautifulSoup(html_doc, 'lxml')

    # Get the title of Guido's webpage: guido_title
    guido_title = soup.title

    # Print the title of Guido's webpage to the shell
    print(guido_title)

    # Get Guido's text: guido_text
    guido_text = soup.get_text()

    # Print Guido's text to the shell
    print(guido_text)


def ex_9_hyperlinks_bs():
    """
    Turning a webpage into data using BeautifulSoup: getting the hyperlinks
    In this exercise, you'll figure out how to extract the URLs of the hyperlinks from the BDFL's webpage. In the
    process, you'll become close friends with the soup method find_all().
    :return:
    """
    # Specify url
    url = 'https://www.python.org/~guido/'

    # Package the request, send the request and catch the response: r
    r = requests.get(url)

    # Extracts the response as html: html_doc
    html_doc = r.text

    # create a BeautifulSoup object from the HTML: soup
    soup = BeautifulSoup(html_doc, 'lxml')

    # Print the title of Guido's webpage
    print(soup.title)

    # Find all 'a' tags (which define hyperlinks): a_tags
    a_tags = soup.find_all('a')

    # Print the URLs to the shell
    for link in a_tags:
        print(link.get('href'))


# Introduction to APIs and JSONs

def lesson_3_json():
    """
    Loading JSONs in Python
    :return:
    """
    # import json  -> imported at the top
    with open('snakes.json', 'r') as json_file:
        json_data = json.load(json_file)

    print(type(json_data))

    for k, v in json_data.items():
        print(f'{k}: {v}')


def ex_10_json():
    """
    Loading and exploring a JSON
    Now that you know what a JSON is, you'll load one into your Python environment and explore it yourself. Here, you'll
    load the JSON 'a_movie.json' into the variable json_data, which will be a dictionary. You'll then explore the JSON
    contents by printing the key-value pairs of json_data to the shell.
    :return:
    """
    # Load JSON: json_data
    with open("a_movie.json") as json_file:
        json_data = json.load(json_file)

    # Print each key-value pair in json_data
    for k in json_data.keys():
        print(k + ': ', json_data[k])


def lesson_4_api():
    """
    How to use an api
    :return:
    """
    url = f'http://www.omdbapi.com/?t=hackers&apikey={omdb_api_key}'
    r = requests.get(url)
    json_data = r.json()
    for k, v in json_data.items():
        print(f'{k}: {v}')


def ex_11_api_requests():
    """
    API requests
    Now it's your turn to pull some movie data down from the Open Movie Database (OMDB) using their API. The movie
    you'll query the API about is The Social Network. Recall that, in the video, to query the API about the movie
    Hackers, Hugo's query string was 'http://www.omdbapi.com/?t=hackers' and had a single argument t=hackers.

    Note: recently, OMDB has changed their API: you now also have to specify an API key. This means you'll have to add
    another argument to the URL: apikey=xxxxxxxx.
    :return:
    """
    # Assign URL to variable: url
    url = f'http://www.omdbapi.com/?apikey={omdb_api_key}&t=social+network'

    # Package the request, send the request and catch the response: r
    r = requests.get(url)

    # Print the text of the response
    print(r.text)

    # Decode the JSON data into a dictionary: json_data
    json_data = r.json()

    # Print each key-value pair in json_data
    for k in json_data.keys():
        print(k + ': ', json_data[k])


def ex_12_wikipedia_api():
    """
    Checking out the Wikipedia API
    You're doing so well and having so much fun that we're going to throw one more API at you: the Wikipedia API
    (documented here). You'll figure out how to find and extract information from the Wikipedia page for Pizza. What
    gets a bit wild here is that your query will return nested JSONs, that is, JSONs with JSONs, but Python can handle
    that because it will translate them into dictionaries within dictionaries.
    :return:
    """
    # Assign URL to variable: url
    url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

    # Package the request, send the request and catch the response: r
    r = requests.get(url)

    # Decode the JSON data into a dictionary: json_data
    json_data = r.json()

    # Print the Wikipedia page extract
    pizza_extract = json_data['query']['pages']['24768']['extract']
    print(pizza_extract)


def lesson_5_twitter():
    """
    API Authentication
    The package tweepy is great at handling all the Twitter API OAuth Authentication details for you. All you need to
    do is pass it your authentication credentials. In this interactive exercise, we have created some mock
    authentication credentials (if you wanted to replicate this at home, you would need to create a Twitter App as Hugo
    detailed in the video). Your task is to pass these credentials to tweepy's OAuth handler.
    https://apps.twitter.com/

    Streaming tweets
    Now that you have set up your authentication credentials, it is time to stream some tweets! We have already defined
    the tweet stream listener class, MyStreamListener, just as Hugo did in the introductory video. You can find the code
    for the tweet stream listener class here.
    (https://gist.github.com/hugobowne/18f1c0c0709ed1a52dc5bcd462ac69f4)

    Your task is to create the Stream object and to filter tweets according to particular keywords.

    Load and explore your Twitter data
    Now that you've got your Twitter data sitting locally in a text file, it's time to explore it! This is what you'll
    do in the next few interactive exercises. In this exercise, you'll read the Twitter data into a list: tweets_data.
    :return:
    """
    consumer_key = tw_api_key
    consumer_secret = tw_api_secret
    access_token = tw_access_token
    access_token_secret = tw_access_token_secret

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    l = MyStreamListener()
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['clinton', 'trump', 'sanders', 'cruz'])

    # String of path to file: tweets_data_path
    tweets_data_path = 'tweets.txt'

    # Initialize empty list to store tweets: tweets_data
    tweets_data = []

    # Open connection to file
    tweets_file = open(tweets_data_path, "r")

    # Read in tweets and store in list: tweets_data
    for line in tweets_file:
        tweet = json.loads(line)
        tweets_data.append(tweet)

    # Close connection to file
    tweets_file.close()

    # Print the keys of the first tweet dict
    print(tweets_data[0].keys())
    return tweets_data


def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, text)

    if match:
        return True
    return False


def ex_13_twitter_df():
    """
    Twitter data to DataFrame
    Now you have the Twitter data in a list of dictionaries, tweets_data, where each dictionary corresponds to a single
    tweet. Next, you're going to extract the text and language of each tweet. The text in a tweet, t1, is stored as the
    value t1['text']; similarly, the language is stored in t1['lang']. Your task is to build a DataFrame in which each
    row is a tweet and the columns are 'text' and 'lang'.

    A little bit of Twitter text analysis
    Now that you have your DataFrame of tweets set up, you're going to do a bit of text analysis to count how many
    tweets contain the words 'clinton', 'trump', 'sanders' and 'cruz'. In the pre-exercise code, we have defined the
    following function word_in_text(), which will tell you whether the first argument (a word) occurs within the 2nd
    argument (a tweet).

    Plotting your Twitter data
    Now that you have the number of tweets that each candidate was mentioned in, you can plot a bar chart of this data.
    You'll use the statistical data visualization library seaborn, which you may not have seen before, but we'll guide
    you through. You'll first import seaborn as sns. You'll then construct a barplot of the data using sns.barplot,
    passing it two arguments:
    http://seaborn.pydata.org/

    1) a list of labels and
    2) a list containing the variables you wish to plot (clinton, trump and so on.)

    Hopefully, you'll see that Trump was unreasonably represented! We have already run the previous exercise solutions
    in your environment.
    :return:
    """
    tweets_data = lesson_5_twitter()
    # Build DataFrame of tweet texts and languages
    df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

    # Print head of DataFrame
    pp(df.head())

    # Initialize list to store tweet counts
    [clinton, trump, sanders, cruz] = [0, 0, 0, 0]

    # Iterate through df, counting the number of tweets in which
    # each candidate is mentioned
    for index, row in df.iterrows():
        clinton += word_in_text('clinton', row['text'])
        trump += word_in_text('trump', row['text'])
        sanders += word_in_text('sanders', row['text'])
        cruz += word_in_text('cruz', row['text'])

    print(f'Clinton: {clinton}\nTrump: {trump}\nSanders: {sanders}\nCruz: {cruz}')
    # Set seaborn style
    sns.set(color_codes=True)

    # Create a list of labels:cd
    cd = ['clinton', 'trump', 'sanders', 'cruz']

    # Plot histogram
    ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
    ax.set(ylabel="count")
    plt.show()


if __name__ == '__main__':

    # print('\nOutput of lesson_1_files_from_web:')
    # lesson_1_files_from_web()

    # print('\nOutput of ex_1_red_wine:')
    # ex_1_red_wine()

    # print('\nOutput of ex_2_red_wine_pd:')
    # ex_2_red_wine_pd()

    # print('\nOutput of ex_3_red_wine_excel:')
    # ex_3_red_wine_excel()

    # print('\nOutput of ex_4_urlopen:')
    # ex_4_urlopen()

    # print('\nOutput of ex_5_print_html:')
    # ex_5_print_html()

    # print('\nOutput of ex_6_requests:')
    # ex_6_requests()

    # print('\nOutput of lesson_2_beautiful_soup:')
    # lesson_2_beautiful_soup()

    # print('\nOutput of ex_7_parsing_html_bs:')
    # ex_7_parsing_html_bs()

    # print('\nOutput of ex_8_getting_text_bs:')
    # ex_8_getting_text_bs()

    # print('\nOutput of ex_9_hyperlinks_bs:')
    # ex_9_hyperlinks_bs()

    # print('\nOutput of lesson_3_json:')
    # lesson_3_json()

    # print('\nOutput of ex_10_json:')
    # ex_10_json()

    # print('\nOutput of lesson_4_api:')
    # lesson_4_api()

    # print('\nOutput of ex_11_api_requests:')
    # ex_11_api_requests()

    # print('\nOutput of ex_12_wikipedia_api:')
    # ex_12_wikipedia_api()

    # print('\nOutput of lesson_5_twitter:')
    # lesson_5_twitter()

    print('\nOutput of ex_13_twitter:')
    twitter_data = lesson_5_twitter()
    ex_13_twitter_df()
