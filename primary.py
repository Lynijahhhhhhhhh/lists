# name: Lynijah Russell
# author: LYNIJAH

# -------------------- Section 1 ------------------------- #
# ------------------ List Creation ----------------------- #

print('# -------------------- Section 1 ------------------------- #')
print('Creating an Empty List' '\n')
# 1. Creating an Empty List
# --------------------------------------------------------
# Instructions
#   1. Create empty lists using the following methods.
#       a. via List Displays
#       b. via the list() function.
#   2. Print the lists.
#
# WRITE CODE BELOW
listOne = []
listTwo = list()
print(listOne)
print(listTwo)
print('\n' 'Creating a Pre-Populated List' '\n')
# 2. Creating a Pre-Populated List
# ------------------------------------------------------------
# Instructions
#   1. Create the following pre-populated lists:
#       a. A list filled with 5 integers.
#       b. A list filled with 5 floats.
#       c. A list filled with 3 boolean values (True / False)
#       d. A list of three animals
#       e. A list with of 3 objects, that are all different data types.
#       f. Convert the string of the name of a star to a list via the list() function.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW
integers = [1, 15, -4, -26, 34]
floats = [1.1,2.2,3.3,4.4,5.5]
boolean=[1==2, 3==4,1==1]
animals=["cat","bunny","goldfish"]
dataType=[11,3.1,3==1]
print(integers)
print(floats)
print(boolean)
print(animals)
print(dataType)


# -------------------- Section 2 ------------------------- #
# ---------------- List Modification --------------------- #
print('\n' '# -------------------- Section 2 ------------------------- #')
print('Accessing and Modifying a List' '\n')
# 1. Accessing and Modifying a List
# ------------------------------------------------------------
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Integers --> Replace the item at position 2 with a new number.
#       b. Floats --> Replace the item at position 4 with a new number.
#       c. Booleans --> Replace the item at position 0 with itself negated. (not)
#       d. Animals --> Replace one of the animals with a new animal.
#       e. Objects --> Replace one of the items within the list with a new one.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW
integers[2] = 44
floats[4]= 4.5
boolean[0]= not boolean [0]
animals[0]= "bobcat"
dataType[1]= 3==1

print(
    f'integers / {integers}' '\n'
    f'floats / {floats}' '\n'
    f'boolean / {boolean}' '\n'
    f'animals / {animals}' '\n'
    f'dataType / {dataType}' '\n'
)
print('\n' 'Append, Insert, and Remove' '\n')
# 2. Accessing and Modifying a List
# ------------------------------------------------------------
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Integers --> Append a new number to the list.
#       b. Floats --> Append a new float to the list.
#       c. Booleans --> Remove one of the items from the list
#       d. Animals --> Insert a new animal at the beginning of the list.
#       e. Objects --> Insert a new object at the middle of the list.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW
integers.append(25)
floats.append(2.5)
boolean.remove(True)
animals.insert(1, "my brother")
dataType.insert((len(dataType)-1)//2,False)
print(
    f'integers / {integers}' '\n'
    f'floats / {floats}' '\n'
    f'boolean / {boolean}' '\n'
    f'animals / {animals}' '\n'
    f'dataType / {dataType}' '\n'
)
print('\n' 'List Concatenation' '\n')
# 3. List Concatenation
# ------------------------------------------------------------
#
# Lists like Strings can Concatenate with other Lists using the + operator. They can also be duplicated by
#   multiplying the list.
#
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Concatenate the lists holding the integers and floats together, and save the result to a new variable.
#       d. Duplicate the list holding animals 3 times, and save the result to a new variable.
#   2. Print the new lists.
#
#   Examples are below for reference
#
# WRITE CODE BELOW

num=integers+floats
animals2=animals*3
print(
    f'num / {num}' '\n'
    f'animals2 / {animals2}' '\n'
)

# -------------------- Section 3 ------------------------- #
# --------------------- Looping -------------------------- #
print('\n' '# -------------------- Section 3 ------------------------- #')
print('Looping' '\n')
# 1. Looping
# ------------------------------------------------------------
# Instructions
#   1. Create a loop that prints out the contents of the two of the lists you have already created, using the
#       methods below.
#       a. via in range()
#       b. via direct access
#
#   An example has been shown below:
#
# WRITE CODE BELOW
print("via in range(len(aniamls))")
for i in range(len(animals)):
    print(animals[i])
print()

print('for integer in intergers ')
for integer in integers:
    print(integers)


# -------------------- Section 4 ------------------------- #
# ------------------ Comprehension ----------------------- #
print('\n' '# -------------------- Section 3 ------------------------- #')
print('Dice - Statistics' '\n')

# 1. Dice - Statistics
# ------------------------------------------------------------
# Preface
#   When we roll a dice, the side it lands on is random. However, since a dice has multiple sides that are equivalent
#       in chance of falling, then we say a side has a 1/6 chance of happening, or 16.7% chance. Lets test to see if
#       that's true!
#
# 1. Create multiple for loops to run 5, 10, 100, and 1000 times.
#   a. Within the loops, roll a dice and append the roll to a list that is keeping track of all the rolls.
# 2. After the loop has finished rolling, print the number of times each face appeared, as well as the rate of
#   rate of appearance.
#
# The beginning of the loop running 5 times has been done for you. Be sure to finish it.
#
# WRITE CODE BELOW
from random import randint

size = 5
rolls = []

for i in range(size):
    pass  # finish the loop

print(f'rolls | {rolls}')
print(f'1\t| total - {rolls.count(1)}\t\t| rate of appearance - {"{:.2%}".format(rolls.count(1) / size)}')
# finish the rest!
