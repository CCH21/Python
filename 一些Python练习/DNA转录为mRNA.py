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
    print(transcription(dna))           # 转录出的mRNA序列
