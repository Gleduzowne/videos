from manim import *
from video import create_ai_fundamentals_video
import os
import sys

class AIFundamentals(Scene):
    def construct(self):
        video_structure = create_ai_fundamentals_video()

        # Keep a persistent background (e.g., a subtle rotating gradient).
        background = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=GREY_E,
            fill_opacity=1
        )
        background.rotate(0.05)
        self.add(background)
        self.play(background.animate.rotate(0.1), run_time=2)

        for scene_index, scene in enumerate(video_structure):
            # Brief conceptual label to identify the scene idea (optional).
            label = Text(f"Scene Concept {scene_index+1}", color=YELLOW).scale(0.6).to_corner(UL)
            self.play(FadeIn(label))

            # Conceptual shape(s) to illustrate the idea.
            # Example: a dynamic network morph for AI concept demonstration.
            dots = VGroup(*[Dot(color=BLUE).scale(0.7) for _ in range(5)])
            dots.arrange_in_grid(rows=1, buff=1)
            network_lines = VGroup()
            for i in range(len(dots) - 1):
                line = Line(dots[i].get_center(), dots[i+1].get_center(), color=BLUE_E)
                network_lines.add(line)
            self.play(FadeIn(dots, shift=DOWN), Create(network_lines))

            # Animate shapes to reflect evolution or transformation.
            self.play(dots.animate.arrange_in_grid(rows=5, buff=0.4).scale(0.4), run_time=2)
            self.play(Rotate(network_lines, angle=PI / 2), run_time=2)

            # Transform into more complex shape (e.g., polygon).
            polygon = RegularPolygon(n=6, color=GREEN).scale(2)
            self.play(Transform(VGroup(dots, network_lines), polygon), run_time=2)

            # Minimal wait time so there's never an empty screen.
            self.wait(scene.duration * 0.4)

            # Clean up shapes but keep background visible.
            self.play(FadeOut(label), FadeOut(polygon))

            # Slight transition effect before next scene.
            self.play(background.animate.rotate(0.05), run_time=1)

        # Final flourish or no fade to black, just hold the last frame.
        self.wait(2)
