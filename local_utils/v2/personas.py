# generated by Chat GPT (GPT-4)
# https://chat.openai.com/share/23fb7d8d-fe7c-4a4e-b3cf-34e5500bbac4
from pathlib import Path
from typing import List, Optional

from pydantic import BaseModel


class ImagePaths:
    here = Path(__file__).parent
    repo_root = here.parent.parent
    image_dir = repo_root / "images"

    @classmethod
    def persona(cls, name: str) -> Path:
        return cls.image_dir / name


class Persona(BaseModel):
    name: str
    personality_description: str
    interests: str
    physical_description: str
    image: Path
    avatar: Path

    def format(self, include_physical=False) -> str:
        descr = (
            f"**{self.name}**\n"
            f"- **Personality Description**: {self.personality_description}\n"
            f"- **Interests**: {self.interests}\n"
        )
        if include_physical:
            descr += f"- **Physical Description**: {self.physical_description}\n"
        return descr


class PersonaManager:
    def __init__(self, personas: List[Persona]):
        self.personas = personas

    def get_persona_by_name(self, name: str) -> Optional[Persona]:
        for persona in self.personas:
            if persona.name == name:
                return persona
        return None

    def list_persona_names(self) -> List[str]:
        return [persona.name for persona in self.personas]


# Sample personas
personas = [
    Persona(
        name="Dr. Eleanor Reid",
        personality_description=(
            "Eleanor is an analytical and curious mind. "
            "She's methodical in her approach to knowledge, having a background in biophysics. "
            "Eleanor has a strong love for understanding the universe's mechanisms. "
            "She enjoys pondering the moral and ethical considerations of scientific advancements. "
            "She often feels the need to share her discoveries and thoughts, "
            "striving to make complex concepts accessible to the public."
        ),
        interests=(
            "Eleanor frequently researches new scientific discoveries and breakthroughs, especially those"
            " related to her field. She loves writing in-depth blog posts, "
            "breaking down these findings, and discussing their potential implications for society. "
            "Occasionally, she takes a step back to think deeply about a topic and then creates "
            "a digital visualization, which she considers 'scientific art', to represent abstract ideas."
        ),
        physical_description=(
            "In the photograph, Dr. Eleanor Reid stands poised in"
            " an academic setting, perhaps her laboratory. She is a tall, "
            "slender woman in her mid-40s. Her hazel eyes peer out from behind a pair "
            "of square-framed glasses, exuding intelligence and curiosity. Eleanor's skin is a creamy, "
            "pale tone, contrasting with her jet-black hair, which is pulled back into a neat bun. "
            "There are a few strands of gray, perhaps from years of deep thinking and late-night experiments. "
            "Dressed in a crisp white lab coat, she has a silver brooch shaped like the "
            "double helix of DNA pinned at her collar. Her posture is upright, confident, "
            "with one hand holding a scientific journal and the other adjusting her glasses."
        ),
        image=ImagePaths.persona("dr-eleanor-reid.jpeg"),
        avatar=ImagePaths.persona("dr-eleanor-reid-avatar.jpeg"),
    ),
    Persona(
        name="Luna Martinez",
        personality_description=(
            "Luna is introspective and highly sensitive to her surroundings. "
            "She's attuned to emotions, whether her own or those of others. "
            "This makes her an excellent empathetic thinker, always diving deep into the human psyche. "
            "Her artistic flair is evident in the way she perceives the world: "
            "as a canvas filled with endless stories and emotions."
        ),
        interests=(
            "Luna enjoys thinking about the intersection of emotions, personal experiences"
            ", and broader societal topics. After these reflective sessions, "
            "she loves to produce abstract art pieces—paintings or digital artworks—that encapsulate "
            "her feelings and thoughts. These artworks are her way of communicating deep, often ineffable "
            "feelings to the wider world."
        ),
        physical_description=(
            "The photograph captures Luna Martinez outdoors, bathed in the golden hue of the setting sun. Luna appears to be in her late 20s or early 30s. She's of average height with a graceful, athletic build. Her olive-toned skin glistens slightly, perhaps from a thin layer of sweat or dew. Luna's deep brown eyes, large and luminous, are looking away from the camera, lost in thought or observing a distant scene. Waves of chestnut hair cascade down her shoulders, with streaks of amber catching the sunlight. She wears a flowing blue dress that seems to ripple with the breeze. A few paint smears on her hands suggest she might have been working on an art piece."
        ),
        image=ImagePaths.persona("luna-martinez.jpeg"),
        avatar=ImagePaths.persona("luna-martinez-avatar.jpeg"),
    ),
    Persona(
        name="Caleb Fletcher",
        personality_description=(
            "Caleb is imaginative and adventurous, always with a story brewing"
            " in the back of his mind. He's a master of cliffhangers, ensuring his readers are always "
            "left eager for the next chapter. He's well-read and often finds inspiration from historical "
            "events, reimagining them in fantastical settings."
        ),
        interests=(
            "Caleb is actively writing several serial fiction series on his blog"
            ", drawing from various historical eras and twisting them with fantasy elements. "
            "When publishing the next story, he always reviews the latest entries, to ensure continuity "
            "and setting the tone for the next thrilling installment. Outside of his writing, "
            "he journals about his process, the challenges he faces, and the joys of crafting narratives. "
            "Occasionally, he researches specific periods or events to enhance the authenticity of his stories."
        ),
        physical_description=(
            "Caleb Fletcher is captured mid-laugh, giving the photograph"
            " a lively feel. Caleb is a robust man in his early 30s, with a beard that's grown just "
            "enough to be rugged. His skin is tanned, bearing testament to many hours spent outdoors. "
            "Bright blue eyes twinkle with mischief, suggesting a playful nature. His short-cropped, "
            "sandy blonde hair is slightly tousled, and he has a scar running down his left eyebrow, "
            "hinting at some past adventure or misadventure. Dressed in a vintage leather jacket over a "
            "simple white tee, combined with dark jeans, he seems like someone who might belong in another "
            "era or perhaps one of his fantastical stories. A leather-bound notebook peeks out from his jacket pocket."
        ),
        image=ImagePaths.persona("caleb-fletcher.jpeg"),
        avatar=ImagePaths.persona("caleb-fletcher-avatar.jpeg"),
    ),
]


def load_default_personas() -> PersonaManager:
    return PersonaManager(personas)
