import matplotlib.pyplot as plt #library used to render and visualize the chart
import random #library that allows us to pseudorandomly select the outcome of a dice roll
from collections import Counter #library used to count the number of duplicates in a list
ypos = []
#this section is the one that determines the settings for the experiment, it might be updated in the future but it does its job well as it is
dice_number = int(input("How many dices do you want to throw every time? :"))
tries = int(input("How many times do you want to roll your dices? (the higher the more accurate, but slower) :"))
faces = int(input("How many faces does each dice have? :"))

#this is the script responsible for rolling the dices, it returns a dictionary containing all the outcomes and how many times they were encountered
def diceroll(dice_number, tries, faces):

    sum_list = []
    for i in range(tries):
        dice_sum = 0
        for dice in range(dice_number):
            dice_sum += random.randint(1, faces)
        sum_list.append(dice_sum)
    result = Counter(sum_list)
    return result

#this script is used to find the most common outcome, knowing this makes the chart more flexible as we can use it to set the height of the chart
def max(list):
    print(list)
    max = 0
    for item in list:
        print("Currently testing ", item[1])
        if item[1] > max:
            max = int(item[1])
            print("Current maximum updated to ", max)
    return max


roll = diceroll(dice_number, tries, faces)
print(roll)
print(roll.items())
print(list(roll.items())[0][0])
height = max(list(roll.items()))
width = dice_number*faces
print(height, width)

for i in range(width):
    try:
        ypos.append(roll[i])
    except:
        ypos.append(0)

plt.plot(range(width), ypos)
plt.axis([0, width, 0, height + height/10])
plt.xlabel("Number rolled")
plt.ylabel("Percentage of times rolled")
plt.show()
