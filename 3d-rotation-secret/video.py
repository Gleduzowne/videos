# video.py
class Scene:
    def __init__(self, scene_number, duration, camera, animations, voiceover):
        self.scene_number = scene_number
        self.duration = duration
        self.camera = camera
        self.animations = animations
        self.voiceover = voiceover

    def __repr__(self):
        return f"Scene(scene_number={self.scene_number}, duration={self.duration}, camera={self.camera}, animations={self.animations}, voiceover={self.voiceover})"

def create_3d_rotation_secret_video():
    """
    Creates scenes for the 3D Rotation Secret video.
    """
    scenes = [
        Scene(
            scene_number=1,
            duration=10,
            camera={"position": [3, 2, 5], "look_at": [0, 0, 0]},
            animations=[
                {"type": "Write", "object": "3D ROTATION?", "position": [0, 1, 0], "scale": 1.5, "creation_speed": 0.05},
                {"type": "Write", "object": "The Problem...", "position": [0, -1, 0], "scale": 1, "creation_speed": 0.03, "start_time": 3}
            ],
            voiceover={"script": "Tired of clunky, confusing 3D rotations? Ever feel like there's a better way? You're not alone. Let's talk about the hidden headache behind rotating objects in three dimensions...", "start_time": 0, "duration": 10}
        ),
        Scene(
            scene_number=2,
            duration=15,
            camera={"position": [4, 3, 6], "look_at": [0, 0, 0]},
            animations=[
                {"type": "Create", "object": "ThreeDVector", "label": "Original Vector", "start_point": [-1, -1, -1], "end_point": [1, 1, 1], "color": "YELLOW"},
                {"type": "Create", "object": "RotationMatrix", "axis": "[0, 0, 1]", "angle": "PI/4", "label": "Rotation Matrix", "position": [2, 1, 0]},
                {"type": "Transform", "initial_state": "Original Vector", "target_state": "Rotated Vector (via Matrix)", "matrix": "Rotation Matrix", "color": "GREEN", "start_time": 5},
                {"type": "Write", "object": "...Matrix Multiplication...", "position": [2, -1, 0], "scale": 0.7, "start_time": 8}
            ],
            voiceover={"script": "The standard approach? Rotation matrices. Multiply your 3D vector by this 3x3 grid of numbers... and voila! Rotation. But under the hood, it's a lot of multiplication and can lead to issues like gimbal lock.", "start_time": 0, "duration": 15}
        ),
        Scene(
            scene_number=3,
            duration=15,
            camera={"position": [5, 4, 7], "look_at": [0, 0, 0]},
            animations=[
                {"type": "Create", "object": "Quaternion", "values": "[w, x, y, z]", "position": [-2, 1, 0], "scale": 1.2},
                {"type": "Write", "object": "Enter: Quaternions!", "position": [-2, -1, 0], "scale": 1, "creation_speed": 0.04},
                {"type": "Explain", "object": "Quaternion", "parts": [{"part": "w", "explanation": "Real part (angle)"}, {"part": "x, y, z", "explanation": "Vector part (axis)"}], "start_time": 5}
            ],
            voiceover={"script": "What if I told you there's a more elegant way? Enter... quaternions! These mysterious four-dimensional numbers might look intimidating, but they beautifully encode both the axis of rotation and the angle in a single entity.", "start_time": 0, "duration": 15}
        ),
        Scene(
            scene_number=4,
            duration=25,
            camera={"position": [4, 3, 6], "look_at": [0, 0, 0]},
            animations=[
                {"type": "Create", "object": "UnitSphere", "radius": 1, "opacity": 0.5},
                {"type": "Create", "object": "Arrow", "start": [0, 0, 0], "end": [1, 0, 0], "color": "RED", "label": "Vector to Rotate"},
                {"type": "AnimateRotation", "object": "Arrow", "axis": "[0, 0, 1]", "angle": "PI/3", "run_time": 5},
                {"type": "Create", "object": "Quaternion", "values": "[cos(PI/6), 0, 0, sin(PI/6)]", "position": [2, 1, 0], "scale": 0.8, "start_time": 7},
                {"type": "Write", "object": "Quaternion Magic!", "position": [2, -1, 0], "scale": 0.7, "start_time": 10},
                {"type": "Transform", "initial_state": "Original Vector", "target_state": "Rotated Vector (via Quaternion)", "quaternion": "[cos(PI/6), 0, 0, sin(PI/6)]", "color": "BLUE", "start_time": 15},
                {"type": "CompareTransformations", "transformation1_label": "Matrix Rotation", "transformation2_label": "Quaternion Rotation", "vector": "Initial Vector", "matrix": "Rotation Matrix (same as before)", "quaternion": "[cos(PI/6), 0, 0, sin(PI/6)]", "start_time": 20}
            ],
            voiceover={"script": "See this vector? With quaternions, rotating it is like performing a single, elegant operation. No complex matrix multiplications, just a quaternion multiplication involving your vector and the rotation quaternion. Notice how smoothly it rotates!", "start_time": 0, "duration": 25}
        ),
        Scene(
            scene_number=5,
            duration=20,
            camera={"position": [5, 3, 7], "look_at": [0, 0, 0]},
            animations=[
                {"type": "Write", "object": "Why Quaternions Rule:", "position": [0, 1.5, 0], "scale": 1.2, "creation_speed": 0.04},
                {"type": "BulletedList", "items": ["No Gimbal Lock!", "More Compact", "Efficient Interpolation"], "position": [0, 0, 0]},
                {"type": "ShowCreation", "object": "GimbalLockVisualization", "start_time": 10}
            ],
            voiceover={"script": "But the benefits don't stop there! Quaternions completely avoid the dreaded gimbal lock, are more memory-efficient, and allow for smoother and more natural-looking interpolations between rotations. This is why they're the secret weapon in many 3D applications, from video games to robotics.", "start_time": 0, "duration": 20}
        ),
        Scene(
            scene_number=6,
            duration=15,
            camera={"position": [3, 2, 5], "look_at": [0, 0, 0]},
            animations=[
                {"type": "Write", "object": "Unlock the Power!", "position": [0, 1, 0], "scale": 1.3, "creation_speed": 0.05},
                {"type": "CallToAction", "text": "Learn more in the description!", "position": [0, -0.5, 0], "scale": 0.8, "color": "BLUE"},
                {"type": "SocialMediaIcons", "platforms": ["YouTube", "Twitter", "Patreon"], "scale": 0.5, "position": [0, -1.5, 0]}
            ],
            voiceover={"script": "Ready to ditch the matrix madness and unlock the power of quaternion rotations? Dive deeper with the resources in the description below! Like, subscribe, and let us know what other mathematical secrets you want us to reveal!", "start_time": 0, "duration": 15}
        )
    ]
    return scenes

