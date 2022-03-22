import matplotlib.pyplot as plt
from random import randint as rand


fig, ax = plt.subplots(10, 10, figsize=(15, 15))

for i in range(10):
    for j in range(10):
        values = [rand(0, 1) for i in range(10)]
        icon_template = [[values[0], values[5], rand(0, 1), values[5], values[0]],
                         [values[1], values[6], rand(0, 1), values[6], values[1]],
                         [values[2], values[7], rand(0, 1), values[7], values[2]],
                         [values[3], values[8], rand(0, 1), values[8], values[3]],
                         [values[4], values[9], rand(0, 1), values[9], values[4]]]
        ax[i, j].imshow(icon_template, cmap='gray')

plt.show()
