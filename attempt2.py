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

    if len(inp) == 5:
        if inp != word_to_guess:
            def isgrey():
                sia = []
                already_sorted = list(''.join(set(word_to_guess)))
                for letter in inp:
                    if letter not in already_sorted:
                        sia.append(letter)
                sd = list(dict.fromkeys(sia))
                for one in sd:
                    print(one, "is grey")


            isgrey()


            def is_green():
                lst = list(set([let for let in set(inp) if let in set(word_to_guess)]))
                for g in lst:
                    print(g, "is green")


            is_green()

        else:
            temp = 6
            print(f"სწორია!,გამოსაცნობი სიტყვა იყო: {word_to_guess}")

    else:
        fake_len = len(inp)
        temp = 6
        print("სიტყვა უნდა შედგებოდეს 5 ასოსგან,თქვენი სიტყვა კი შედგება {} ასოსგან!".format(fake_len))
