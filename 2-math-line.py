"""
实数平面（NumberPlane）的关键参数有4个：

    x_range：设置X轴的范围和间隔
    y_range：设置Y轴的范围和间隔
    x_length：设置X轴显示的长度
    y_length：设置Y轴显示的长度
"""
from manim import *
class num_line(Scene):
    def construct(self):
        a=NumberPlane(
            x_range=(-4, 11, 1),
            y_range=(-3, 3, 1),
            x_length=3,
            y_length=2,
        )
        b=NumberPlane(
            x_range=(-4, 11, 1),
            x_length=3,
            y_length=4,
        )
        self.play(Create(a), run_time=5)
        self.play(Create(b), run_time=5)