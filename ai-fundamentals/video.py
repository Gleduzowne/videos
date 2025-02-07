# video.py

class Scene:
    def __init__(self, name, duration, content):
        self.name = name
        self.duration = duration
        self.content = content

    def __repr__(self):
        return f"Scene(name='{self.name}', duration={self.duration}, content='{self.content}')"

def create_ai_fundamentals_video():
    """
    Defines the structure and content of the AI Fundamentals video.
    """

    scenes = [
        Scene(
            name="Introduction",
            duration=30,
            content="Welcome and overview of the video's topics."
        ),
        Scene(
            name="What is AI?",
            duration=60,
            content="Explanation of AI, its goals, and capabilities. Show examples of AI in everyday life."
        ),
        Scene(
            name="History of AI",
            duration=90,
            content="Brief history of AI, including key milestones and figures. Show historical photos and videos."
        ),
        Scene(
            name="Types of AI",
            duration=120,
            content="Explanation of Narrow AI, General AI, and Super AI with examples. Use animations to illustrate the differences."
        ),
        Scene(
            name="Core Concepts of AI",
            duration=180,
            content="Detailed explanation of Machine Learning, Deep Learning, Neural Networks, NLP, Computer Vision, and Robotics. Use diagrams and animations to explain each concept."
        ),
        Scene(
            name="Applications of AI",
            duration=120,
            content="Examples of AI applications in healthcare, finance, transportation, manufacturing, education, and entertainment. Show real-world examples and use cases."
        ),
        Scene(
            name="Ethical Considerations",
            duration=60,
            content="Discussion of ethical considerations such as bias, privacy, job displacement, and accountability. Show examples of AI bias and its impact."
        ),
        Scene(
            name="The Future of AI",
            duration=60,
            content="Overview of the future trends in AI, including Explainable AI, AI Ethics and Governance, and Human-AI Collaboration. Show potential future applications of AI."
        ),
        Scene(
            name="Conclusion",
            duration=30,
            content="Summary of the video's key points and a thank you to the viewers."
        )
    ]

    return scenes

if __name__ == "__main__":
    video_structure = create_ai_fundamentals_video()
    for scene in video_structure:
        print(scene)
