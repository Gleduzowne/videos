from manim import *

class TestScene(Scene):
    def construct(self):
        text = Text("Hello, World!", font_size=72)
        self.play(Write(text))
        self.wait(2)
