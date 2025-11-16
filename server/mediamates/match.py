import pandas as pd
import random
import numpy as np

names = [
    "VexiQ_47", "lunaByteX9", "RIFTwave_203", "aZura7Flux", "K1raNova",
    "t3mpoShift", "CrypTiK_91", "HEXaMori_54", "Nyxian4u", "piXelCraze_88",
    "SolsticeXJ2", "Z3phyrLane", "miraQ_Tech17", "JoltR4zer", "N0vaRuneX",
    "qBitTide_56", "VantaL1nk", "AeroFrost_92", "fluxTone0", "R3miXArc77"
]

def findMatchedWomen(men_df, women_df, ratings, new_man_answers, num_sim=10):
    """
    This function will return the most likely compatible women based on a few given
    dataframes for a new male user.  Will use the top N similar users' compatibility
    ratings to find the potentially most compatible women.
    """

    # First need to replace the DF answers with their numerical values
    men_df = men_df.apply(lambda x: x.cat.codes)

    women_df = women_df.apply(lambda x: x.cat.codes)

    # Dataframe of new user
    new_man = pd.DataFrame(
        [new_man_answers],
        columns=men_df.columns,
        index=['m' + str(int(men_df.index[-1][1:]) + 1)]  # Getting the new man's id
    )

    # Categorical answers to the profile questions
    ans = ['A', 'B', 'C', 'D', 'E']

    # Categorizing the answers
    new_man = new_man.apply(
        lambda x: pd.Categorical(x, categories=ans)
    ).apply(
        lambda x: x.cat.codes, axis=1
    )

    # Getting the top N similar users
    sim_men = men_df.corrwith(
        new_man.iloc[0],
        axis=1
    ).sort_values(ascending=False)[:num_sim].index

    # Getting the similar users' ratings
    sim_rate = ratings.T[sim_men]

    # Filling in unseen values with nan for calculation purposes
    sim_rate.replace("unseen", np.nan, inplace=True)

    # The potentially most compatible women for the new man
    most_comp = sim_rate.mean(axis=1).sort_values(ascending=False)

    return most_comp

def findMatchedMen(men_df, women_df, ratings, new_woman_answers, num_sim=10):
    """
    This function will return the most likely compatible men based on a few given
    dataframes for a new female user.  Will use the top N similar users' compatibility
    ratings to find the potentially most compatible women.
    """

    # First need to replace the DF answers with their numerical values
    men_df = men_df.apply(lambda x: x.cat.codes)

    women_df = women_df.apply(lambda x: x.cat.codes)

    # Dataframe of new user
    new_woman = pd.DataFrame(
        [new_woman_answers],
        columns=women_df.columns,
        index=['w' + str(int(women_df.index[-1][1:]) + 1)]  # Getting the new man's id
    )

    # Categorical answers to the profile questions
    ans = ['A', 'B', 'C', 'D', 'E']

    # Categorizing the answers
    new_woman = new_woman.apply(
        lambda x: pd.Categorical(x, categories=ans)
    ).apply(
        lambda x: x.cat.codes, axis=1
    )

    # Getting the top N similar users
    sim_women = women_df.corrwith(
        new_woman.iloc[0],
        axis=1
    ).sort_values(ascending=False)[:num_sim].index

    # Getting the similar users' ratings
    sim_rate = ratings.T[sim_women]

    # Filling in unseen values with nan for calculation purposes
    sim_rate.replace("unseen", np.nan, inplace=True)

    # The potentially most compatible women for the new man
    most_comp = sim_rate.mean(axis=1).sort_values(ascending=False)

    return most_comp

def init_data():
    # Creating a Dataset of men and women
    men = pd.DataFrame()
    women = pd.DataFrame()
    # Number of users
    num = 20
    # Dating profile questions for each
    # TODO: this can be replaced with real data
    #   i.e.
    #       Q1 can be data from Spotify playlist
    #       the answer can be AI generated category letter based on the playlist
    #       A - pop, B - classic, etc.
    qs = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
    # Answers to profile questions
    ans = ['A', 'B', 'C', 'D', 'E']
    for q in qs:
        # Making them categorical for preprocessing later
        men[q] = pd.Categorical(random.choices(ans, k=num), categories=ans)

        women[q] = pd.Categorical(random.choices(ans, k=num), categories=ans)

        # IDs
        men['id'] = ["m" + str(i) for i in range(num)]

        women['id'] = ["w" + str(i) for i in range(num)]
    # Setting index
    men.set_index('id', inplace=True)
    women.set_index('id', inplace=True)

    return men, women, num


def create_women_ratings(men, women, num):
    # Creating match status between users
    ratings = pd.DataFrame(index=men.index, columns=women.index)
    for i in ratings.columns:
        ratings[i] = random.choices([0, 1, "unseen"], k=num)

    return ratings


def create_men_ratings(men, women, num):
    # Creating match status between users
    ratings = pd.DataFrame(index=women.index, columns=men.index)
    for i in ratings.columns:
        ratings[i] = random.choices([0, 1, "unseen"], k=num)

    return ratings

def find_matches():
    ans = ['A', 'B', 'C', 'D', 'E']

    # init fake user data
    # there are 2000 people in the dataset
    men, women, num = init_data()


    #########################
    # found matched women
    #########################

    # init fake ratings for all women
    ratings = create_women_ratings(men, women, num)

    # Randomly picking answers
    new_man_answers = random.choices(ans, k=5)
    # Running the function
    recs = findMatchedWomen(
        men,
        women,
        ratings,
        new_man_answers,
        num_sim=10
    )

    # Finding the top 8 most potentially compatible
    matches = []
    print('Top 8 matched women:')
    for label, value in recs[:8].items():
        print(f"id: {label}, value: {value}, name: {names[int(label[1:])]}")
        matches.append(names[int(label[1:])])

    return matches


def main():

    ans = ['A', 'B', 'C', 'D', 'E']

    # init fake user data
    # there are 2000 people in the dataset
    men, women, num = init_data()


    #########################
    # found matched women
    #########################

    # init fake ratings for all women
    ratings = create_women_ratings(men, women, num)

    # Randomly picking answers
    new_man_answers = random.choices(ans, k=5)
    # Running the function
    recs = findMatchedWomen(
        men,
        women,
        ratings,
        new_man_answers,
        num_sim=10
    )

    # Finding the top 10 most potentially compatible
    print('Top 10 matched women:')
    for label, value in recs[:10].items():
        print(f"id: {label}, value: {value}")



    # #########################
    # # found matched men
    # #########################
    #
    # # init fake ratings for all men
    # ratings = create_men_ratings(men,women, num)
    #
    # # a new woman
    # ans = ['A', 'B', 'C', 'D', 'E']
    # # Randomly picking answers
    # new_women_answers = random.choices(ans, k=5)
    # # Running the function
    # recs = findMatchedMen(
    #     men,
    #     women,
    #     ratings,
    #     new_women_answers,
    #     num_sim=10
    # )
    # # Finding the top 10 most potentially compatible
    # print('Top 10 matched men:')
    # for label, value in recs[:10].items():
    #     print(f"id: {label}, value: {value}")


if __name__ == "__main__":
    main()
