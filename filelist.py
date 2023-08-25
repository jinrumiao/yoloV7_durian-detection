# 90%訓練、10%驗證
import os
import random

img_path = "fruits/images"

fruits = os.listdir(img_path)

train = open("fruits/train.txt", "w")
val = open("fruits/val.txt", "w")

for fruit in fruits:
    files = os.listdir(os.path.join(img_path, fruit))
    ls = [f"./images/{fruit}/{file}" for file in files]
    random.shuffle(ls)

    total = len(ls)
    for i, f in enumerate(ls):
        if i < total * 0.9:
            train.write(f"{f}\n")
        else:
            val.write(f"{f}\n")

train.close()
val.close()
