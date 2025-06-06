from preprocess import preprocess_images
from split_data import split_dataset
from utils import load_dataset
from cnn import ShrimpleCNN

import numpy as np


def main():
    preprocess_images()
    split_dataset()
    X_train, y_train, X_test, y_test = load_dataset()

    cnn = ShrimpleCNN()
    cnn.train(X_train, y_train, epochs=100)
    y_pred = cnn.predict(X_test)
    accuracy: np.float64 = np.mean(y_pred == np.array(y_test)) * 100
    print(f"[ ACCURACY ] {accuracy:.4f}%")


if __name__ == "__main__":
    main()
