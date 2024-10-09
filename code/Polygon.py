from manim import *
class PolygonSample(Scene):
    def construct(self):
        self._polygons()
        self.wait()

    def _polygons(self):
        p = Polygon([-3, 1, 0], [-1, 1, 0], [-2, -1, 0])
        self.play(Create(p), run_time=0.5)

        p = Polygon([1, 1, 0], [2, 0, 0], [3, 1, 0], [3, -1, 0], [1, -1, 0])
        self.play(Create(p), run_time=0.5)
