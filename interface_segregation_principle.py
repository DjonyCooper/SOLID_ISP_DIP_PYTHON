"""
Необходимо исправить этот класс, разбив его на более маленькие интерфейсы т.к. он нарушает принцип разделения интерфейсов.
class Worker:
    def work(self):
        pass
    def eat(self):
        pass
"""
class Work:
    pass
class Eat:
    pass


class HumanWorker(Work, Eat):
    def work(self):
        print("Человек работает")

    def eat(self):
        print("Человек ест")


class RobotWorker(Work):
    def work(self):
        print("Робот работает")
"""
    def eat(self):
        raise AttributeError("Роботы не едят!")
"""

if __name__ == "__main__":
    worker = RobotWorker()
    worker.work()
    # worker.eat()
