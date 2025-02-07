from manim import *

class GleduzowneLogo(Scene):
    def construct(self):
        # Define colors
        primary_color = "#4285F4"  # Google Blue
        secondary_color = "#DB4437" # Google Red
        accent_color = "#F4B400"    # Google Yellow
        experiment_color = "#0F9D58" # Google Green

        # Pipette shape (using Polygon)
        pipette = Polygon(
            [-0.2, 0, 0], [0.2, 0, 0], [0.2, 2, 0], [0.1, 2.5, 0], [-0.1, 2.5, 0], [-0.2, 2, 0],
            color=primary_color,
            fill_opacity=1
        ).scale(0.7)
        
        # Small circles for experimentation
        circles = VGroup(*[
            Circle(radius=0.08, color=experiment_color, fill_opacity=1).move_to([np.random.uniform(-0.5, 0.5), np.random.uniform(-0.5, 0.5), 0])
            for _ in range(15)
        ]).scale(0.7).next_to(pipette, DOWN, buff=0.2)

        # "Gl" shapes (using Text) - stylized
        gl_text = Text("Gl", font="Arial", color=accent_color).scale(2).move_to(pipette.get_center()).shift(UP * 1.2)
        
        # Background rectangle
        background_rect = Rectangle(width=6, height=4, color=BLACK, fill_opacity=0.2).move_to(ORIGIN)

        # Combine elements
        logo = VGroup(background_rect, pipette, circles, gl_text).move_to(ORIGIN)

        # Animation
        self.play(Create(background_rect))
        self.play(Create(pipette), Create(gl_text))
        self.play(FadeIn(circles, shift=UP))
        self.wait(2)
        self.play(FadeOut(logo))
