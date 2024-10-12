from manim import *
class CircleSample(Scene):
    def construct(self):
        self._circles()
        self.wait()

    def _circles(self):
        c = Circle(radius=1)
        self.play(Create(c), run_time=0.5)

        c = Circle(radius=2)
        self.play(Create(c), run_time=0.5)

        c = Circle(radius=3)
        self.play(Create(c), run_time=0.5)