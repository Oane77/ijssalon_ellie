#opgave 12 deel 1
from algemene_functies import mijn_functie_2


#opgave 5

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)

    return (
        f"Vandaag in de aanbieding: emmertje ijs (1 liter) "
        f"in de smaak {smaak}, van {prijs} euro voor "
        f"{nieuwe_prijs:.2f} euro."
    )



print(aanbieding_1("aardbei", 4, 0.1))


#opgave 6 en 7
def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    btw_bedrag = totaal * btw

    return (
        f"Het totaal van alle inkomsten van deze week is "
        f"{totaal} euro, waarover {btw_bedrag:.2f} euro "
        f"btw betaald dient te worden."
    )


week = [220, 430, 125, 160, 205, 90, 345]

print(inkomsten_totaal(week, 0.09))


#opgave 8
def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]


week = [220, 430, 125, 160, 205, 90, 345]

print(laag_en_hoog(week))

#opgave 9 en 10
def gemiddelde(mijn_lijst):
    gemiddeld = sum(mijn_lijst) / len(mijn_lijst)

    return (
        f"De gemiddelde inkomsten deze week zijn "
        f"{gemiddeld:.2f} euro."
    )


week = [220, 430, 125, 160, 205, 90, 345]

print(gemiddelde(week))


#Opgave 11 
def laag_en_hoog(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

print(meervoudig([10, 5, 3, 2, 1, 2, 9]))


#opgave 12 deel 2
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])

print(combinatie([10, 5, 3, 2, 1, 2, 9]))


wait = input("Press Enter to continue.")