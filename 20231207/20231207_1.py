import numpy as np
import pandas as pd

# Read the file
# with open("../data/20231207_input.txt", "r") as f:
with open("test.txt", "r") as f:
    data = f.read()

# Get rid of the newline at the end
data = data.strip()

# Split the data into a list
data = data.split("\n")

card_labels = [x.split(" ")[0] for x in data]
card_bid = [int(x.split(" ")[1]) for x in data]

card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

hand_types = ["5", "4", "fulll", "3", "2p", "1p", "hc"]

# Make a dictionary of the card labels and their bids
card_dict = dict(zip(card_labels, card_bid))


def get_hand_type(hand):
    hand_types = ["5", "4", "fh", "3", "2p", "1p", "hc"]

    # If all the cards are the same, it's hand type is "5"
    if len(set(hand)) == 1:
        hand_type = hand_types[0]
    # If there are 4 of the same card, it's hand type is "4"
    elif len(set(hand)) == 2:
        # Check the number of times each card appears
        card_counts = [hand.count(x) for x in set(hand)]
        if 4 in card_counts:
            hand_type = hand_types[1]
        else:
            hand_type = hand_types[2]
    elif len(set(hand)) == 3:
        # Check the number of times each card appears
        card_counts = [hand.count(x) for x in set(hand)]
        if 3 in card_counts:
            hand_type = hand_types[3]
        else:
            hand_type = hand_types[4]
    elif len(set(hand)) == 4:
        hand_type = hand_types[5]
    else:
        hand_type = hand_types[6]
    # If there are 3 of the same card, and the other 2 are the same, it's hand type is "fulll"
    # elif len(set(hand)) == 3:

    return hand_type


def get_hand_ranks(hand, hand_type):
    card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    # If the hand type is "5", then arrange the cards in descending order or card order
    if hand_type == "5":
        hand_ranks = [card_order.index(x[0]) for x in hand]
        hand_length = len(hand_ranks)
        hand_ranks = np.array(hand_ranks)
        # Assign values from 1 to hand_length to the hand ranks in descending order
        # Get indices that would sort hand_ranks
        sorted_indices = sorted(range(len(hand_ranks)), key=lambda i: hand_ranks[i])

        # Create new_hand_ranks based on the sorted indices
        new_hand_ranks = [
            hand_length - sorted_indices.index(i) for i in range(hand_length)
        ]
    elif hand_type == "4":
        hand_ranks = [1] * len(hand)
        # While hand ranks are not unique, compare the two adjacent cards and assign the higher rank
        # to the higher card
        count = 0
        # while len(set(hand_ranks)) != len(hand_ranks):
        for j in range(10):
            print(hand_ranks, count)
            for i in range(len(hand) - 1):
                hand1 = hand[i]
                hand2 = hand[i + 1]
                # Between the two cards, find the index where they are different from each other
                diff_index = [j for j in range(len(hand1)) if hand1[j] != hand2[j]][0]
                # Compare the two cards at the diff_index
                if card_order.index(hand1[diff_index]) > card_order.index(
                    hand2[diff_index]
                ):
                    hand_ranks[i] += 1
                    hand_ranks[i + 1] -= 1
                else:
                    hand_ranks[i + 1] += 1
                    hand_ranks[i] -= 1
            count += 1
            print(hand_ranks, count)

    return new_hand_ranks


test_hand = ["KKKKA", "AAAAQ", "TKTTT"]
test_hand_type = "4"

test_hand_ranks = get_hand_ranks(test_hand, test_hand_type)

print(test_hand_ranks)

"""
# Convert the card_dict to a dataframe
card_df = pd.DataFrame.from_dict(card_dict, orient="index").reset_index()
card_df.columns = ["hand", "bid"]

# Get the hand type for each hand
card_df["hand_type"] = card_df["hand"].apply(lambda x: get_hand_type(x))

# Group by hand type 
"""
