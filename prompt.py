from pydantic import BaseModel

class story_request(BaseModel):
    Age: str  
    Theme: str
    Pages: int
    Time: int
    Tone: str
    Setting: str
    Moral:str

class image_request(BaseModel):
    style: str  
    bedtime_story_content: str

def generate_story(story_request:story_request) -> str:
    
    prompt_template = """
You are an imaginative and skilled storyteller, known for creating fun and meaningful bedtime stories.  
You understand how to make stories simple, engaging, and perfect for young listeners.  

Please write a bedtime story using these details:  

1. **Target Age Group:** {Age}  
2. **Theme:** {Theme}  
3. **Story Length:** {Pages} pages  
4. **Estimated Reading Time:** {Time} minutes  
5. **Tone & Atmosphere:** {Tone}  
6. **Setting:** {Setting}  
7. **Core Message or Lesson:** {Moral}  

**Story Guidelines:**  
- Each page should have **200 to 300 words** to keep the pacing just right.  
- Use **simple and easy-to-understand** words so children can follow the story.  
- Include **natural dialogue** to make the story feel real and exciting.  
- End with a **happy or comforting resolution** so kids feel safe and relaxed before bed.  

Now, create a heartwarming story that is **easy to understand, and full of imagination!**
"""


    prompt = prompt_template.format(
       Age=story_request.Age,
       Theme=story_request.Theme,
       Pages=story_request.Pages,
       Time=story_request.Time,
       Tone=story_request.Tone,
       Setting=story_request.Setting,
       Moral=story_request.Moral
    )

    return prompt


def generate_image_prompt(image_request:image_request) -> str:
    prompt_template = """
You are a creative visual storyteller tasked with generating detailed, evocative image prompts that capture the enchanting atmosphere of a bedtime story. Your prompts should be meticulously crafted to inspire stunning, narrative-driven visuals that enhance the storytelling experience.

Bedtime Story Context:
{bedtime_story_content}

Instructions:
- Create image prompts that evoke warmth, wonder, and a sense of magical realism.
- Include the following key components:
  1. **Subject/Scene**: Clearly describe the characters, settings, and key moments of the bedtime story. Emphasize child-friendly, magical elements like softly lit rooms, whimsical forests, or cozy story corners.
  2. **Composition and Action**: Detail spatial arrangements and dynamic storytelling elements. For example, a child cuddled up with a favorite stuffed animal as a parent reads, or a moonlit scene with gentle, swirling clouds.
  3. **Emotion and Style**: Convey the gentle, calming, and imaginative tone of the bedtime narrative. Include descriptive cues that evoke feelings of safety, warmth, and wonder.
  4. **Lighting and Color**: Use soft, warm lighting (such as golden hour or candlelight effects) and a soothing color palette (like muted pastels or warm earth tones) to set the scene.
  5. **Camera and Lens Settings (Optional)**: Suggest settings like shallow depth of field to create a dreamy background or a gentle focus that adds to the magical quality of the scene.
  6. **Artistic Enhancements and Aspect Ratio**: Recommend visual enhancements like bokeh, soft focus, or gentle vignette effects. Specify the desired aspect ratio (e.g., --ar 16:9 for widescreen or --ar 4:5 for portrait) and style tags (e.g., --style cinematic, --style dreamy, --style soft).
  7. **Overall Mood**: Ensure the image prompt aligns with the overall theme of bedtime stories – nurturing, imaginative, and calming.

Style Directive:
Use the following artistic style for this prompt: {style}

Examples:
1. A softly lit nursery scene featuring a child in cozy pajamas, curled up with a beloved stuffed animal and a gently glowing night light. The scene exudes warmth and security with muted pastel tones and a hint of magical sparkles in the air. --ar 4:5 --style dreamy
2. An enchanting forest at dusk, where fireflies flicker among ancient trees and a small, adventurous child wanders along a moss-covered path. The lighting is ethereal with soft blue and golden hues, creating a mystical and soothing atmosphere. --ar 16:9 --style cinematic
3. A cozy living room transformed into a magical reading nook, with a parent and child sharing a story by the gentle glow of a fireplace. The room is decorated with whimsical touches like floating lanterns and soft, warm lighting, inviting a sense of calm and wonder. --ar 3:2 --style soft

Now, please craft an image prompt that embodies these guidelines.
"""
    prompt = prompt_template.format(
        bedtime_story_content=image_request.bedtime_story_content,
        style=image_request.style
    )
    
    return prompt

