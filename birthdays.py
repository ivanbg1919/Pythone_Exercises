### without saving data to files ###

birthdays = {'Mica':'26.1', 'Igor': '26.7', 'Fiki': '15.9', 'Koka': '6.12'}

while True:
    print("Please enter a name: (blank to quit)")
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(f"{birthdays[name]} is birthday of {name}")
    else:
        print(f"I don't have information {name}")
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.")

