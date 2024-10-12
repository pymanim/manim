"""
数轴（NumberLine）是最基本的一维坐标系，它的关键参数是：

    x_range：设置数轴的范围和间隔
    length：设置数轴显示的长度

"""
from manim import *
class num_line(Scene):
    def construct(self):
        a=NumberLine(x_range=[-10, 10, 2], length=10, include_numbers=True)
        b=NumberLine(x_range=[-3, 3, 0.5], length=12, include_numbers=True)
        c=NumberLine(
            x_range=[-5, 5 + 1, 1],
            length=6,
            include_numbers=True,
            include_tip=True,
            rotation=10 * DEGREES,#DEGREES = 2*PI / 360
        )
        self.play(Create(a), run_time=5)
        self.play(Create(b), run_time=5)
        self.play(Create(c), run_time=5)