from manim import *
import numpy as np

# Scene 1: Introduction
class Scene1(ThreeDScene):
    def construct(self):
        # Set camera position to [3, 2, 5] looking at [0, 0, 0]
        self.move_camera(phi=60 * DEGREES, theta=45 * DEGREES, frame_center=[0, 0, 0], distance=7)
        # Title
        title = Text("3D ROTATION?", font_size=72).move_to([0, 1, 0]).scale(1.5)
        subtitle = Text("The Problem...", font_size=48).move_to([0, -1, 0]).scale(1)
        # Write title
        self.play(Write(title, run_time=2))
        # Wait until start_time for subtitle (3 seconds after start)
        self.wait(3)
        # Write subtitle
        self.play(Write(subtitle, run_time=1.5))
        self.wait(2)

# Scene 2: Matrix Rotation
class Scene2(ThreeDScene):
    def construct(self):
        # Set camera position to [4, 3, 6] looking at [0, 0, 0]
        self.move_camera(phi=53 * DEGREES, theta=56 * DEGREES, frame_center=[0, 0, 0], distance=8)
        axes = ThreeDAxes()
        self.add(axes)
        # Original Vector
        orig_vec = Arrow3D(start=[-1, -1, -1], end=[1, 1, 1], color=YELLOW)
        orig_label = Text("Original Vector", font_size=32).next_to(orig_vec.get_end(), UP)
        self.play(Create(orig_vec), Write(orig_label))
        # Rotation Matrix (valid LaTeX)
        rot_matrix = Matrix([[r"\cos(\frac{\pi}{4})", r"-\sin(\frac{\pi}{4})", "0"],
                             [r"\sin(\frac{\pi}{4})", r"\cos(\frac{\pi}{4})", "0"],
                             ["0", "0", "1"]])
        rot_matrix.scale(0.7).move_to([2, 1, 0])
        rot_label = Text("Rotation Matrix", font_size=28).next_to(rot_matrix, DOWN)
        self.play(FadeIn(rot_matrix), Write(rot_label))
        self.wait(1)
        # Rotated Vector (simulate rotation by PI/4 about z)
        rotated_vec = Arrow3D(start=[-1, -1, -1], end=[np.sqrt(2), 0, 1], color=GREEN)
        rot_label2 = Text("Rotated Vector (via Matrix)", font_size=28).next_to(rotated_vec.get_end(), UP)
        self.play(Transform(orig_vec, rotated_vec), Write(rot_label2), run_time=2)
        self.wait(1)
        # Matrix Multiplication Text
        matrix_mult = Text("...Matrix Multiplication...", font_size=32).move_to([2, -1, 0])
        self.play(Write(matrix_mult))
        self.wait(1)

