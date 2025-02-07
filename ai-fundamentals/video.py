# video.py
import re

class Scene:
    def __init__(self, name, duration, content):
        self.name = name
        self.duration = duration
        self.content = content

    def __repr__(self):
        return f"Scene(name='{self.name}', duration={self.duration}, content='{self.content}')"

def create_ai_fundamentals_video():
    """
    Creates scenes manually, based on the final voiceover text (interpreted outside of code).
    Durations are approximate and can be adjusted as needed.
    """
    scenes = [
        Scene(
            name="Scene 1",
            duration=16,
            content="""Behold, the algorithmic universe. Within the abstract language of mathematics, a profound transformation is underway. We are witnessing the dawn of Artificial Intelligence."""
        ),
        Scene(
            name="Scene 2",
            duration=15,
            content="""Forget flesh and blood. Forget faces. Here, intelligence emerges from pure form, from the elegant dance of equations and the relentless logic of computation. We will explore the very foundations of AI, visualized through the language of shapes, symbols, and dynamic abstraction."""
        ),
        Scene(
            name="Scene 3",
            duration=24,
            content="""What is Artificial Intelligence, stripped to its essence? It is the construction of machines capable of mimicking cognitive functions. Not through imitation of biology, but through the rigorous application of algorithms. We seek to encode learning, reasoning, problem-solving, perception, and linguistic understanding within computational structures."""
        ),
        Scene(
            name="Scene 4",
            duration=12,
            content="""This is not about replicating humanity. It is about augmenting intellect. Building tools that amplify our cognitive reach, solve problems of immense scale, and unveil patterns hidden within the noise of data."""
        ),
        Scene(
            name="Scene 5",
            duration=10,
            content="""AI is not monolithic. It exists on a spectrum of capability. Let us dissect its fundamental forms."""
        ),
        Scene(
            name="Scene 6",
            duration=20,
            content="""First, we encounter Narrow AI, or Weak AI. This is the workhorse of the present. Think of algorithmic trading in financial markets, recommendation engines predicting your preferences, spam filters dissecting email content."""
        ),
        Scene(
            name="Scene 7",
            duration=19,
            content="""Narrow AI excels at specialized tasks. It can surpass human performance in domains defined by clear rules and vast datasets. Chess algorithms, facial recognition systems, language translation engines – all are testaments to its power. Yet, its intelligence is bounded. It operates within predefined parameters, lacking general cognitive capacity."""
        ),
        Scene(
            name="Scene 8",
            duration=18,
            content="""Then, there is the aspiration of General AI, or Strong AI. This is the theoretical horizon. General AI would possess human-level cognitive versatility. The capacity to learn and apply knowledge across diverse domains, to reason abstractly, to exhibit creativity, to possess common sense."""
        ),
        Scene(
            name="Scene 9",
            duration=14,
            content="""General AI remains a research objective. Its realization would signify a profound shift. Imagine an algorithm not merely processing language, but comprehending nuance, context, and intent. An intelligence capable of genuine innovation."""
        ),
        Scene(
            name="Scene 10",
            duration=23,
            content="""Beyond General AI lies the speculative realm of Super AI. This is the conceptual limit. Super AI would transcend human intellect in all dimensions. Creativity, problem-solving, strategic thinking, wisdom – all amplified beyond human comprehension. Super AI is a theoretical construct, a point of contemplation, both awe-inspiring and cautionary."""
        ),
        Scene(
            name="Scene 11",
            duration=24,
            content="""Now, let us delve into the algorithmic core. How is this artificial intelligence constructed? We begin with the bedrock principle: Machine Learning."""
        ),
        Scene(
            name="Scene 12",
            duration=20,
            content="""Machine learning is the paradigm shift. Instead of explicit programming, we employ data-driven learning. Algorithms are designed to extract knowledge and patterns directly from data, to refine their performance through experience."""
        ),
        Scene(
            name="Scene 13",
            duration=14,
            content="""Consider the task of object recognition. We do not hardcode rules for identifying objects. Instead, we expose algorithms to vast datasets of labeled examples – images, text, numerical arrays. From this deluge of data, algorithms discern underlying structures, make predictions, and iteratively improve their accuracy."""
        ),
        Scene(
            name="Scene 14",
            duration=18,
            content="""Machine learning encompasses diverse methodologies. Supervised learning operates with labeled data. Algorithms learn to map inputs to known outputs, guided by explicit examples. Unsupervised learning explores unlabeled data, seeking hidden structures and inherent groupings. Reinforcement learning employs a reward-penalty mechanism. Algorithms learn through interaction with an environment, optimizing actions to maximize cumulative reward."""
        ),
        Scene(
            name="Scene 15",
            duration=16,
            content="""Within machine learning, Deep Learning stands as a transformative force. It leverages Artificial Neural Networks, computational structures inspired by the biological brain."""
        ),
        Scene(
            name="Scene 16",
            duration=20,
            content="""These networks comprise interconnected layers of artificial neurons. Data propagates through these layers, undergoing transformations at each stage. The network learns to extract hierarchical features, progressively capturing increasingly abstract and complex representations of the input data. Deep learning has revolutionized image recognition, natural language processing, and speech synthesis, achieving unprecedented performance in previously intractable tasks."""
        ),
        Scene(
            name="Scene 17",
            duration=18,
            content="""The realm of language processing is captured by Natural Language Processing, or NLP. This domain empowers machines to parse, interpret, and generate human language."""
        ),
        Scene(
            name="Scene 18",
            duration=16,
            content="""NLP fuels conversational agents, automated translation systems, sentiment analysis tools, and voice interfaces. It bridges the chasm between human linguistic expression and algorithmic comprehension, enabling seamless interaction between humans and machines."""
        ),
        Scene(
            name="Scene 19",
            duration=18,
            content="""And finally, Computer Vision bestows upon machines the power of sight. It enables algorithms to interpret and analyze the visual world."""
        ),
        Scene(
            name="Scene 20",
            duration=20,
            content="""Computer vision algorithms dissect images and videos, identifying objects, patterns, and relationships. From autonomous navigation systems to medical image analysis and biometric authentication, computer vision grants machines the capacity to perceive and interpret the visual domain."""
        ),
        Scene(
            name="Scene 21",
            duration=12,
            content="""The construction of AI relies on a synergistic triad: Data, Algorithms, and Computational Power."""
        ),
        Scene(
            name="Scene 22",
            duration=18,
            content="""Data is the fuel. Vast quantities of data are essential for effective learning. Algorithms are the blueprints, the logical structures that define the learning process. And Computational Power is the engine, the processing capacity necessary to execute complex algorithms on massive datasets. Advances in computational hardware, particularly parallel processing architectures, have been pivotal in the recent surge of AI capabilities."""
        ),
        Scene(
            name="Scene 23",
            duration=14,
            content="""As AI permeates our world, we must confront the ethical dimensions."""
        ),
        Scene(
            name="Scene 24",
            duration=18,
            content="""Algorithmic bias, job displacement, autonomous weapon systems, surveillance technologies, fairness, transparency – these are not mere technical challenges. They are profound ethical imperatives. The trajectory of AI development must be guided by principles of responsibility, equity, and human well-being."""
        ),
        Scene(
            name="Scene 25",
            duration=16,
            content="""Yet, amidst these considerations, the future of AI is incandescently bright. We stand at the cusp of a new era of intellectual augmentation."""
        ),
        Scene(
            name="Scene 26",
            duration=24,
            content="""Imagine personalized medicine tailored to individual genetic profiles, intelligent infrastructure optimizing resource allocation, AI-driven scientific discovery accelerating the pace of knowledge creation, and creative algorithms pushing the boundaries of artistic expression. The algorithmic potential is boundless."""
        ),
        Scene(
            name="Scene 27",
            duration=18,
            content="""This has been a journey into the theoretical heart of Artificial Intelligence. From the abstract definition to the algorithmic foundations and ethical considerations, we have explored the essence of this transformative technology through the language of shapes and mathematics."""
        ),
        Scene(
            name="Scene 28",
            duration=16,
            content="""The algorithmic awakening is not a distant prospect – it is our present reality. Understanding its fundamentals is the first step towards harnessing its profound potential and shaping a future where human intellect and artificial intelligence converge to solve the grand challenges and illuminate the path forward."""
        ),
        Scene(
            name="Scene 29",
            duration=10,
            content="""To delve deeper into the algorithmic universe, explore further resources, and join the conversation, visit the links in the description. The algorithmic future awaits."""
        ),
    ]
    return scenes

if __name__ == "__main__":
    video_structure = create_ai_fundamentals_video()
    for scene in video_structure:
        print(scene)
