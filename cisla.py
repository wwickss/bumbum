cisloJedna = input(str("Zadejte prvni cislo: "))
cisloDva = input(str("Zadejte druhe cislo: "))
znamenko = input(str("Zadejte operace: "))
if znamenko == "+":
    soucet = cisloJedna+cisloDva
    print("Soucet je: ",soucet)
elif znamenko == "-":
    rozdil = cisloJedna-cisloDva
    print("Rozdil je: ",rozdil)
elif znamenko == "*":
    soucin = cisloJedna*cisloDva
    print("Soucin je: ",soucin)
else znamenko == "/":
    podil = cisloJedna/cisloDva
    print("Podil je: ",podil)


x = len(znamenko)
znamenko = [znamenko]
znamenko = ["soucet", "rozdil", "soucin", "podil"]

opakovat = input("Chcete opakovat program? (ano/ne)")
import = random
random.choice(znamenko)


