"""
Jaclyn Horowitz
Music Software Projects 2014
"""
from EvenTemperedInterval import EvenTemperedInterval

from EvenTemperedScale import EvenTemperedScale
from PythagSeries import PythagSeries
import math
import pyaudio
import struct
import numpy
from operator import itemgetter
from scipy import interpolate

'''
'''


class Scales(object):
    def __init__(self, base_fq):

        self.base_fq = float(base_fq)
        self.max_frequency = base_fq * math.pow(2, 2)
        self.min_frequency = base_fq / math.pow(2, 2)

    def play_pythag_scales(self):
        # adjust octave to be within 4 octaves of starting frequency
        newbase = self.base_fq
        for x in range(6):
            pythag_series = PythagSeries(newbase)
            pythag_series.generate_pythag_scale_adjusted(self.min_frequency, self.max_frequency)
            pythag_series = pythag_series.sort_by_final_frequency()
            play_scale(pythag_series)
            newbase *= float(3.0 / 2.0)

    def play_et_scales(self):
        newbase = self.base_fq
        for x in range(6):
            print(x)
            et_scale = EvenTemperedScale(newbase)
            et_scale.generate_even_tempered_scale_adjusted(self.min_frequency, self.max_frequency)
            # newbase = et_scale.scale_intervals[7].final_frequency
            play_scale(et_scale.get_et_major_scale())
            newbase *= math.pow(EvenTemperedInterval.even_interval_factor, 7)

        newbase = self.base_fq
        for x in range(6, 12):
            print(x)
            et_scale = EvenTemperedScale(newbase)
            et_scale.generate_even_tempered_scale_adjusted(self.min_frequency, self.max_frequency)
            newbase /= math.pow(EvenTemperedInterval.even_interval_factor, 7)
            play_scale(et_scale.get_et_major_scale())


    def play_pythag_chords_sequentially(self):
        pyscale = PythagSeries(self.base_fq)
        pyscale.generate_pythag_scale_adjusted(self.min_frequency, self.max_frequency)
        sorted_scale = pyscale.sort_by_final_frequency()
        for i in sorted_scale:
            newscale = PythagSeries(i.final_frequency)
            newscale.generate_pythag_scale_adjusted(self.min_frequency, self.max_frequency)
            c = newscale.get_major_chord()
            print(c)
            play_chord(c)

    def play_pythag_chord_fifths(self):
        newbase = (2.0 / 3.0) * float(self.base_fq)
        for i in range(6):
            pyscale = PythagSeries(newbase)
            pyscale.generate_pythag_scale_adjusted(self.min_frequency, self.max_frequency)
            c = pyscale.get_major_chord()
            print(c)
            play_chord(c)
            newbase *= (3.0 / 2.0)

    def play_et_chords_sequentially(self):
        et_scale = EvenTemperedScale(self.base_fq)
        et_scale.generate_even_tempered_scale_adjusted(self.min_frequency, self.max_frequency)
        major_scale = et_scale.get_et_major_scale()
        for i in major_scale:
            new_et = EvenTemperedScale(i.final_frequency)
            new_et.generate_even_tempered_scale_adjusted(self.min_frequency, self.max_frequency)
            c = new_et.get_major_chord()
            print(c)
            play_chord(c)

    def play_et_chord_fifths(self):
        newbase = (2.0 / 3.0) * float(self.base_fq)
        for i in range(6):
            etscale = EvenTemperedScale(newbase)
            etscale.generate_even_tempered_scale_adjusted(self.min_frequency, self.max_frequency)
            c = etscale.get_major_chord()
            print(c)
            play_chord(c)
            newbase *= (3.0 / 2.0)


def play_scale(scale):
    fs = 48000
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=fs,
        output=True)
    for interval in scale:
        print(interval.final_frequency)
        play_tone(interval.final_frequency, .5, 1, fs, stream)

    stream.close()
    p.terminate()


def play_tone(frequency, amplitude, duration, fs, stream):
    N = int(fs / frequency)
    T = int(frequency * duration)  # repeat for T cycles
    dt = 1.0 / fs
    # 1 cycle
    tone = (amplitude * math.sin(2 * math.pi * frequency * n * dt)
            for n in range(N))
    # =todo: get the format from the stream; this assumes Float32
    data = b''.join(struct.pack('f', samp) for samp in tone)
    for n in range(T):
        stream.write(data)


def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)


def shape(data, points, kind='slinear'):
    items = points.items()
    items.sort(key=itemgetter(0))
    keys = map(itemgetter(0), items)
    vals = map(itemgetter(1), items)
    interp = interpolate.interp1d(keys, vals, kind=kind)
    factor = 1.0 / len(data)
    shape = interp(numpy.arange(len(data)) * factor)
    return data * shape


def harmonics1(freq, length):
    a = sine(freq * 1.00, length, 44100)
    b = sine(freq * 2.00, length, 44100) * 0.5
    c = sine(freq * 4.00, length, 44100) * 0.125
    return (a + b + c) * 0.2


def harmonics2(freq, length):
    a = sine(freq * 1.00, length, 44100)
    b = sine(freq * 2.00, length, 44100) * 0.5
    return (a + b) * 0.2


def pluck1(note):
    chunk = harmonics1(note.final_frequency, 2)
    return shape(chunk, {0.0: 0.0, 0.005: 1.0, 0.25: 0.5, 0.9: 0.1, 1.0: 0.0})


def pluck2(note):
    chunk = harmonics2(note.final_frequency, 2)
    return shape(chunk, {0.0: 0.0, 0.5: 0.75, 0.8: 0.4, 1.0: 0.1})


def play_chord(chord):
    # root = chord.get(n)
    # third = scale.transpose(root, 2)
    #fifth = scale.transpose(root, 4)
    c = pluck1(chord.notes[0]) + pluck1(chord.notes[1]) + pluck1(chord.notes[2])
    chunks = [c]
    chunk = numpy.concatenate(chunks) * 0.25
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
    stream.write(chunk.astype(numpy.float32).tostring())
    stream.close()
    p.terminate()


def main():
    # Change base_frequency manually
    base_frequency = 528
    print("Your base frequency is %d hertz" % base_frequency)
    scales = Scales(base_frequency)
    #
    print("*** PYTHAGOREAN CHORDS SEQUENTIALLY ***")
    scales.play_pythag_chords_sequentially()
    print("*** PYTHAGOREAN CHORDS FIFTHS ***")
    scales.play_pythag_chord_fifths()
    print("*** EVEN TEMPERED CHORDS SEQUENTIALLY ***")
    scales.play_et_chords_sequentially()
    print("*** EVEN TEMPERED CHORDS FIFTHS ***")
    scales.play_et_chord_fifths()


if __name__ == '__main__':
    main()


