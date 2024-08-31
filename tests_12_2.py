import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def sorting(self):
        for j in range(len(self.participants) - 1):
            for i in range(len(self.participants) - 1):
                if self.participants[i + 1].speed > self.participants[i].speed:
                    tmp = self.participants[i]
                    self.participants[i] = self.participants[i + 1]
                    self.participants[i + 1] = tmp

    def start(self):
        self.sorting()  # новая функция для избежания возможной логической ошибки
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for d in cls.all_results.values():
            new_dict = {}
            for key, value in d.items():
                new_dict[key] = value.name
            print(new_dict)

    def test_1(self):
        tour = Tournament(90, self.runner_1, self.runner_3)
        self.all_results[1] = tour.start()
        self.assertTrue(self.all_results[1][len(self.all_results[1])] == "Ник")

    def test_2(self):
        tour = Tournament(90, self.runner_2, self.runner_3)
        self.all_results[2] = tour.start()
        self.assertTrue(self.all_results[2][len(self.all_results[2])] == "Ник")

    def test_3(self):
        tour = Tournament(90, self.runner_2, self.runner_1, self.runner_3)
        self.all_results[3] = tour.start()
        self.assertTrue(self.all_results[3][len(self.all_results[3])] == "Ник")
