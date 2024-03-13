"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class TestCounter(unittest.TestCase):
    def test_singleton(self):
        counter = Counter()
        counter1 = Counter()
        for i in range(5):
            counter.increment()
        self.assertEqual(counter1, counter)

    def test_instance_share_the_same_count(self):
        counter1 = Counter()
        counter1.increment()
        counter1.increment()
        counter2 = Counter()
        self.assertEqual(2, counter2.count)

