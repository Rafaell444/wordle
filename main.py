import random

print("""_________________________________________________________________________________________________

        წარმოგიდგენთ თამაშის რეპლიკას - WORDLE.
_________________________________________________________________________________________________
        Rules: 
        
        გამოცნობის გასაადვილებლად სისტემას გამოაქვს ფერები:  მწვანე - სწორ პოზიციაზე მყოფი ასო,
                                                             ყვითელი - არასწორ პოზიციაზე,
                                                             ნაცრისფერი - არარსებული ასო.
                                                             _________________________________________""")

print("""
გაქვთ 6 ცდა იმისთვის რომ გამოიცნოთ 5 ასოიანი სიტყვა

1]|_|_|_|_|_|
2]|_|_|_|_|_|
3]|_|_|_|_|_|
4]|_|_|_|_|_|
5]|_|_|_|_|_|
6]|_|_|_|_|_|
""")

with open("Ka2.txt", "r") as f:
    wholetext = f.read()
    words = list(map(str, wholetext.split()))

word_to_guess = random.choice(words)
print(word_to_guess)

temp = 0
while temp != 6:
    inp = input("შეიყვანეთ სიტყვა: ")
    temp += 1

    # indexing
    zero = inp[0]
    first = inp[1]
    second = inp[2]
    third = inp[3]
    fourth = inp[4]

    sia = [zero, first, second, third, fourth]
    notneeded = []

    for each2 in word_to_guess:
        for each3 in sia:
            if each2 == each3:
                print(each3, "არის მწვანე")

    if len(inp) <= 5:
        for i in inp:
            for letter in word_to_guess:
                if i == letter:
                    print(i, "არის ყვითელი ")

    else:
        print("მაქსიმუმ 5 ასოიანი სიტყვა!!!,ერთი ცდით ნაკლები გაქვს :) ")
        temp += 1

# def is_green():
#     lst = list(set([let for let in set(inp) if let in set(word_to_guess)]))
#     for g in lst:
#         for t in g:
#             print(g, "is green")
#
#
# is_green()
#


#
# def is_yellow():
#     lst = list(set([let for let in set(inp) if let in set(word_to_guess)]))
#     for letter in inp:
#         if letter in word_to_guess:
#             if letter not in lst:
#                 print(letter, "is yellow")
#     print(lst)
#
# is_yellow()