def validate_dna(dna_seq):
    seqm = dna_seq.upper()
    valid = seqm.count("A") + seqm.count("C") + seqm.count("G") + seqm.count("T") + seqm.count("X")
    return valid == len(seqm)

def frequency(seq):
    dic = {}
    for s in seq.upper():
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    return dic
dna_seq = input("Ingrese la secuencia de ADN: ")

if validate_dna(dna_seq):
    print("La secuencia de ADN es válida.")
    freq_dict = frequency(dna_seq)
    print("Frecuencia:", freq_dict)
else:
    print("La secuencia de ADN no es válida.")
