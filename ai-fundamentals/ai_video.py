from manim import *
from video import create_ai_fundamentals_video  # Import the scene data
import os
import sys

class AIFundamentals(Scene):
    def construct(self):
        video_structure = create_ai_fundamentals_video()

        for i, scene in enumerate(video_structure):
            # Background
            bg = Rectangle(width=config.frame_width, height=config.frame_height,
                           fill_color=BLUE_E, fill_opacity=0.5)
            self.play(FadeIn(bg))

            # Scene Title
            title = Text(scene.name, color=YELLOW).scale(1.2).to_edge(UP)
            self.play(Write(title))

            # Scene Content
            content = Paragraph(scene.content, alignment="left", width=7).shift(DOWN*0.5)
            self.play(FadeIn(content))

            # Sample Animation (circle demonstration)
            circle = Circle(radius=1, color=RED)
            self.play(Create(circle))
            self.play(circle.animate.shift(LEFT*2).rotate(PI))
            self.play(Uncreate(circle))

            # Cleanup before next scene
            self.play(FadeOut(title), FadeOut(content), FadeOut(bg))
            self.wait(scene.duration)
