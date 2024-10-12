# 线

manim的线其实都是线段，绘制线只要提供两个点的坐标。

提供任意2个点，manim通过`Line`来绘制线。
``` python
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
```
运行程序
``` bash
manim -p .\line.py
```
其中，带箭头的线为`Arrow`，虚线为`DashedLine`
他们的用法和`Line`一样，都是提供两个点的坐标。