from Interval import Interval
class Chord:
    def __init__(self,notes=None):
        self.notes = notes

    def __str__(self):
        string=""
        for n in self.notes:
            string+=str(n)
        return string

    def __repr__(self):
        return str(self.notes)



