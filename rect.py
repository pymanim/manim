from manim import *
class PolygonSample(Scene):
    def construct(self):
        self._rectangles()
        self.wait()

    def _rectangles(self):
        r = Rectangle(width=1.5, height=1)
        self.play(Create(r), run_time=0.5)

        r = Rectangle(width=2, height=1.5)
        self.play(Create(r), run_time=0.5)

        r = Rectangle(width=3, height=2)
        self.play(Create(r), run_time=0.5)
