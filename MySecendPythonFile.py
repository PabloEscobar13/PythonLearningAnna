#print("Basic Calculator")
#number_1 = input("Napisz jakąś liczbę")
#number_2 = input("Napisz drugą liczbę")
#resulte = number_1 + number_2
#print(resulte)
#print("nie działa dodawanie, bo nie pokazuje sumy - jak temu zaradzić?")

#number_1 = input("Napisz jakąś liczbę")
#number_2 = input("Napisz drugą liczbę")
#resulte = int(number_1) + int(number_2)
#print(resulte)

#number_1 = input("Napisz jakąś liczbę")
#number_2 = input("Napisz drugą liczbę")
#resulte = float(number_1) + float(number_2)
#print(resulte)

#print("Mad Libs Game")
#kwiaty = input("Podaj nazwę gatunku kwatów:")
#kwiaty_2 = input("Jaki inny gatunek rośnie na ziemi?")
#boskie_stworzenia = input("Jakie boskie stworzenia zostały stworzone przez Boga?")
#print("Na górze " + kwiaty)
#print("Na dole " + kwiaty_2)
#print("My się kochamy jak dwa " + boskie_stworzenia)

friends = ["Maciek","Ewelina","Weronika","Monika","Paweł"]

print(friends)
print(friends[1])
print(friends[0])
print(friends[-1])
print(friends[-2])
print(friends[-3])

print(friends[1:])
print(friends[3:])
print(friends[1:3])

friends[1] = "Mike"
print(friends[1])

print("Fuctions of Lists")

friends = ["Maciek","Ewelina","Weronika","Monika","Paweł", "Weronika"]
lucky_numbers = [3, 7, 13, 17, 21]
friends.extend(lucky_numbers)
print(friends)

friends.append("Thomas")
print(friends)
print(friends.index("Ewelina"))
print(friends.count("Weronika"))

print(friends)
friends_2 = friends.copy()
print(friends_2)