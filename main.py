import pytest
from app.calculator import Calculator
class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self,2,4) == 8

    def test_division(self):
        assert self.calc.division(self, 8, 4) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(self, 8, 4) == 4

    def test_adding(self):
        assert self.calc.adding(self, 2, 4) == 6