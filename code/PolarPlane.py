"""
极坐标系（PolarPlane）通过角度和与原点的距离来定位位置，经常被用于导航类的系统中，
与直角坐标相比，在这类系统中能极大的简化计算。
它的关键参数有：

    azimuth_step：分割的角度个数
    size：极坐标在屏幕中显示的大小
    radius_step：极坐标半径的间隔
    radius_max：极坐标最大半径
"""
from manim import *
class polar_math_line(Scene):
    def construct(self):
        a = PolarPlane(
            azimuth_step=30,
            size=6,
            radius_step=1,
            radius_max=3,
        ).add_coordinates()
        self.play(Create(a),run_time=5)
        self.wait()
