from src.io_utils import lees_personen
from src.operations import (
    namen_naar_hoofdletters,
    namen_naar_kleine_letters,
    voeg_persoon_toe,
    verwijder_persoon,
)
from src.ui import (
    toon_menu,
    toon_overzicht,
    prompt_new_person,
    prompt_delete_index,
)


def main():
    """Hoofdprogramma: bestuurt menu en acties (CLI)."""
    print("Welkom bij Personen Beheer")
    personen = lees_personen()
    while True:
        keuze = toon_menu()
        if keuze == '1':
            personen = namen_naar_hoofdletters(personen)
        elif keuze == '5':
            personen = namen_naar_kleine_letters(personen)
        elif keuze == '2':
            gegevens = prompt_new_person()
            if gegevens:
                personen = voeg_persoon_toe(personen, gegevens)
            else:
                print("Toevoegen geannuleerd.")
        elif keuze == '3':
            if not personen:
                print("Geen personen om te verwijderen.")
            else:
                toon_overzicht(personen)
                idx = prompt_delete_index(len(personen))
                if idx is None or not (0 <= idx < len(personen)):
                    print("Verwijderen geannuleerd of ongeldige invoer.")
                else:
                    personen = verwijder_persoon(personen, idx)
        elif keuze == '4':
            toon_overzicht(personen)
        elif keuze == '0':
            print("Programma gestopt.")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.")
