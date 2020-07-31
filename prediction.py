import random
import constants


def predict():
    data = open(constants.prediction_file)
    data = data.readlines()

    r = random.randint(0, len(data)-1)

    pred = data[r]
    return pred


if __name__ == "__main__":
    print(predict())