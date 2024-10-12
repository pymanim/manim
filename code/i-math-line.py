from manim import *
class i_math_line(Scene):
    def construct(self):
        plane = ComplexPlane().add_coordinates()# coordinates:坐标
        d1 = Dot(plane.n2p(2 + 1j), color=YELLOW)
        d2 = Dot(plane.n2p(-3 - 2j), color=YELLOW)
        label1 = Tex("2+i").next_to(d1, UR, 0.1)
        label2 = Tex("-3-2i").next_to(d2, UR, 0.1)
        self.play(Create(plane),run_time=1)
        self.play(Create(d1),run_time=1)
        self.play(Create(d2),run_time=1)
        self.play(Create(label1),run_time=1)
        self.play(Create(label2),run_time=1)
        self.wait() # 等待