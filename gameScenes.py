import gameBase.py
from sys import exit


class Death(Scene):

    death_message = "I'm actually not sure how you managed to die..."

    def enter(self):
        print death_message
        exit(1)


class FirstRoom(Scene):

    def enter(self):
        pass


class SecondRoom(Scene):

    def enter(self):
        pass


class ThirdRoom(Scene):

    def enter(self):
        pass


class FourthRoom(Scene):

    def enter(self):
        pass


class FinalRoom(Scene):

    def enter(self):
        pass


class Ending(Scene):

    def enter(self):
        print "You win!"
        return 'ending'
