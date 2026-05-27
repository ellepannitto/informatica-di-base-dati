with open("dati/voti.txt", "r", encoding="utf-8") as f:
    for line in f:
        campi = line.strip().split(",")
        print(campi[0], campi[1], "→ voto:", campi[2])
