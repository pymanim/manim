from manim import *
class PolygonSample(Scene):
    def construct(self):
        self._squares()
        self.wait()

    def _squares(self):
        s = Square(side_length=1)
        self.play(Create(s), run_time=0.5)

        s = Square(side_length=1.5)
        self.play(Create(s), run_time=0.5)

        s = Square(side_length=2)
        self.play(Create(s), run_time=0.5)