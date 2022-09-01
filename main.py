import matplotlib.pyplot as plt
import random
from collections import Counter
dice_number = int(input("How many dices do you want to throw every time? :"))
tries = int(input("How many times do you want to roll your dices? (the higher the more accurate, but slower) :"))
faces = int(input("How many faces does each dice have? :"))

def diceroll(dice_number, tries, faces):

    sum_list = []
    for i in range(tries):
        dice_sum = 0
        for dice in range(dice_number):
            dice_sum += random.randint(1, faces)
        sum_list.append(dice_sum)
    result = Counter(sum_list)
    return result

def max(list):
    print(list)
    max = 0
    for item in list:
        print("Currently testing ", item)
        if list[item] > max:
            item = max
            print("Current maximum updated to ", max)
    return max

roll = diceroll(dice_number, tries, faces)
print(roll)
print(roll.items)
print(list(roll.items)[0][0])
height = max(list(roll.items))
width = dice_number*faces
print(height, width)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.axis(0, width, 0, height)
plt.show()
