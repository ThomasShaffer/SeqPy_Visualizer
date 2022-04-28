from django.db import models
from seqpy_library.SourceCode.dna import * 

# Create your models here.
methods = {'complementation': dna.complementation, 
            'reverse_complementation': dna.reverse_complementation,
            'translation': dna.translation,
            'transcription': dna.transcription,
            'hamming_distance':dna.hamming_dist,
            'edit_distance': dna.edit_dist}


class Dna(models.Model):
    name = models.TextField()
    sequence = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def to_dna(self, data):
        dna_obj = dna(data["sequence"], data["name"])
        return dna_obj

    def compute(self, computation):
        dna = self.to_dna({"name":self.name, "sequence":self.sequence})
        compute_method = methods[computation]
        returned_dna = compute_method(dna)
        return returned_dna[:10] + "..." if len(returned_dna) > 10 else returned_dna
    
    def create(self, given_name, given_sequence):
        new_dna = self.create(name=given_name, sequence=given_sequence)
        print(new_dna)