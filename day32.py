print("Greetings in different languages")
print()
greetings = ["Hello", "Hola", "Halo", "Ciao", "Ola", "Ni hao", "Asalaam Alaikum","Namaste", "OHAYO", "MERHABA", "Bonjour", "Salve", "Privit", "Tung"]

import random
name = input("What is your name? ")
print(f"{greetings[random.randint(0,13)]}", name)