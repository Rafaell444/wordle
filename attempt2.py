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
    inp = input("შეიყვანე სიტყვა: ")
    temp += 1

    # needstobesorted = []
    # for letter in inp:
    #     if letter in word_to_guess:
    #         needstobesorted.append(letter)
    #         sorted_list = list(dict.fromkeys(needstobesorted))
    #         to_str = " ".join(map(str, sorted_list))
    #         print(to_str)
    #

    zero = inp[0]
    first = inp[1]
    second = inp[2]
    third = inp[3]
    fourth = inp[4]

    listofindex = [zero, first, second, third, fourth]


    def isgrey():
        sia = []
        alreadysorted = list(''.join(set(word_to_guess)))
        for letter in inp:
            if letter not in alreadysorted:
                sia.append(letter)
        sd = list(dict.fromkeys(sia))
        for one in sd:
            print(one, "is grey")


    isgrey()


    def isgreen():
        lst = list(set([let for let in set(inp) if let in set(word_to_guess)]))
        for g in lst:
            for t in g:
                print(g, "is green")
    isgreen()

