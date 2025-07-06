from django.test import SimpleTestCase
from app import calc

class Clactests(SimpleTestCase):

  def test_add_num(self):

    res = calc.add(5,6)

    self.assertEqual(res,11)

  def test_subtract_num(self):
    res = calc.sub(5,6)
    self.assertEqual(res,-1)
