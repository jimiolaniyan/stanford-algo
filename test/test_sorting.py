from unittest import TestCase


class TestSorting(TestCase):
    def test_merge_sort(self):
        from sorting.merge_sort import merge_sort
        self.assertTrue(merge_sort([8, 7, 6, 5, 4, 3, 2, 1, ]) == [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertTrue(merge_sort([7, 6, 5, 4, 3, 2, 1, ]) == [1, 2, 3, 4, 5, 6, 7])

    def test_sort_count(self):
        from sorting.sort_count import sort_count
        self.assertTrue(sort_count([8, 7, 6, 5, 4, 3, 2, 1, ]) == (28, [1, 2, 3, 4, 5, 6, 7, 8]))

    # def test__quick_sort_count(self):
    #     from sorting.quick_sort import quick_sort_and_count
    #     self.assertTrue(quick_sort_and_count(lines, 0, len(lines)) == (138382, lines.sort()))