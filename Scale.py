from Interval import Interval
import math
class Scale(object):
    def __init__(self, base_fq,numintervals):
        self.base_freq = base_fq
        self.num_intervals = numintervals
        self.scale_intervals = [Interval]  * self.num_intervals
        self.max_frequency = base_fq * math.pow(2, 2)
        self.min_frequency = base_fq / math.pow(2, 2)

    def sort_by_final_frequency(self):
        sorted_scale = sorted(self.scale_intervals, key=lambda a: a.final_frequency)
        notenum = 1
        for interval in sorted_scale:
            interval.note_number = notenum
            notenum += 1
        return sorted_scale

    # def get_octave(self):
    #     octave = Interval(self.base_freq)
    #     octave_freq = self.scale_intervals[0].final_frequency*2
    #     octave.final_frequency = octave_freq
    #     octave.note_number = self.num_intervals
    #     octave.set_note_name()
    #     return octave

    # def get_next_mode(self):
    #     self.scale_intervals = self.sort_by_final_frequency()
    #     self.scale_intervals.pop(0)
    #     octave = self.get_octave()
    #     self.scale_intervals.append(octave)
    #     return self.scale_intervals




__author__ = 'jaclyn'
