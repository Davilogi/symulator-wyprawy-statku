import random

def gra():
    print("=== Symulator wyprawy statku ===")

    nazwa = input("Podaj nazwę statku:")

    try:
        x = int(input("Podaj pozycję startową x:"))
        y = int(input("Podaj pozycję startową y:"))
        energia = int(input("Podaj ilość energii:"))

    except ValueError:
        print ("Błąd danych. Ustawiono wartości domyślnie")
        x=0
        y=0
        energia = 30
    start_x = x
    start_y = y
    start_energia = energia

    try:
        cel_x = int(input("Podaj cel wyprawy x:"))
        cel_y = int(input("Podaj cel wyprawy y:"))
    except ValueError:
        print("Błąd celu. Ustawiono cel domyślny: 5, 5")
        cel_x = 5
        cel_y = 5


    krok = 0
    max_krokow = 20
    historia = []

    print("\n--- START WYPRAWY---")
    print("Statek:", nazwa)
    print("Pozycja startowa:", x, y)
    print("Cel: ",  cel_x,cel_y)
    print("Energia startowa: ", energia)
    print("Granice świata: od -10 do 10 na osi X i Y")
    print("Warunek zakończenia: dotarcie do celu, brak energii albo limit kroków")
    print("Sterowanie: N - na górę,S - w dół, E - w prawo,W - w lewo")
    print()

    while energia > 0 and krok < max_krokow:

        if x == cel_x and y == cel_y:
            break


        krok += 1


        stare_x = x
        stare_y = y
        stara_energia = energia

        ruch = input(f"Krok {krok} - wybierz kierunek N/S/E/W: ").upper()
        if ruch == "N":
            y += 1
        elif ruch == "S":
            y-= 1
        elif ruch == "E":
            x += 1
        elif ruch == "W":
            x -= 1

        else:
            print("Niepoprawny ruch. Statek traci 1 energię.")
            energia -= 1
            continue

        energia -= 2
        opis = "Normalny ruch statku. Zużyto 2 energii."

        if x < -10 or x > 10 or y < -10 or y > 10:
            x = stare_x
            y = stare_y
            energia -= 3
            opis = "Statek próbował wypłynąć poza mapę. Cofnięto go i stracił 3 energii."

        los = random.randint(1,3)

        if los == 1:
            energia -= 4
            opis += " Statek wpłynął na rafę: -4 energii"
        elif los == 2:
            energia += 3
            opis +=(" Silny wiatr pomógł statkowi: +3 energii")
        elif los == 3:
            energia += 5
            opis += " Znaleziono wyspę z zapasami: +5 energii"

        zdarzenie = random.randint(1,4)

        if zdarzenie == 1:
            energia -= 5
            opis+= (" Losowe zdarzenie: -5 energii")

        elif zdarzenie == 2:
            x += 1
            opis += " Losowe zdarzenie: prąd morski przesunął statek o 1 w prawo."
        if x < -10 or x > 10 or y < -10 or y > 10:
            x = stare_x
            y = stare_y
            energia -= 3
            opis += " Po zdarzeniu statek wyszedł poza mapę, więc wrócił na poprzednią pozycję i stracił 3 energii."

        historia.append(opis)

        print("Wybrany ruch:", ruch)
        print("Pozycja przed ruchem:", stare_x, stare_y)
        print("Pozycja po ruchu:",x,y)
        print("Energia przed krokiem:", stara_energia)
        print("Energia po kroku:", energia)
        print("Opis:", opis)
        print()

    print("=== RAPORT KOŃCOWY ===")
    print("Nazwa statku:", nazwa)
    print("Pozycja startowa:", start_x, start_y)
    print("Energia startowa:", start_energia)
    print("Cel:", cel_x, cel_y)
    print("Końcowa pozycja:",x,y)
    print("Liczba kroków:", krok)
    print("Pozostała energia:",energia)

    if x == cel_x and y == cel_y:
        wynik = "SUKCES"
        powod = "Statek dotarł do celu."
        punkty = energia + 100 - krok

    elif energia <= 0:
        wynik = "PORAŻKA"
        powod = "Skończyła się energia"
        punkty = krok

    else:
        wynik = "CZĘŚCIOWY SUKCES"
        powod = "Skończył się limit kroków."
        punkty = energia + krok

    print("Wynik wyprawy:", wynik)
    print("Przyczyna zakończenia:", powod)
    print("Końcowy wynik punktowy:", punkty)

    print("\nNajważniejsze zdarzenia:")
    if len(historia) == 0:
        print("Brak zdarzeń.")
    else:
        for zdarzenie in historia:
            print("-", zdarzenie)

while True:
    gra()

    decyzja = input("\nCzy chcesz uruchomić symulację ponownie? tak/nie: ").lower()

    if decyzja != "tak":
        print("Koniec programu.")
        break
