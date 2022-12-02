import os.path

total_score = 0
total_score_with_updated_strategy = 0

with open(os.path.join(os.path.dirname(__file__), 'data.txt')) as fh:

    for line in fh.readlines():
        line = line.strip()

        # Rock vs Rock - Draw (3 + 1)
        if line == "A X":
            total_score += 4

        # Rock vs Paper - Win for you (6 + 2)
        elif line == "A Y":
            total_score += 8

        # Rock vs Scissors - Loss for you (0 + 3)
        elif line == "A Z":
            total_score += 3

        # Paper vs Rock - Loss for you (0 + 1)
        elif line == "B X":
            total_score += 1

        # Paper vs Paper - Draw (3 + 2)
        elif line == "B Y":
            total_score += 5

        # Paper vs Scissors - Win for you (6 + 3)
        elif line == "B Z":
            total_score += 9

        # Scissors vs Rock - Win for you (6 + 1)
        elif line == "C X":
            total_score += 7

        # Scissors vs Paper - Loss for you (0 + 2)
        elif line == "C Y":
            total_score += 2

        # Scissors vs Scissors - Draw (3 + 3)
        elif line == "C Z":
            total_score += 6

        else:
            print("Wrong input")

print("Your total score was: " + str(total_score))

with open(os.path.join(os.path.dirname(__file__), 'data.txt')) as fh:

    for line in fh.readlines():
        line = line.strip()

        # You need to lose. Rock vs Scissors (0 + 3)
        if line == "A X":
            total_score_with_updated_strategy += 3

        # You need to draw. Rock vs Rock (3 + 1)
        elif line == "A Y":
            total_score_with_updated_strategy += 4

        # You need to win. Rock vs Paper (6 + 2)
        elif line == "A Z":
            total_score_with_updated_strategy += 8

        # You need to lose. Paper vs Rock (0 + 1)
        elif line == "B X":
            total_score_with_updated_strategy += 1

        # You need to draw. Paper vs Paper (3 + 2)
        elif line == "B Y":
            total_score_with_updated_strategy += 5

        # You need to win. Paper vs Scissors (6 + 3)
        elif line == "B Z":
            total_score_with_updated_strategy += 9

        # You need to lose. Scissors vs Paper (0 + 2)
        elif line == "C X":
            total_score_with_updated_strategy += 2

        # You need to draw. Scissors vs Scissors (3 + 3)
        elif line == "C Y":
            total_score_with_updated_strategy += 6

        # You need to win. Scissors vs Rock (6 + 1)
        elif line == "C Z":
            total_score_with_updated_strategy += 7

        else:
            print("Wrong input")

print("With the updated strategy, your total score was: " + str(total_score_with_updated_strategy))
