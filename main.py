import spellchecker

sc = spellchecker.SpellChecker()

while True:
    sc.print_menu()

    txtIn = input()
    # Add input control here!
    while True:
        if not txtIn.isnumeric():
            txtIn = input("È stato inserito almeno un carattere non numerico. Riprovare: ")
            continue
        if int(txtIn) not in range(1, 5): txtIn = input("È stato inserito un numero diverso da quelli elencati. Riprovare: ")
        else: break

    if int(txtIn) == 1:
        # sc.multi_dictionary.print_dic("italian")
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        print(sc.handle_sentence(txtIn,"italian"), end="")
        continue

    if int(txtIn) == 2:
        # sc.multi_dictionary.print_dic("english")
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        print(sc.handle_sentence(txtIn,"english"), end="")
        continue

    if int(txtIn) == 3:
        # sc.multi_dictionary.print_dic("spanish")
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        print(sc.handle_sentence(txtIn,"spanish"), end="")
        continue

    if int(txtIn) == 4:
        break


