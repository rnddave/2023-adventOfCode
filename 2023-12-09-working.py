from itertools import pairwise


def read_input_file():
    return [list(map(int, line.split()))
            for line in open("2023-12-09-puzzle-input", "r")]


def predict_value(history):
    return history[-1] + predict_value([right - left
        for left, right in pairwise(history)]) if any(history) else 0


def partOne(histories):
    return sum(map(predict_value, histories))


def partTwo(histories):
    return sum(predict_value(list(reversed(history)))
        for history in histories)


if __name__ == "__main__":
    history_data = read_input_file()
    extrapolatedPartOne = partOne(history_data)
    extrapolatedPartTwo = partTwo(history_data)

    print(f"part_one: {extrapolatedPartOne}")
    print(f"part_two: {extrapolatedPartTwo}")