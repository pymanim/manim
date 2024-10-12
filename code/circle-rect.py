from manim import *
class PolygonSample(Scene):
    def construct(self):
        self._rounded_rectangles()
        self.wait()

    def _rounded_rectangles(self):
        r = RoundedRectangle(corner_radius=0.2, width=1.5, height=1)
        self.play(Create(r), run_time=0.5)

        r = RoundedRectangle(corner_radius=0.4, width=2, height=1.5)
        self.play(Create(r), run_time=0.5)

        r = RoundedRectangle(corner_radius=0.6, width=3, height=2)
        self.play(Create(r), run_time=0.5)
