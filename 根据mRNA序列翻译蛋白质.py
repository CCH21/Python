import re


def mrna_translate(seq):
    table = {
        'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
        'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
        'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
        'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
        'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
        'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
        'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
        'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
        'UAC': 'Y', 'UAU': 'Y', 'UAA': '_', 'UAG': '_',
        'UGC': 'C', 'UGU': 'C', 'UGA': '_', 'UGG': 'W'
    }
    start_sit = re.search('AUG', seq)
    protein = ""
    for sit in range(start_sit.end() - 3, len(seq), 3):
        protein += table[seq[sit:sit + 3]]
        if table[seq[sit:sit + 3]] == '_':
            break
    return protein


def transcription(seq):
    # 这里我们假设给定DNA序列为编码链
    seq = seq.upper()
    seq = seq.replace('T', 'U')
    return seq


def read_seq(inputfile):
    file = open(inputfile, "r")
    seq = file.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq


if __name__ == '__main__':
    dna = read_seq("E:\\python_pycharm\\一些Python程序练习\\DNA\\dna.txt")
    print(dna)                          # 原DNA序列（编码链）
    mrna = transcription(dna)
    print(mrna)                         # 转录出的mRNA序列
    print(mrna_translate(mrna)[:-1])    # 翻译出的蛋白质序列
