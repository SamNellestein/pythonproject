import csv
from typing import List


CSV_BESTAND = 'lijst.csv'


def lees_personen() -> List[List[str]]:
	"""Lees personen uit het CSV-bestand en zorg dat elke rij 6 velden heeft."""
	personen: List[List[str]] = []
	try:
		with open(CSV_BESTAND, newline='', encoding='utf-8') as f:
			reader = csv.reader(f)
			for rij in reader:
				if rij:
					while len(rij) < 6:
						rij.append('')
					personen.append(rij[:6])
	except FileNotFoundError:
		# Caller kan beslissen wat te doen als het bestand ontbreekt
		return []
	return personen


def schrijf_personen(personen: List[List[str]]) -> None:
	"""Schrijf de lijst met personen terug naar het CSV-bestand."""
	with open(CSV_BESTAND, 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerows(personen)

