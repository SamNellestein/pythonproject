from typing import List
from src.io_utils import schrijf_personen


def namen_naar_hoofdletters(personen: List[List[str]]) -> List[List[str]]:
	for p in personen:
		p[0] = p[0].upper() if p[0] else ''
		p[1] = p[1].upper() if p[1] else ''
		p[2] = p[2].upper() if p[2] else ''
	schrijf_personen(personen)
	return personen


def namen_naar_kleine_letters(personen: List[List[str]]) -> List[List[str]]:
	for p in personen:
		p[0] = p[0].lower() if p[0] else ''
		p[1] = p[1].lower() if p[1] else ''
		p[2] = p[2].lower() if p[2] else ''
	schrijf_personen(personen)
	return personen


def voeg_persoon_toe(personen: List[List[str]], gegevens: List[str]) -> List[List[str]]:
	while len(gegevens) < 6:
		gegevens.append('')
	personen.append(gegevens[:6])
	schrijf_personen(personen)
	return personen


def verwijder_persoon(personen: List[List[str]], index: int) -> List[List[str]]:
	if 0 <= index < len(personen):
		personen.pop(index)
		schrijf_personen(personen)
	return personen
