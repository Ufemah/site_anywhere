import random


def predict():
    data = open('/home/Ufemah/mysite/static/text/predict_data.txt')
    data = data.readlines()

    r = random.randint(0, len(data)-1)

    pred = data[r]
    return pred


if __name__ == "__main__":
    print(predict())