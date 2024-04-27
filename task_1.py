class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        self.cursor = 0
        self.cursor_2 = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor == len(self.list_of_lists):
            raise StopIteration
        sublist = self.list_of_lists[self.cursor]
        if self.cursor_2 == len(sublist):
            self.cursor_2 = 0
            self.cursor += 1
            if self.cursor == len(self.list_of_lists):
                raise StopIteration
        item = self.list_of_lists[self.cursor][self.cursor_2]
        self.cursor_2 += 1
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
