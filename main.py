import spellchecker
sc = spellchecker.SpellChecker()

while True:
    sc.print_menu()

    while True:
        txtIn = input()
        # Add input control here!
        try:
            int(txtIn)
            break
        except ValueError:
            print("Non è stato digitato alcun numero. Riprovare:\n")

    match int(txtIn):
        case 1:
            print("Inserisci la tua frase in Italiano\n")
            print(sc.handle_sentence(input(), "Italian"))
            print("Premere un qualunque tasto per proseguire.\n")
            input()
        case 2:
            print("Inserisci la tua frase in Inglese\n")
            print(sc.handle_sentence(input(), "English"))
            print("Premere un qualunque tasto per proseguire.\n")
            input()
        case 3:
            print("Inserisci la tua frase in Spagnolo\n")
            print(sc.handle_sentence(input(), "Spanish"))
            print("Premere un qualunque tasto per proseguire.\n")
            input()
        case 4: break
        case _: print("Il numero digitato non corrisponde ad alcun comando. Riprovare:\n")


