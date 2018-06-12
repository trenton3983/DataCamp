import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint as pp


def coin_toss():
    np.random.seed(123)

    # np.random.rand()  # float between 0 and 1

    coin = np.random.randint(0, 2)
    print(coin)
    if coin == 0:
        print('Heads')
    else:
        print('Tails')


print('\nOutput from the function coin_toss:')
coin_toss()


def steps():
    np.random.seed(123)

    # Starting step
    step = 50

    # Roll the dice
    dice = np.random.randint(1, 7)

    # Finish the control construct
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step += 1
    else:
        step = step + np.random.randint(1, 7)

    # Print out dice and step
    print(dice)
    print(step)


print('\nOutput from the function steps:')
steps()


def random_walk_fun():
    np.random.seed(123)

    # Initialize random_walk
    random_walk = [0]

    # Complete the ___
    for x in range(100):
        # Set step: last element in random_walk
        step = random_walk[-1]

        # Roll the dice
        dice = np.random.randint(1, 7)

        # Determine next step
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        # append next_step to random_walk
        random_walk.append(step)

    # Print random_walk
    print(random_walk)

    # Plot random_walk
    plt.plot(random_walk)

    # Show the plot
    plt.show()


print('\nOutput from the function random_walk_fun:')
random_walk_fun()


def mult_random_walk_fun():
    np.random.seed(123)

    # Initialize all_walks
    all_walks = []

    # Simulate random walk some number of times
    random_walks = 500
    for i in range(random_walks):

        # Code from before
        random_walk = [0]
        for x in range(100):
            step = random_walk[-1]
            dice = np.random.randint(1, 7)

            if dice <= 2:
                step = max(0, step - 1)
            elif dice <= 5:
                step = step + 1
            else:
                step = step + np.random.randint(1, 7)

            # Implement Clumsiness
            if np.random.rand() <= 0.001:
                step = 0

            random_walk.append(step)

        # Append random_walk to all_walks
        all_walks.append(random_walk)

    # Print all_walks
    print('All Walks')
    pp(all_walks, compact=True)

    # Convert all_walks to Numpy array: np_aw
    np_aw = np.array(all_walks)
    print('\nNP Array All Walks')
    pp(np_aw, compact=True)

    # Plot np_aw and show
    plt.plot(np_aw)
    plt.savefig('np_aw.png')
    plt.show()

    # Clear the figure
    plt.clf()

    # Transpose np_aw: np_aw_t
    np_aw_t = np.transpose(np_aw)
    print('\nNP Array All Walks Transposed')
    pp(np_aw_t, compact=True)

    # Plot np_aw_t and show
    plt.plot(np_aw_t)
    plt.savefig('np_aw_t.png')
    plt.show()
    plt.clf()

    # Select last row from np_aw_t: ends
    ends = np.array(np_aw_t[-1])

    # Plot histogram of ends, display plot
    plt.hist(ends)
    plt.savefig('np_aw_t_last_hist.png')
    plt.show()

    # Calculate odds of reaching top of empire state building
    odds = (len(ends[ends >= 60])/random_walks)*100
    print(f'\nOdds of reaching the top of the Empire State Building based upon the results of {random_walks} walks is '
          f'{odds}%')


print('\nOutput from the function mult_random_walk_fun:')
mult_random_walk_fun()
