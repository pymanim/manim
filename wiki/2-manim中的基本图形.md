# 点

**点**是最简单图形，也是其他所有图形的基础。
 绘制其他任何图形时，都是用**点**来定位的。

`manim`中生成一个点很方便，只要给定一个坐标即可。
 这里的坐标包含 `[x, y, z]`3个维度，如果绘制二维图形，将第三个坐标 `z`固定为 `0`。

``` python
from manim import *
class DotSample(Scene):
    def construct(self):
        # 绘制 9个点
        for x in range(-1, 2):
            for y in range(1, -2, -1):
                p = Dot([x, y, 0])
                self.play(Create(p), run_time=0.5)
                self.wait() # 等待
```

按照 `3x3`的格式绘制9个点

```bash
manim -p .\samples.py DotSample
```

![out01](.\img\dot.gif)

