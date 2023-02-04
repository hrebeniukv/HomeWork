# Create an iterator that accepts a sequence and can iterate over values over a given range.
# CustomIterator(sequence, start_index, end_index)

class CustomIterator:
    def __init__(self, sequence, start_index, end_index):
        self.sequence = sequence
        self.start_index = start_index
        self.current = start_index
        self.end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):

        if len(self.sequence) <= self.start_index or len(self.sequence) <= self.end_index:
            raise Exception("Start or End index is out of list")

        if self.current <= self.end_index <= len(self.sequence):

            item = self.sequence[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration


sequence = [1, 3, 4, 5, 6]
start_index = 2
end_index = 1
iterator = CustomIterator(sequence, start_index, end_index)
for i in iterator:
    print(i)
