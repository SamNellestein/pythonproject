from typing import List, Optional


def toon_menu() -> str:
	print("\nKeuzemenu:")
	print("1. Namen naar hoofdletters")
	print("5. Namen naar kleine letters")
	print("2. Nieuwe persoon toevoegen")
	print("3. Personen verwijderen")
	print("4. Overzicht van alle personen")
	print("0. Programma stoppen")
	return input("\nMaak jouw keuze (0-5): ").strip()


def toon_overzicht(personen: List[List[str]]) -> None:
	if not personen:
		print("\nEr zijn geen personen in de lijst.")
		return
	print("\nOverzicht van alle personen:")
	for i, p in enumerate(personen, 1):
		print(f"{i}. {p[0]} {p[1]} {p[2]}, {p[3]}, {p[4]}, {p[5]}")


def prompt_new_person() -> Optional[List[str]]:
	print("\nNieuwe persoon toevoegen (laat leeg om te annuleren):")
	voornaam = input("Voornaam: ").strip()
	if voornaam == '':
		return None
	tussen = input("Tussenvoegsel (laat leeg indien geen): ").strip()
	achternaam = input("Achternaam: ").strip()
	adres = input("Adres: ").strip()
	postcode = input("Postcode: ").strip()
	plaats = input("Woonplaats: ").strip()
	return [voornaam, tussen, achternaam, adres, postcode, plaats]


def prompt_delete_index(max_index: int) -> Optional[int]:
	keuze = input(f"Voer nummer (1-{max_index}) of leeg om te annuleren: ").strip()
	if keuze == '':
		return None
	try:
		idx = int(keuze) - 1
		return idx
	except ValueError:
		return None
