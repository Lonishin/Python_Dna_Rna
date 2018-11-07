class Rna:
    def __init__(self, seq):
        self.sequence = seq
        self.complement = ""

    def reverse_complement(self):
        complement_dictionary = {'A': 'U', 'C': 'G', 'U': 'A', 'G': 'C'}

        for i in range(len(self.sequence)):
            self.complement += complement_dictionary[self.sequence[i]]
        return self.complement[::-1]

    def gc(self):
        gc_amount = (self.sequence.count("C") + self.sequence.count("G")) / len(self.sequence)
        return gc_amount

    def __repr__(self):
        return self.sequence


class Dna(Rna):
    def __init__(self, seq):
        self.dna_seq = seq

    def transcribe(self):
        rna_seq = self.dna_seq.replace('T', 'U')
        rna_complement = Rna(rna_seq).reverse_complement()
        return rna_complement