# Scene 3: Quaternions Intro
class Scene3(ThreeDScene):
    def construct(self):
        # Set camera position to [5, 4, 7] looking at [0, 0, 0]
        self.move_camera(phi=60 * DEGREES, theta=53 * DEGREES, frame_center=[0, 0, 0], distance=9)
        # Quaternion object
        quat = Text("Quaternion: [w, x, y, z]", font_size=40).move_to([-2, 1, 0]).scale(1.2)
        self.play(Write(quat))
        self.wait(1)
        # Enter Quaternions
        enter = Text("Enter: Quaternions!", font_size=36).move_to([-2, -1, 0]).scale(1)
        self.play(Write(enter))
        self.wait(1)
        # Explanation overlays (after 5 seconds)
        self.wait(3)  # To reach 5s from start
        w_part = Text("w: Real part (angle)", font_size=28).move_to([1, 0.5, 0])
        xyz_part = Text("x, y, z: Vector part (axis)", font_size=28).move_to([1, -0.5, 0])
        self.play(Write(w_part), Write(xyz_part))
        self.wait(1)

# Scene 4: Quaternion Rotation
class Scene4(ThreeDScene):
    def construct(self):
        # Set camera position to [4, 3, 6] looking at [0, 0, 0]
        self.move_camera(phi=53 * DEGREES, theta=56 * DEGREES, frame_center=[0, 0, 0], distance=8)
        axes = ThreeDAxes()
        self.add(axes)
        # Unit Sphere
        sphere = Sphere(radius=1, fill_opacity=0.5, color=BLUE).move_to([0, 0, 0])
        self.play(FadeIn(sphere))
        # Arrow to rotate
        arrow = Arrow3D(start=[0, 0, 0], end=[1, 0, 0], color=RED)
        arrow_label = Text("Vector to Rotate", font_size=28).next_to(arrow.get_end(), UP)
        self.play(Create(arrow), Write(arrow_label))
        self.wait(0.5)
        # Animate rotation (simulate quaternion rotation)
        self.play(Rotate(arrow, angle=PI/3, axis=[0, 0, 1], about_point=[0, 0, 0], run_time=5))
        self.wait(1.5)  # To reach 7s from start
        # Quaternion object
        quat = Text("Quaternion: [cos(π/6), 0, 0, sin(π/6)]", font_size=28).move_to([2, 1, 0]).scale(0.8)
        self.play(FadeIn(quat))
        self.wait(2)  # To reach 10s from start
        # Quaternion Magic text
        magic = Text("Quaternion Magic!", font_size=28).move_to([2, -1, 0]).scale(0.7)
        self.play(Write(magic))
        self.wait(5)  # To reach 15s from start
        # Rotated Vector (via Quaternion)
        rot_vec = Arrow3D(start=[0, 0, 0], end=[0.5, np.sqrt(3)/2, 0], color=BLUE)
        rot_label = Text("Rotated Vector (via Quaternion)", font_size=28).next_to(rot_vec.get_end(), UP)
        self.play(Transform(arrow, rot_vec), Write(rot_label))
        self.wait(5)  # To reach 20s from start
        # Compare Transformations
        compare = Text("Matrix Rotation vs Quaternion Rotation", font_size=28).move_to([0, -2, 0])
        self.play(Write(compare))
        self.wait(1)

# Scene 5: Why Quaternions Rule
class Scene5(ThreeDScene):
    def construct(self):
        # Set camera position to [5, 3, 7] looking at [0, 0, 0]
        self.move_camera(phi=59 * DEGREES, theta=59 * DEGREES, frame_center=[0, 0, 0], distance=8)
        title = Text("Why Quaternions Rule:", font_size=48).move_to([0, 1.5, 0]).scale(1.2)
        self.play(Write(title, run_time=2))
        bullets = BulletedList("No Gimbal Lock!", "More Compact", "Efficient Interpolation", font_size=36).move_to([0, 0, 0])
        self.play(FadeIn(bullets))
        self.wait(10)  # Wait until 10s for gimbal lock viz
        # Gimbal Lock Visualization (placeholder)
        gimbal = Text("[Gimbal Lock Visualization]", font_size=28).move_to([0, -1.5, 0])
        self.play(FadeIn(gimbal))
        self.wait(1)

# Scene 6: Call to Action
class Scene6(ThreeDScene):
    def construct(self):
        # Set camera position to [3, 2, 5] looking at [0, 0, 0]
        self.move_camera(phi=60 * DEGREES, theta=45 * DEGREES, frame_center=[0, 0, 0], distance=7)
        unlock = Text("Unlock the Power!", font_size=48).move_to([0, 1, 0]).scale(1.3)
        self.play(Write(unlock, run_time=2))
        cta = Text("Learn more in the description!", font_size=32, color=BLUE).move_to([0, -0.5, 0]).scale(0.8)
        self.play(Write(cta, run_time=1.5))
        icons = Text("YouTube   Twitter   Patreon", font_size=28).move_to([0, -1.5, 0]).scale(0.5)
        self.play(FadeIn(icons))
        self.wait(1)

# To render all scenes in sequence as a single video, run:
# manim -pql video.py FullVideo

class FullVideo(ThreeDScene):
    def construct(self):
        Scene1.construct(self)
        Scene2.construct(self)
        Scene3.construct(self)
        Scene4.construct(self)
        Scene5.construct(self)
        Scene6.construct(self)
