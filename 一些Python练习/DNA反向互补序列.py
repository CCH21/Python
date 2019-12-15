def dna_complement(seq):
    seq = seq.upper()
    seq = seq.replace('A', 'T')
    seq = seq.replace('T', 'A')
    seq = seq.replace('C', 'G')
    seq = seq.replace('G', 'C')
    return seq


def dna_reverse(seq):
    seq = seq.upper()
    return seq[::-1]


def dna_revcomp(seq):
    seq = seq.upper()
    return dna_complement(seq)[::-1]


def read_seq(inputfile):
    file = open(inputfile, "r")
    seq = file.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq


if __name__ == '__main__':
    dna = read_seq("E:\\python_pycharm\\一些Python程序练习\\DNA\\dna.txt")
    print(dna)                          # 原DNA序列
    print(dna_complement(dna))          # DNA互补序列
    print(dna_reverse(dna))             # DNA反向序列
    print(dna_revcomp(dna))             # DNA反向互补序列
