def validate_dna():
    dna_seq = input("Secuencia de ADN: ")
    seqm = dna_seq.upper()
    valid = seqm.count("A") + seqm.count("C") + seqm.count("G") + seqm.count("T") + seqm.count("X")
    if valid == len(seqm):
        return True
    else:
        return False
if validate_dna():
    print("El ADN es válido")
else:
    print("El ADN no es válido")
