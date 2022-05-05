from turtle import Turtle
from math import sqrt

class SerpinksiCurve(Turtle):
    def draw(self, depth: int, size: float = 20) -> None:
        self.draw_half(depth, size)
        self.right(90)
        self.forward(size)
        self.right(90)

        self.draw_half(depth, size)
        self.right(90)
        self.forward(size)
        self.right(90)

        self.draw_half(depth, size)
        self.right(90)
        self.forward(size)
        self.right(90)

    def draw_half(self, depth, size) -> None:
        if depth > 0:
            self.draw_half(depth-1, size)
            self.left(45)
            self.forward(size * sqrt(2))
            self.left(45)

            self.draw_half(depth-1, size)
            self.right(90)
            self.forward(size)
            self.right(90)

            self.draw_half(depth-1, size)
            self.left(45)
            self.forward(size * sqrt(2))
            self.left(45)

            self.draw_half(depth-1, size)


SerpinksiCurve().draw(3)