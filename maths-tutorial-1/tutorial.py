from manim import *

# Added definitions for Diamond and Parallelogram:
class Diamond(Polygon):
    def __init__(self, width=1, **kwargs):
        # Create a diamond as a square rotated by 45 degrees
        points = [UP * width, RIGHT * width, DOWN * width, LEFT * width]
        super().__init__(*points, **kwargs)

class Parallelogram(Polygon):
    def __init__(self, width=1, height=1, slant=0.3, **kwargs):
        # Define vertices: (0,0), (width,0), (width+slant,height), (slant,height)
        points = [ORIGIN, RIGHT * width, RIGHT * width + UP * height + RIGHT * slant, UP * height + RIGHT * slant]
        super().__init__(*points, **kwargs)

class IntroScene(Scene):
    def construct(self):
        dot = Dot()
        lines = VGroup(*[Line(dot.get_center(), [x, y, 0]) for x, y in [(-2, 1), (2, -1), (1, 2), (-1, -2)]])
        network = VGroup(dot, *lines)
        ai_text = Text("AI", font_size=72).move_to(dot.get_center())
        self.animations = [Create(network), Write(ai_text), Wait(2), FadeOut(network), FadeOut(ai_text)]
        self.play(*self.animations)

class TitleCard(Scene):
    def construct(self):
        title = Text("AI: Algebra and Algorithms", font_size=72)
        self.animations = [FadeIn(title), Wait(2), FadeOut(title)]
        self.play(*self.animations)

class AlgebraIntro(Scene):
    def construct(self):
        axes = NumberPlane()
        dots = VGroup(*[Dot([x, y, 0]) for x, y in [(1, 2), (-2, -1), (3, 1), (-1, -3)]])
        labels = VGroup(
            Text("Feature 1").next_to(axes.x_axis, RIGHT),
            Text("Feature 2").next_to(axes.y_axis, UP)
        )
        self.animations = [Create(axes), Create(dots), Write(labels), Wait(2)]
        self.play(*self.animations)

class VectorRepresentation(Scene):
    def construct(self):
        dot = Dot([2, 3, 0])
        vector = Arrow(ORIGIN, dot.get_center(), buff=0)
        components = VGroup(
            DashedLine(ORIGIN, [2, 0, 0]),
            DashedLine([2, 0, 0], dot.get_center())
        )
        braces = VGroup(
            Brace(components[0], DOWN),
            Brace(components[1], RIGHT)
        )
        labels = VGroup(
            braces[0].get_text("2"),
            braces[1].get_text("3")
        )
        self.animations = [Create(dot), Create(vector), Create(components), Create(braces), Write(labels), Wait(2)]
        self.play(*self.animations)

class MatrixRepresentation(Scene):
    def construct(self):
        vectors = VGroup(
            Arrow(ORIGIN, [2, 3, 0], buff=0),
            Arrow(ORIGIN, [-1, 2, 0], buff=0),
            Arrow(ORIGIN, [3, -1, 0], buff=0)
        )
        matrix = MobjectMatrix(
            [[MathTex("2"), MathTex("3")], [MathTex("-1"), MathTex("2")], [MathTex("3"), MathTex("-1")]],
            left_bracket="(", right_bracket=")"
        ).scale(0.75).to_edge(RIGHT)
        self.animations = [Create(vectors), Wait(1), Transform(vectors, matrix), Wait(2)]
        self.play(*self.animations)

class ImageRepresentation(Scene):
    def construct(self):
        image = Square().scale(2)
        grid = NumberPlane(x_range=[0, 4, 1], y_range=[0, 4, 1]).scale(0.5).move_to(image.get_center())
        numbers = VGroup(*[Text(str(i)).move_to(grid.c2p(x, y)) for i, (x, y) in enumerate([(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2), (0, 3), (1, 3), (2, 3), (3, 3)])])
        self.animations = [Create(image), Create(grid), Write(numbers), Wait(2)]
        self.play(*self.animations)

class BuildingBlocks(Scene):
    def construct(self):
        shapes = VGroup(Square(), Circle(), Triangle()).arrange(RIGHT, buff=1)
        complex_shape = VGroup(*[sh.copy().shift(UP * i) for i, sh in enumerate(shapes)])
        ai_icon = Text("AI", font_size=72).move_to(complex_shape.get_center())
        self.animations = [Create(shapes), Wait(1), Transform(shapes, complex_shape), Wait(1), Write(ai_icon), Wait(2)]
        self.play(*self.animations)

class AlgorithmIntro(Scene):
    def construct(self):
        flowchart = VGroup(
            Rectangle().shift(UP * 2),
            Arrow(UP, DOWN),
            Diamond().shift(DOWN),
            Arrow(DOWN, DOWN * 2),
            Parallelogram().shift(DOWN * 3)
        )
        labels = VGroup(
            Text("Input Data (Matrix)").next_to(flowchart[0], UP),
            Text("Algorithm (Process)").next_to(flowchart[2], RIGHT),
            Text("Output (Result)").next_to(flowchart[4], DOWN)
        )
        self.animations = [Create(flowchart), Write(labels), Wait(2)]
        self.play(*self.animations)

