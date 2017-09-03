class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, newvalue):
        self.series.append(newvalue)
        total = sum(self.series)
        return total/len(self.series)

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager
