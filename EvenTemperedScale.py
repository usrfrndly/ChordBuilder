from EvenTemperedInterval import EvenTemperedInterval
from Scale import Scale
from Chord import Chord
import math
class EvenTemperedScale(Scale):
    note_names = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B","C"]
    def __init__(self, base_fq):
        super(EvenTemperedScale, self).__init__(float(base_fq), 13)
           #self.generate_even_tempered_scale()

    def generate_even_tempered_scale(self):
        for x in range(self.num_intervals):
            self.scale_intervals[x] = EvenTemperedInterval(self.base_freq,x)

    def generate_even_tempered_scale_adjusted(self,min_frequency,max_frequency):
        while self.base_freq * 2 > max_frequency:
            self.base_freq /= 2
        while self.base_freq < min_frequency:
            self.base_freq *= 2
        for x in range(self.num_intervals):
            self.scale_intervals[x] = EvenTemperedInterval(self.base_freq, x)

    def get_et_major_scale(self):
        mjr_scale = [self.scale_intervals[0],self.scale_intervals[2], self.scale_intervals[4], self.scale_intervals[5], self.scale_intervals[7], self.scale_intervals[9], self.scale_intervals[11], self.scale_intervals[12]]
        return mjr_scale

    def get_major_chord(self):
        mjrscale = self.get_et_major_scale()
        return Chord([mjrscale[0],mjrscale[2],mjrscale[4]])


    def print_even_tempered_scale(self):
        for interval in self.scale_intervals:
            print(interval)

