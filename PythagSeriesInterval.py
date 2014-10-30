"""
HarmonicSeriesRow.py
Jaclyn Horowitz
Music Software Projects 2014
"""

import math
from Interval import Interval

'''
PythagSeriesInterval class : Represents an interval_number_unsorted column in the pythagorean series and is initialized with a
 interval_number_unsorted degree and a base frequency.
'''


class PythagSeriesInterval(Interval):
    def __init__(self, base_fq, interval):
        super(PythagSeriesInterval, self).__init__(base_fq, interval)
        self.numerator = self.get_numerator()
        self.denom = self.get_denom()
        self.factor = self.get_factor()
        self.frequency = self.get_frequency()
        self.octave = self.get_octave()
        self.octave_denom = self.get_octave_denom()
        self.new_denom = self.get_new_denom()
        self.factor_reduced = self.get_factor_reduced()
        self.final_frequency = self.get_final_frequency()

    def __repr__(self):
        # return '{}: {}, {}, {}, {}, {}, {}, {}, {}, {} '.format(self.__class__.__name__,self.interval_number_unsorted, self.numerator,
        # self.denom, self.factor, self.frequency, self.octave, self.octave_denom, self.factor_reduced,self.final_frequency)
        return '{}:  Scale Degree:{}, Unsorted Interval Number: {}, Numerator: {}, Denom: {}, Factor:{}, Frequency: {}, Octave: {}, Octave Denom: {}, Factor Reduced: {},Final Frequency:{} '.format(
            self.__class__.__name__, self.note_number, self.interval_number_unsorted, self.numerator,
            self.denom, self.factor, self.frequency, self.octave, self.octave_denom, self.factor_reduced,
            self.final_frequency)

    '''
    Methods that calculate properties for a row in the HarmonicSeries
    '''

    def get_numerator(self):
        if self.interval_number_unsorted == -1:
            return 2
        else:
            return math.pow(3, self.interval_number_unsorted)

    def get_frequencytofundamental(self):
        return "\"" + str(self.interval_number_unsorted) + "/1\""

    def get_octave(self):
        return math.floor(self.interval_number_unsorted / 2)

    def get_factor(self):
        return float(self.numerator) / float(self.denom)

    def get_octave_denom(self):
        return math.pow(2, self.octave)

    def get_denom(self):
        if self.interval_number_unsorted == -1:
            return 3
        else:
            return math.pow(2, self.interval_number_unsorted)

    def get_frequency(self):
        return self.base_fq * self.factor

    def get_new_denom(self):
        return self.denom * self.octave_denom

    def get_factor_reduced(self):
        return self.factor / self.octave_denom

    def get_final_frequency(self):
        return round(self.base_fq * self.factor_reduced, 2)

    # def set_note_name(self):
    # if self.final_frequency is not 0:
    #         if self.final_frequency in self.note_names.keys():
    #             name = self.note_names[self.final_frequency]
    #             self.note_name = name
    #         elif self.final_frequency / 2 in self.note_names.keys():
    #             name = self.note_names[self.final_frequency / 2]
    #             self.note_name = name
    #     else:
    #         return

    # to_array(): Returns an array representation of the properties of a row in the HarmonicSeries, which
    # orders the properties the same as in the csv file
    def to_array(self):
        return [self.note_name, self.note_number, self.interval_number_unsorted, self.numerator, self.denom,
                self.factor, self.frequency, self.octave,
                self.octave_denom, self.factor_reduced, self.final_frequency]

    # show_row(): Returns a string representation of the properties of a row in the HarmonicSeries
    def show_column(self):
        # [interval_number_unsorted, frequencytofundamental, frequency, octave, denom, ratio, ratio_reduced, decimal,freqinlowestoctave]
        print("[{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8} ".format(self.note_name, self.note_number,
                                                                     str(self.interval_number_unsorted), self.numerator,
                                                                     str(self.denom), str(self.factor),
                                                                     str(self.frequency), self.octave,
                                                                     self.octave_denom, str(self.factor_reduced),
                                                                     self.final_frequency))