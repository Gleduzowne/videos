from manim import *
from tutorial import (
    IntroScene, TitleCard, AlgebraIntro, VectorRepresentation, MatrixRepresentation,
    ImageRepresentation, BuildingBlocks, AlgorithmIntro, SearchAlgorithm, SortingAlgorithm,
    MachineLearningAlgorithm, RecipeBook, FaceRecognition, LanguageTranslation,
    RecommendationSystem, AIApplications, OutroScene, EndScreen
)

class AITutorialVideo(Scene):
    def construct(self):
        self.play_scene(IntroScene)
        self.play_scene(TitleCard)
        self.play_scene(AlgebraIntro)
        self.play_scene(VectorRepresentation)
        self.play_scene(MatrixRepresentation)
        self.play_scene(ImageRepresentation)
        self.play_scene(BuildingBlocks)
        self.play_scene(AlgorithmIntro)
        self.play_scene(SearchAlgorithm)
        self.play_scene(SortingAlgorithm)
        self.play_scene(MachineLearningAlgorithm)
        self.play_scene(RecipeBook)
        self.play_scene(FaceRecognition)
        self.play_scene(LanguageTranslation)
        self.play_scene(RecommendationSystem)
        self.play_scene(AIApplications)
        self.play_scene(OutroScene)
        self.play_scene(EndScreen)

    def play_scene(self, scene_class):
        scene = scene_class()
        scene.construct()
        for animation in scene.animations:
            self.play(animation)
        self.wait(2) # Add a wait time between scenes
