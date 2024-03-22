class CLONERANGE:
    def __init__(self, start, stop = None, step = 1):
        if stop is None:
            self.stop = start
            self.start = -step
            self.step = step
        else:
            self.start = start - step
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop and self.step > 0:
            self.start += self.step
            if self.start >= self.stop:
                raise StopIteration
            return self.start
        if self.start > self.stop and self.step < 0:
            self.start += self.step
            if self.start <= self.stop:
                raise StopIteration
            return self.start


for i in CLONERANGE(10, 20,0.5):
    print(i)
