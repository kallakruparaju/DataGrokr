class ReverseIter:
    def __init__(self, l):
        self.l = l[::-1]
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.l):
            i = self.i
            self.i += 1
            return self.l[i]
        else:
            raise StopIteration()
    def next(self):
        return self.__next__()

for i in ReverseIter([67,43,9,278,332]):
    print(i)