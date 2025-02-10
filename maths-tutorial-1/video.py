from manim import *

class AIAlgebraVideo(Scene):
    def construct(self):
        # Opening sequence
        self.opening_sequence()
        
        # Title sequence
        self.title_sequence()
        
        # Main content
        self.algebra_section()
        self.algorithm_section()
        self.applications_section()
        
        # Closing sequence
        self.closing_sequence()

    def opening_sequence(self):
        # Create network effect
        dots = VGroup(*[Dot() for _ in range(6)]).arrange_in_grid(2, 3, buff=2)
        lines = VGroup()
        for i, d1 in enumerate(dots):
            for j, d2 in enumerate(dots[i+1:], i+1):
                lines.add(Line(d1.get_center(), d2.get_center(), stroke_opacity=0.3))
        
        network = VGroup(dots, lines)
        
        # Add title text
        title = Text("Artificial Intelligence", font_size=72)
        subtitle = Text("The Mathematics Behind the Magic", font_size=48)
        VGroup(title, subtitle).arrange(DOWN, buff=0.5)
        
        # Animate
        self.play(Create(network), run_time=2)
        self.play(
            Write(title),
            Write(subtitle),
        )
        self.wait()
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

    def title_sequence(self):
        title = Text("Algebra & Algorithms", font_size=72)
        subtitle = Text("The Core of AI", font_size=48)
        VGroup(title, subtitle).arrange(DOWN, buff=0.5)
        
        self.play(
            Write(title),
            Write(subtitle)
        )
        self.wait()
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

    def algebra_section(self):
        # Vector space visualization
        plane = NumberPlane(
            x_range=[-5, 5],
            y_range=[-5, 5],
            background_line_style={
                "stroke_opacity": 0.4
            }
        )
        
        title = Text("Linear Algebra", font_size=48).to_edge(UP)
        
        # Create vector
        vector = Arrow(ORIGIN, [2, 3, 0], buff=0, color=YELLOW)
        vector_label = MathTex(r"\vec{v}").next_to(vector.get_end(), RIGHT)
        
        self.play(
            Create(plane),
            Write(title)
        )
        self.wait()
        
        self.play(
            Create(vector),
            Write(vector_label)
        )
        self.wait()
        
        # Transform to matrix
        matrix = MathTex(r"\begin{bmatrix} 2 \\ 3 \end{bmatrix}").shift(RIGHT * 3)
        self.play(
            TransformFromCopy(vector, matrix)
        )
        self.wait()
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

    def algorithm_section(self):
        title = Text("Algorithms", font_size=48).to_edge(UP)
        
        # Create flowchart
        start = Rectangle(width=2, height=1).shift(UP * 2)
        process = Rectangle(width=2, height=1)
        end = Rectangle(width=2, height=1).shift(DOWN * 2)
        
        arrows = VGroup(
            Arrow(start.get_bottom(), process.get_top()),
            Arrow(process.get_bottom(), end.get_top())
        )
        
        labels = VGroup(
            Text("Input", font_size=24).move_to(start),
            Text("Process", font_size=24).move_to(process),
            Text("Output", font_size=24).move_to(end)
        )
        
        flowchart = VGroup(start, process, end, arrows, labels)
        
        self.play(
            Write(title)
        )
        self.play(
            Create(flowchart)
        )
        self.wait()
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

    def applications_section(self):
        title = Text("AI Applications", font_size=48).to_edge(UP)
        
        applications = VGroup(
            Text("Computer Vision"),
            Text("Natural Language Processing"),
            Text("Recommendation Systems")
        ).arrange(DOWN, buff=1)
        
        self.play(
            Write(title)
        )
        self.play(
            LaggedStart(*[Write(app) for app in applications])
        )
        self.wait()
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

    def closing_sequence(self):
        thanks = Text("Thanks for watching!", font_size=72)
        subscribe = Text("Subscribe for more AI & Math content", font_size=36)
        
        VGroup(thanks, subscribe).arrange(DOWN, buff=1)
        
        self.play(
            Write(thanks)
        )
        self.play(
            Write(subscribe)
        )
        self.wait()
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
