from unittest import TestCase


class TestRecursion(TestCase):
    def test_exponentiation(self):
        from recursion.exponentiation import exp
        self.assertTrue(exp(3, 3) == 27)

    def test_mod(self):
        from recursion.exponentiation import mod
        self.assertTrue(mod(3, 3, 5) == 2)

    def test_factorial(self):
        from recursion.factorial import factorial
        self.assertTrue(factorial(5) == 120)
