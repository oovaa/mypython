from jovian.pythondsa import evaluate_test_case


def locate(cards, target):
    position = 0
    while True:
        if cards[position] == target:
            return position
        position += 1
        if position == len(cards):
            return -1


cards = [14, 12, 9, 7, 5, 3, 1]
target = 1
print(locate(cards, target))
