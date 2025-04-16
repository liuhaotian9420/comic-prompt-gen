"""Prompt generator for 4-panel comics."""
from typing import Dict, Optional

from .models import ComicPrompt, Panel, StyleProfile


def generate_prompt(comic_prompt: ComicPrompt) -> str:
    """Generate a complete prompt from a ComicPrompt object.
    
    Args:
        comic_prompt: The ComicPrompt object containing all comic details
        
    Returns:
        The formatted prompt text ready for AI image generators
    """
    # Format the content summary
    content_summary = f"四个画格展示了{comic_prompt.content_summary_char}正在经历{comic_prompt.content_summary_action}。"
    
    # Format comic title if present
    comic_title = ""
    if comic_prompt.comic_title:
        comic_title = f'图片最上方尝试清晰展示文字："{comic_prompt.comic_title}"。（AI可能无法准确生成文字）'
    
    # Start building the prompt
    prompt = f"""
## 核心指令：生成一张包含2x2网格布局的四格漫画，主题：[{comic_prompt.core_concept}]

**【整体故事板与叙事流】(Overall Storyboard & Narrative Flow):**
- **核心概念/主题：** {comic_prompt.core_concept}
- **叙事弧线 (可选):** {comic_prompt.narrative_arc}
- **目标读者感受 (可选):** {comic_prompt.reader_feeling}

**【整体画面描述与布局要求】(Overall Scene Description & Layout Requirements):**
- **最终图像：** 生成一张单一图片，内部包含一个清晰的2x2网格，分隔出四个独立的漫画画格。
- **整体场景/环境：** {comic_prompt.overall_scene}
- **主题/标题（尝试性）：** {comic_title}
- **内容梗概：** {content_summary} 风格遵循下方的【漫画风格配置文件】。

**【参考图像 (可选)】(Reference Images - Optional):**
- **整体风格参考:** {comic_prompt.ref_overall_style}
- **角色设计参考:** {comic_prompt.ref_character}
- **环境/物品参考:** {comic_prompt.ref_environment}
- **姿势/构图参考:** {comic_prompt.ref_pose}
- **其他参考:** {comic_prompt.ref_other}
*注：AI可能无法直接访问URL，请同时提供关键描述。参考图主要用于启发和指导风格/元素，而非直接复制。*

**【各画格内容描述】(Individual Panel Content Descriptions):**
"""

    # Add Panel Details
    panel_locations = {
        '1': '左上格 (Panel 1: Top-Left)', 
        '2': '右上格 (Panel 2: Top-Right)', 
        '3': '左下格 (Panel 3: Bottom-Left)', 
        '4': '右下格 (Panel 4: Bottom-Right)'
    }
    
    for i in range(1, 5):
        panel = comic_prompt.panels[str(i)]
        prompt += f"""
{i}.  **{panel_locations[str(i)]}:**
    *   **叙事作用 (Panel Purpose):** {panel.purpose}
    *   **画面描述 (Visual Description):** {panel.desc}
    *   **构图/视角 (Composition/Angle):** {panel.comp}
    *   **文字内容 (Text Content):** "{panel.text}"
    *   **文字位置 (Text Placement):** {panel.placement}
    *   **音效 (Sound Effects - 可选):** {panel.sfx}
    *   **具体参考 (Specific Reference - 可选):** {panel.ref}
    *   **与前格联系 (Transition from Prev. - 可选):** {panel.transition}
"""

    # Add Style Profile
    style = comic_prompt.style
    prompt += f"""
---

**【漫画风格配置文件】(Comic Style Profile):**
{{
  "style_name": "{style.style_name}",
  "visual_elements": {{
    "character_design": {{
      "style": "{style.char_style}",
      "recurring_character": "{style.char_recurring}",
      "expressions": "{style.char_expressions}"
    }},
    "line_art": {{
      "weight": "{style.line_weight}",
      "style": "{style.line_style}",
      "color": "{style.line_color}"
    }},
    "color_theme": {{
      "palette_style": "{style.palette_style}",
      "background": "{style.background}",
      "overall_tone": "{style.overall_tone}"
    }},
    "panel_layout": {{
       "grid_style": "{style.grid_style}",
       "gutter_color": "{style.gutter_color}",
       "gutter_width": "{style.gutter_width}",
       "border_style": "{style.border_style} using color {style.border_color}" // Adjusted border description
    }},
    "text_rendering": {{
       "font_style_hint": "{style.font_hint}",
       "bubble_style": "{style.bubble_style}"
    }}
  }}
}}
"""
    
    return prompt 