# 点
from manim import *
class DotSample(Scene):
    def construct(self):
        # 绘制 9个点
        for x in range(-1, 2):
            for y in range(1, -2, -1):
                p = Dot([x, y, 0])
                self.play(Create(p), run_time=0.5)

