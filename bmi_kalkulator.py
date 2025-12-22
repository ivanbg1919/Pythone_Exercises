visina = float(input("Unesi visinu u metrima (npr. 1.75): "))
tezina = float(input("Unesi težinu kilogramima (npr. 80): "))

# Proveri unos
if  visina <= 0 or tezina <= 0:
    print("Greska: visina i tezina moraju biti pozitivni brojevi!")
else:
    # Izračunavanje BMI     < 18.5 normal 25 >
    bmi = tezina / (visina ** 2)
    print(f"Tvoj BMI je: {bmi:2f}")

# Proveri BMI kategorije
if bmi < 18.5:
    print("Kategorija: Pothranjen")
elif bmi < 25:
    print("Kategorija: Normalna telesna tezina")
elif bmi < 30:
    print("Kategorija: Prekomerna telesna tezina")
else:
    print("Gojaznost")









