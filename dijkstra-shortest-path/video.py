from manim import *

class DijkstraShortestPath(Scene):
    def construct(self):
        # Title and intro
        title = Text("How Google Maps Finds the Shortest Route").scale(0.8).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        intro = Text("Powered by Dijkstra's Algorithm", font_size=36).next_to(title, DOWN)
        self.play(FadeIn(intro))
        self.wait(2)
        self.play(FadeOut(intro))

        # Draw a simple map (graph)
        nodes_pos = [
            [-3, 1, 0],   # A
            [0, 2, 0],    # B
            [3, 1, 0],    # C
            [-2, -1, 0],  # D
            [2, -1, 0],   # E
        ]
        node_names = ["A", "B", "C", "D", "E"]
        nodes = [Dot(pos, color=WHITE) for pos in nodes_pos]
        node_labels = [Text(name, font_size=32).next_to(nodes[i], LEFT if i in [0,3] else (RIGHT if i in [2,4] else UP)) for i, name in enumerate(node_names)]
        edges = [
            (0, 1, 2),  # A-B
            (1, 2, 3),  # B-C
            (0, 3, 1),  # A-D
            (3, 4, 4),  # D-E
            (4, 2, 2),  # E-C
            (1, 4, 1),  # B-E
        ]
        edge_objs = []
        edge_labels = []
        for i, j, w in edges:
            edge = Line(nodes[i].get_center(), nodes[j].get_center(), color=GREY)
            edge_objs.append(edge)
            label_pos = (nodes[i].get_center() + nodes[j].get_center())/2
            edge_labels.append(Text(str(w), font_size=28).move_to(label_pos + 0.3*(UP if i<j else DOWN)))
        # Draw edges
        for edge in edge_objs:
            self.play(Create(edge), run_time=0.3)
        # Draw nodes and labels
        for node, label in zip(nodes, node_labels):
            self.play(FadeIn(node), Write(label), run_time=0.2)
        for label in edge_labels:
            self.play(Write(label), run_time=0.1)
        self.wait(1)

        # Step-by-step Dijkstra's algorithm (forced pacing with dummy animations)
        # 1. Start at A
        self.play(nodes[0].animate.set_color(YELLOW))
        self.play(FadeIn(VMobject(), run_time=6))
        # 2. Explore neighbors (A->B, A->D)
        self.play(edge_objs[0].animate.set_color(BLUE))
        self.play(FadeIn(VMobject(), run_time=4))
        self.play(edge_objs[2].animate.set_color(BLUE))
        self.play(FadeIn(VMobject(), run_time=4))
        # 3. Mark D as next (shortest from A)
        self.play(nodes[3].animate.set_color(GREEN))
        self.play(FadeIn(VMobject(), run_time=6))
        # 4. Explore D's neighbor (D->E)
        self.play(edge_objs[3].animate.set_color(BLUE))
        self.play(FadeIn(VMobject(), run_time=4))
        self.play(nodes[4].animate.set_color(GREEN))
        self.play(FadeIn(VMobject(), run_time=6))
        # 5. Explore E's neighbor (E->C)
        self.play(edge_objs[4].animate.set_color(BLUE))
        self.play(FadeIn(VMobject(), run_time=4))
        self.play(nodes[2].animate.set_color(RED))
        self.play(FadeIn(VMobject(), run_time=6))
        # 6. Highlight final path (A-D-E-C)
        for idx in [2, 3, 4]:
            self.play(edge_objs[idx].animate.set_color(RED), run_time=2.5)
            self.play(FadeIn(VMobject(), run_time=2.5))
        self.play(FadeIn(VMobject(), run_time=8))

        # Show all distances (simulate table, row by row, much slower)
        table_data = [
            ["Node", "Distance from A", "Previous"],
            ["A", "0", "-"],
            ["B", "2", "A"],
            ["C", "5", "E"],
            ["D", "1", "A"],
            ["E", "5", "D"],
        ]
        table = Table([table_data[0]]).scale(0.7).to_edge(DOWN)
        self.play(FadeIn(table))
        self.play(FadeIn(VMobject(), run_time=4))
        for row in table_data[1:]:
            new_table = Table([table_data[0]] + table_data[1:table_data.index(row)+1]).scale(0.7).to_edge(DOWN)
            self.play(Transform(table, new_table))
            self.play(FadeIn(VMobject(), run_time=5))
        self.play(FadeIn(VMobject(), run_time=8))
        self.play(FadeOut(table))

        # Real-world context
        context = Text("Google Maps runs this algorithm\nfor millions of users every day!", font_size=36).next_to(title, DOWN)
        self.play(Write(context))
        self.wait(5)
        self.play(FadeOut(context))

        # Summary
        summary = Text("Dijkstras algorithm helps you\nget to your destination quickly!", font_size=36).move_to(ORIGIN)
        self.play(Write(summary))
        self.wait(5)
        self.play(FadeOut(summary), FadeOut(title))
        self.wait(2)

        # End
        self.play(*[FadeOut(mobj) for mobj in nodes+node_labels+edge_objs+edge_labels])
        self.wait(2)


        # End
        self.play(*[FadeOut(mobj) for mobj in nodes+node_labels+edge_objs+edge_labels])
        self.wait(1)
