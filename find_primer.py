from Bio import SeqIO

infilename = "4seq.fasta"
wanted_seq = "AGCT"


for record in SeqIO.parse(infilename, "fasta"):
    if wanted_seq in record.seq:
        print record.seq
