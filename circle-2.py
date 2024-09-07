from manim import *
class CircleSample(Scene):
    def construct(self):
        self._arcs()
        self.wait()

    def _arcs(self):
        # 90度圆弧，半径1
        a = Arc(angle=PI / 2, radius=1)
        self.play(Create(a), run_time=0.5)

        # 180度圆弧，半径2
        a = Arc(angle=PI, radius=2)
        self.play(Create(a), run_time=0.5)

        # 30度圆弧，半径2，从270度开始绘制
        a = Arc(angle=PI / 6, start_angle=PI * 1.5, radius=2)
        self.play(Create(a), run_time=0.5)
