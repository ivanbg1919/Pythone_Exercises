while True:
    print("\n--- BMI KALKULATOR ---")

    visina = float(input("Unesi visinu u metrima (npr. 1.75): "))
    tezina = float(input("Unesi tezinu u kilogramima (npr. 80): "))

    if visina <= 0 or tezina <= 0:
        print("Greska: visina i tezina moraju biti pozitivni brojevi!")
    else:
        bmi = tezina / (visina ** 2)
        print(f"Tvoj BMI je: {bmi:.2f}")

        if bmi < 18.5:
            print("Kategorija: Pothranjen")
        elif bmi < 25:
            print("Kategorija: Normalna telesna tezina")
        elif bmi < 30:
            print("Kategorija: Prekomerna telesna tezina")
        else:
            print("Kategorija: Gojaznost")

    # Pitanje za nastavak
    nastavak = input("\nZelis li da uneses nove podatke? (da/ne): ").lower()
    if nastavak != "da":
        print("Program zavrsen. 👋")
        break
