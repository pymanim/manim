from manim import *
class PolygonSample(Scene):
    def construct(self):
        self._reguler_polygons()
        self.wait()

    def _reguler_polygons(self):
        p1 = RegularPolygon(n=6)  # 正六边形
        p2 = RegularPolygon(n=8)  # 正八边形
        p3 = RegularPolygon(n=10)  # 正十边形

        vg = VGroup(p1, p2, p3)
        vg.arrange(RIGHT, buff=SMALL_BUFF)
        self.play(Create(vg))