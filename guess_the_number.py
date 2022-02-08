from random import randint

los = randint(1,100)
odp = -1
i = 0
print("Zgadnij liczbę z przedziału od 1 do 100")

while odp != los: 
    i += 1
    odp = int(input("Podaj Liczbę: "))
    if odp > los:
        print("Wylosowana liczba jest mniejsza od Twojej")
    elif odp < los:
        print("Wylosowana liczba jest większa od Twojej")
print("Brawo, odgadłeś za", i, "razem.")