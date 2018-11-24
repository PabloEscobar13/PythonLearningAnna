print("Nauka podstawowych zmiennych i danych")
character_name = "John"
character_age = "50"
mężczyzna = "man"
print("There onece was a "+mężczyzna+" niked "+character_name+".")
print("He was "+character_age+" years old.")

character_name = "Mike"
character_age = "25"
print("He really like the name "+character_name+".")
print("But didn't like being "+character_age+".")

x = 5
y = 7
print(x+y)
print(y-x)
print(y*x)
print(y/x)

x=10+2+5
print(x)

print(type("John"))
print(type(x))

print("Piękna Dupka Pawełka")
print("Piękna Dupka \n Pawełka")

phrase = "Aneczka ma brązowe włosy"
print(phrase + " lubi koty.")
print(phrase.upper())
print(phrase.isupper())
print(len(phrase))
print(phrase[0])
print(phrase[1])
print(phrase[2])
print(phrase[3])
print(phrase[4])
print(phrase[5])
print(phrase[6])

print(phrase.index("A"))
print(phrase.index("necz"))
print(phrase.replace("Aneczka","Maciek"))

print("Working with numbers")
print(2+5+7)
print(2+5*8)
print((2+5)*8)
print(10%3)

my_favourite_number = 7
print(str(my_favourite_number) + " to moja ulubiona liczba")

my_number = -5
print(abs(my_number))
print(pow(3,3))
print(max(3,6))
print(min(3,6))
print(round(4.5897))
print(round(4.2327))

from math import *
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))

print("Komputer ze mną się wita")
name = input("Jak się nazywasz?")
age = input("Ile masz lat Mój miły? :)")
print(name + " ,miło Cię poznać."+ age + "... hmm... Niezła z Ciebie dupeczka!")