class FlatIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.flat_data = self.flatten(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.flat_data):
            item = self.flat_data[self.index]
            self.index += 1
            return item
        raise StopIteration

    def flatten(self, data):
        if isinstance(data, list):
            flattened = []
            for item in data:
                if isinstance(item, list):
                    flattened.extend(self.flatten(item))
                else:
                    flattened.append(item)
            return flattened
        else:
            return [data]


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
