class Rna:
    def __init__(self, seq):
        assert isinstance(seq, str)
        self.sequence = seq.upper()
        self.complement = ""
        if 'A' or 'C' or 'G' or 'T' in self.sequence:
            pass
        else:
            raise 'This is not a Rna'

    def reverse_complement(self):
        complement_dictionary = {'A': 'U', 'C': 'G', 'U': 'A', 'G': 'C'}

        for i in range(len(self.sequence)):
            self.complement += complement_dictionary[self.sequence[i]]
        return self.complement[::-1]

    def gc(self):
        gc_amount = (self.sequence.count("C") + self.sequence.count("G")) / len(self.sequence)
        return '{0:.2f}%'.format(round(gc_amount, 2)*100)

    def __repr__(self):
        return self.sequence


class Dna:
    def __init__(self, sequence):
        assert isinstance(sequence, str)
        self.sequence = sequence.upper()
        self.complement = ""

        if 'A' or 'C' or 'G' or 'T' in self.sequence:
            pass
        else:
            raise 'This is not a Dna'

    def transcribe(self):
        rna_complement = Rna(self.sequence.replace('T', 'U'))
        return rna_complement

    def gc(self):
        gc_amount = (self.sequence.count("C") + self.sequence.count("G")) / len(self.sequence)
        return '{0:.2f}%'.format(round(gc_amount, 2)*100)

    def reverse_complement(self):
        complement_dictionary = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}

        for i in range(len(self.sequence)):
            self.complement += complement_dictionary[self.sequence[i]]
        return self.complement[::-1]
