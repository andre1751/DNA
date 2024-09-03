def validate_dna():
    dna_seq = input("Ingrese la secuencia de ADN: ")
    seqm = dna_seq.upper()
    valid = seqm.count("A") + seqm.count("C") + seqm.count("G") + seqm.count("T") + seqm.count("X")
    if valid == len(seqm):
        return True
    else:
        return False
if validate_dna():
    print("La secuencia de ADN es válida.")
else:
    print("La secuencia de ADN no es válida.")