class SearchAlgorithm(Scene):
    def construct(self):
        matrix = MobjectMatrix(
            [
                [MathTex("1"), MathTex("2")],
                [MathTex("3"), MathTex("4")]
            ],
            left_bracket="(", right_bracket=")"
        ).scale(0.75).to_edge(LEFT)
        magnifying_glass = Circle().scale(0.5).move_to(matrix.get_center())
        self.animations = [Create(matrix), Create(magnifying_glass), Wait(1), 
                           magnifying_glass.animate.move_to(matrix.get_entries()[3].get_center()), Wait(2)]
        self.play(*self.animations)

class SortingAlgorithm(Scene):
    def construct(self):
        bars = VGroup(*[Rectangle(height=h, width=0.5).shift(UP * h / 2) for h in [1, 3, 2, 4]])
        sorted_bars = VGroup(*[Rectangle(height=h, width=0.5).shift(UP * h / 2) for h in [1, 2, 3, 4]])
        self.animations = [Create(bars), Wait(1), Transform(bars, sorted_bars), Wait(2)]
        self.play(*self.animations)

class MachineLearningAlgorithm(Scene):
    def construct(self):
        layers = VGroup(
            VGroup(*[Dot().shift(UP * i) for i in range(-2, 3)]).shift(LEFT * 3),
            VGroup(*[Dot().shift(UP * i) for i in range(-2, 3)]),
            VGroup(*[Dot().shift(UP * i) for i in range(-2, 3)]).shift(RIGHT * 3)
        )
        connections = VGroup(*[Line(start.get_center(), end.get_center()) for start in layers[0] for end in layers[1]] + [Line(start.get_center(), end.get_center()) for start in layers[1] for end in layers[2]])
        self.animations = [Create(layers), Create(connections), Wait(2)]
        self.play(*self.animations)

class RecipeBook(Scene):
    def construct(self):
        book = Square().scale(2)
        flowcharts = VGroup(
            VGroup(Rectangle(), Arrow(), Diamond(), Arrow(), Parallelogram()).arrange(DOWN, buff=0.5),
            VGroup(Rectangle(), Arrow(), Diamond(), Arrow(), Parallelogram()).arrange(DOWN, buff=0.5).shift(RIGHT * 2)
        )
        self.animations = [Create(book), Wait(1), Create(flowcharts), Wait(2)]
        self.play(*self.animations)

class FaceRecognition(Scene):
    def construct(self):
        face = Circle().scale(2)
        matrix = MobjectMatrix(
            [[1, 2], [3, 4]],
            left_bracket="(", right_bracket=")"
        ).scale(0.75).to_edge(RIGHT)
        features = VGroup(
            Rectangle().move_to(face.point_from_proportion(0.25)),
            Rectangle().move_to(face.point_from_proportion(0.75)),
            Rectangle().move_to(face.point_from_proportion(0.5))
        )
        self.animations = [Create(face), Create(matrix), Wait(1), Create(features), Wait(2)]
        self.play(*self.animations)

class LanguageTranslation(Scene):
    def construct(self):
        text = Text("Hello World").to_edge(UP)
        vectors = VGroup(
            Arrow(ORIGIN, [1, 2, 0], buff=0),
            Arrow(ORIGIN, [-1, 2, 0], buff=0),
            Arrow(ORIGIN, [3, -1, 0], buff=0)
        ).shift(DOWN)
        translated_text = Text("Bonjour le monde").to_edge(DOWN)
        self.animations = [Write(text), Create(vectors), Wait(1), Transform(text, translated_text), Wait(2)]
        self.play(*self.animations)

class RecommendationSystem(Scene):
    def construct(self):
        user_vector = Arrow(ORIGIN, [2, 3, 0], buff=0).set_color(BLUE)
        item_vectors = VGroup(
            Arrow(ORIGIN, [1, 2, 0], buff=0).set_color(GREEN),
            Arrow(ORIGIN, [3, 1, 0], buff=0).set_color(GREEN),
            Arrow(ORIGIN, [2, 3, 0], buff=0).set_color(RED)
        )
        self.animations = [Create(user_vector), Create(item_vectors), Wait(1), item_vectors[2].animate.set_color(YELLOW), Wait(2)]
        self.play(*self.animations)

class AIApplications(Scene):
    def construct(self):
        applications = VGroup(
            Text("Medical Diagnosis").shift(UP * 3),
            Text("Fraud Detection").shift(UP * 1.5),
            Text("Self-Driving Cars").shift(DOWN * 1.5),
            Text("More...").shift(DOWN * 3)
        )
        self.animations = [Write(applications), Wait(2)]
        self.play(*self.animations)

class OutroScene(Scene):
    def construct(self):
        dot = Dot()
        lines = VGroup(*[Line(dot.get_center(), [x, y, 0]) for x, y in [(-2, 1), (2, -1), (1, 2), (-1, -2)]])
        network = VGroup(dot, *lines)
        ai_text = Text("Algebra & Algorithms: The Foundation of AI", font_size=48).move_to(dot.get_center())
        self.animations = [Create(network), Write(ai_text), Wait(2), FadeOut(network), FadeOut(ai_text)]
        self.play(*self.animations)

class EndScreen(Scene):
    def construct(self):
        title = Text("AI: Algebra and Algorithms", font_size=48).to_edge(UP)
        subscribe = Text("Subscribe for more!", font_size=36).next_to(title, DOWN)
        self.animations = [FadeIn(title), Write(subscribe), Wait(2)]
        self.play(*self.animations)
