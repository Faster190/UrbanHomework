import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        human = Runner("Nick")
        for _ in range(10):
            human.walk()
        self.assertEqual(human.distance, 50)

    def test_run(self):
        human = Runner("Nick")
        for _ in range(10):
            human.run()
        self.assertEqual(human.distance, 100)

    def test_challenge(self):
        human_1 = Runner("Nick")
        human_2 = Runner("Mike")
        for _ in range(10):
            human_1.run()
            human_2.walk()
        self.assertNotEqual(human_1.distance, human_2.distance)
