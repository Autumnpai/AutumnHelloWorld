prices = [24, 16, 28, 90, 12]
# for itemtest in prices:
#    print(itemtest)
total = 0
for price in prices:
    total = total + price
print(f"Total is ${total}")

# numbers = ["X"*5, "X"*2, "X"*5, "X"*2, "X"*2]
# for item in numbers:
#    print(item)
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    quantity = ""
    for each in range(number):
        quantity = quantity + "x"
    print(quantity)

numbers = [2, 2, 2, 2, 6]
for number in numbers:
    quantity = ""
    for each in range(number):
        quantity = quantity + "x"
    print(quantity)

nums = [86, 59, 1, 9, 8, 31, 84, 2]
lgst_num = nums[0]
for num in nums:
    if num > lgst_num:
        lgst_num = num
print(lgst_num)

mymt = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for apx in mymt:
    for apy in apx:
        print(apy)

nums = [3, 5, 7, 8, 3, 4, 8, 0, 9, 7]
for num in nums:
    if nums.count(num) > 1:
        nums.remove(num)
print(nums)

nums2 = [3, 5, 7, 8, 3, 4, 8, 0, 9, 7]
unique = []
for num2 in nums2:
    if num2 not in unique:
        unique.append(num2)
print(unique)
# print(nums.index(9))

Ph_number = input("Phone: ")
numtochar_dic = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six"
}
Pho_char = ""
for num in Ph_number:
    Pho_char = Pho_char + numtochar_dic.get(num, '!') + " "
print(Pho_char)



def emoji_fun(message):
    words = message.split(" ")
    emojis = {
        ":)": "🙂",
        ":(": "☹"
    }
    output = ""
    for word in words:
        output = output + emojis.get(word, word) + " "
    return output


message_inp = input("> ")
print(emoji_fun(message_inp))


class Person:
    def __init__(self, first_name, last_name):
        self.fnm = first_name
        self.lnm = last_name

    def talk(self):
        print(f"Hi, I am {self.fnm} {self.lnm}.")


person_no1 = Person('Autumn', 'Pai')
person_no2 = Person("Jiaojiao", "Quan")
print(person_no1.fnm, person_no1.lnm)
print(person_no2.fnm, person_no2.lnm)
person_no1.talk()
person_no2.talk()

from utils import find_max

print(find_max((14, 6, 17, 84, 2, 51)))


import random


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())
