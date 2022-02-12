import random

from colorama import Fore

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
# print(word_to_guess)

grey = []
yellow = []
green = []
last_answer = []

temp = 0

style = input(
    "აირჩიეთ თამაშის ტიპი :  საბავშვო - 1 , გამარტივებული - 2 , კლასიკური - 3 , ვერტიკალურად გართულებული - 4 :  ")

atr = None

if int(style) == 1:
    atr = True
elif int(style) == 2:
    atr = 8
elif int(style) == 3:
    atr = 6
elif int(style) == 4:
    atr = 4

while temp != atr:
    inp = input("შეიყვანე სიტყვა: ")
    temp += 1

    fake = True
    if inp in wholetext:
        if len(inp) == 5:
            if inp != word_to_guess:
                sia1 = []


                def is_grey():

                    already_sorted = list(''.join(set(word_to_guess)))
                    for letter in inp:
                        if letter not in already_sorted:
                            sia1.append(letter)
                    sd = list(dict.fromkeys(sia1))
                    for one in sd:
                        grey.append(one)
                        # print(one, "is grey")


                is_grey()


                def is_green():
                    for num in range(len(inp)):
                        if inp[num] == word_to_guess[num]:
                            green.append(inp[num])
                            # print(inp[num], "is green")


                is_green()


                def is_yellow():
                    sia = []
                    for letter in inp:
                        if letter in word_to_guess:
                            for num in range(len(inp)):
                                if inp[num] != word_to_guess[num]:
                                    sia.append(inp[num])
                    without_dublicates = list(dict.fromkeys(sia))
                    for each in without_dublicates:
                        if each not in sia1:
                            yellow.append(each)
                            # print(each, "is Yellow")


                is_yellow()

            else:
                fake = False
                temp = atr
                print(f"სწორია!,გამოსაცნობი სიტყვა იყო: {word_to_guess}")

        else:
            fake = False
            fake_len = len(inp)
            temp = atr
            print("სიტყვა უნდა შედგებოდეს 5 ასოსგან,თქვენი სიტყვა კი შედგება {} ასოსგან!".format(fake_len))

        if temp is True and fake is True:
            pass
        elif (temp is not True) and (temp == atr) and (fake is True):
            print("სამწუხაროდ თქვენ წააგეთ")
            print("ჩაფიქრებული სიტყვა იყო - {}".format(word_to_guess))

    else:
        print(f"{inp} - ასეთი სიტყვა არ არსებობს ან არ არის ბაზაში,გთხოვთ ცადოთ სხვა !", )
        temp += 1


    def color_answer():
        # მუშაობს მაგრამ ბოლომდე სწორად არა
        for letter in inp:
            if letter in yellow:
                yel = Fore.YELLOW + f'{letter}'
                last_answer.append(yel)
                # print(yel)
            if letter in grey:
                gry = Fore.LIGHTBLUE_EX + f"{letter}"
                last_answer.append(gry)
                # print(gry)
            if letter in green:
                grn = Fore.GREEN + f"{letter}"
                last_answer.append(grn)
                # print(grn)

        ans = ""
        for each1 in last_answer:
            ans += each1

        print(ans)

        del last_answer[:]


    color_answer()


def main():
    pass


if __name__ == '__main__':
    main()
