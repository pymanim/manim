from manim import *
class LineSample(Scene):
    def construct(self):
        self._lines()

    def _lines(self):
        # 绘制 3 条线
        l = Line([-1, 1, 0], [1, 1, 0])
        self.play(Create(l), run_time=0.5)

        l = Line([-1, 0, 0], [1, 0, 0])
        self.play(Create(l), run_time=0.5)

        l = Line([-1, -1, 0], [1, -1, 0])
        self.play(Create(l), run_time=0.5)
