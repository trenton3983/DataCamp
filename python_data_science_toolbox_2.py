# Using Iterators in Python

# Here, you'll learn all about iterators and iterables, which you have already worked with before when writing for
# loops! You'll learn about some very useful functions that will allow you to effectively work with iterators and
# finish the chapter with a use case that is pertinent to the world of Data Science - dealing with large amounts of
# data - in this case, data from Twitter that you will load in chunks using iterators!

avengers = ['hawkeye', 'iron man', 'thor', 'quicksliver']
names = ['barton', 'stark', 'odinson', 'maximoff']


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

# List Comprehensions and Generators

# In this chapter, you'll build on your knowledge of iterators and be introduced to list comprehensions, which allow
# you to create complicated lists and lists of lists in one line of code! List comprehensions can dramatically
# simplify your code and make it more efficient, and will become a vital part of your Python Data Science toolbox.
# You'll then learn about generators, which are extremely helpful when working with large sequences of data that you
# may not want to store in memory but instead generate on the fly.

# Bring it all Together!

# This chapter will allow you to apply your newly acquired skills towards wrangling and extracting meaningful
# information from a real-world dataset - the World Bank's World Development Indicators dataset! You'll have the
# chance to write your own functions and list comprehensions as you work with iterators and generators and solidify
# your Python Data Science chops. Enjoy!
