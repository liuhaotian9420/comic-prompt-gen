import streamlit as st

# --- Configuration ---
st.set_page_config(page_title="4-Panel Comic Prompt Generator", layout="wide")

# --- Reference Image URLs (Replace with your actual URLs or local paths) ---
# If using local paths: e.g., url_close_up = "assets/close_up.jpg"
REFERENCE_IMAGES = {
    "composition": {
        "Close-up": "https://via.placeholder.com/150/FF0000/FFFFFF?text=Close-Up", # Replace
        "Medium shot": "https://via.placeholder.com/150/00FF00/FFFFFF?text=Medium+Shot", # Replace
        "Long shot": "https://via.placeholder.com/150/0000FF/FFFFFF?text=Long+Shot", # Replace
        "POV (Point of View)": "https://via.placeholder.com/150/FFFF00/000000?text=POV", # Replace
        "Bird's-eye view": "https://via.placeholder.com/150/FF00FF/FFFFFF?text=Bird's-Eye", # Replace
    },
    "style": {
        "Clean Slice-of-Life Anime": "https://via.placeholder.com/150/AAAAAA/FFFFFF?text=SliceOfLife", # Replace
        "Chibi / Cute": "https://via.placeholder.com/150/FFAAAA/000000?text=Chibi", # Replace
        "Gag Manga": "https://via.placeholder.com/150/AAFFAA/000000?text=Gag+Manga", # Replace
        "Simple Cartoon": "https://via.placeholder.com/150/AAAAFF/000000?text=Cartoon", # Replace
    },
    "coloring": {
        "Flat Colors": "https://via.placeholder.com/150/CCCCCC/000000?text=Flat+Color", # Replace
        "Cell Shading": "https://via.placeholder.com/150/E6E6E6/000000?text=Cell+Shading", # Replace
        "Watercolor": "https://via.placeholder.com/150/D0D0FF/000000?text=Watercolor", # Replace
        "Black and White": "https://via.placeholder.com/150/FFFFFF/000000?text=B%26W", # Replace
    }
}

# --- Helper Function to Display Reference Images ---
def show_reference_image(category, key):
    if key in REFERENCE_IMAGES.get(category, {}):
        st.image(REFERENCE_IMAGES[category][key], caption=key, width=150)
    else:
        st.caption(f"(No image preview for {key})")

# --- Streamlit App UI ---
st.title("📝 4-Panel Comic Prompt Generator")
st.markdown("Fill in the details below to generate a detailed prompt for an AI image generator.")

# Use columns for better layout
col1, col2 = st.columns([2, 1]) # Main input area and reference sidebar

with col1:
    st.header("Overall Story & Scene")

    with st.expander("1. Overall Storyboard & Narrative Flow", expanded=True):
        core_concept = st.text_input("Core Concept/Theme", "A cat tries to get its owner's attention while they work.")
        narrative_arc = st.text_area("Narrative Arc (Optional)", "1. Setup: Owner works, cat watches.\n2. Rising Action: Gentle nudge.\n3. Climax/Escalation: Walks on keyboard.\n4. Resolution: Owner gives in.", height=100)
        reader_feeling = st.text_input("Target Reader Feeling (Optional)", "Amused, relatable, heartwarming")

    with st.expander("2. Overall Scene Description & Layout", expanded=True):
        overall_scene = st.text_input("Overall Scene/Environment", "Simple home office corner with desk, laptop, chair.")
        # Title generation is tricky for AI, make it optional/clear
        comic_title_placeholder = st.text_input("Attempt Comic Title (AI might ignore/fail)", "Work 'Assistant'")
        comic_title = f'图片最上方尝试清晰展示文字：“{comic_title_placeholder}”。（AI可能无法准确生成文字）' if comic_title_placeholder else ""
        content_summary_char = st.text_input("Character(s)", "An orange tabby cat 'Mimi'")
        content_summary_action = st.text_input("Core Action/Content", "progressively distracting its owner who is using a laptop")
        content_summary = f"四个画格展示了{content_summary_char}正在经历{content_summary_action}。"


    with st.expander("3. Reference Images (Optional)", expanded=False):
        st.markdown("Provide URLs or descriptions for visual guidance (AI might not access URLs directly).")
        ref_overall_style = st.text_input("Overall Style Reference", "e.g., 'Chi's Sweet Home' manga style")
        ref_character = st.text_input("Character Design Reference", "Slightly chubby orange tabby cat, big expressive eyes.")
        ref_environment = st.text_input("Environment/Item Reference", "Modern clean desk setup, laptop, mouse.")
        ref_pose = st.text_input("Pose/Composition Reference", "Common cat poses (loafing, stretching, walking on things)")
        ref_other = st.text_input("Other References", "")

    st.header("Individual Panel Details")

    panels = {}
    default_panels = {
        1: {"purpose": "Setup: Introduce character/situation", "desc": "Owner typing at laptop. Orange cat 'Mimi' sits nearby, watching intently.", "comp": "Medium shot", "text": "", "placement": "No text", "sfx": "tap tap tap (keyboard)", "ref": ""},
        2: {"purpose": "Rising Action: Initial attempt", "desc": "Mimi gently paws at owner's arm. Owner glances slightly annoyed.", "comp": "Close-up", "text": "Hmm?", "placement": "Thought bubble (Owner)", "sfx": "pat pat", "ref": "Cat pleading expression"},
        3: {"purpose": "Turning Point/Escalation: Bold move", "desc": "Mimi walks directly onto the laptop keyboard. Owner stops typing, surprised. Gibberish on screen.", "comp": "Medium shot", "text": "Hey!", "placement": "Speech bubble (Owner)", "sfx": "thump!", "ref": ""},
        4: {"purpose": "Resolution/Reaction: Outcome", "desc": "Owner sighs, hand on face, other hand petting Mimi who is now loafing on keyboard, purring.", "comp": "Medium close-up", "text": "Okay, five-minute break...", "placement": "Thought bubble (Owner)", "sfx": "purrrr~", "ref": "Cat looking smug/satisfied"},
    }

    panel_cols = st.columns(2) # Display panels in two columns

    for i in range(1, 5):
        col_index = (i - 1) % 2
        with panel_cols[col_index]:
            st.subheader(f"Panel {i}: {'Top-Left' if i==1 else 'Top-Right' if i==2 else 'Bottom-Left' if i==3 else 'Bottom-Right'}")
            with st.expander(f"Edit Panel {i} Details", expanded=(i==1)): # Expand first panel by default
                defaults = default_panels[i]
                panels[i] = {}
                panels[i]['purpose'] = st.text_input(f"[{i}] Narrative Purpose", defaults['purpose'], key=f"p{i}_purpose")
                panels[i]['desc'] = st.text_area(f"[{i}] Visual Description", defaults['desc'], key=f"p{i}_desc", height=100)

                # Composition with Reference Image
                st.write(f"[{i}] Composition/Angle")
                comp_options = list(REFERENCE_IMAGES["composition"].keys()) + ["Other"]
                selected_comp = st.selectbox(f"Select Composition", comp_options, index=comp_options.index(defaults['comp']) if defaults['comp'] in comp_options else len(comp_options)-1, key=f"p{i}_comp_select")
                if selected_comp != "Other":
                    panels[i]['comp'] = selected_comp
                    show_reference_image("composition", selected_comp)
                else:
                     panels[i]['comp'] = st.text_input("Specify Other Composition", key=f"p{i}_comp_other")

                panels[i]['text'] = st.text_input(f"[{i}] Text Content", defaults['text'], key=f"p{i}_text")
                panels[i]['placement'] = st.selectbox(f"[{i}] Text Placement", ["No text", "Caption below", "Speech bubble", "Thought bubble", "Signage/On-screen", "Sound effect text"], index=["No text", "Caption below", "Speech bubble", "Thought bubble", "Signage/On-screen", "Sound effect text"].index(defaults['placement']) if defaults['placement'] in ["No text", "Caption below", "Speech bubble", "Thought bubble", "Signage/On-screen", "Sound effect text"] else 0, key=f"p{i}_placement")
                panels[i]['sfx'] = st.text_input(f"[{i}] Sound Effects (Optional)", defaults['sfx'], key=f"p{i}_sfx")
                panels[i]['ref'] = st.text_input(f"[{i}] Specific Reference (Optional)", defaults['ref'], key=f"p{i}_ref")
                panels[i]['transition'] = st.text_input(f"[{i}] Transition from Prev. (Optional)", "", key=f"p{i}_transition", help="How does this panel connect to the previous one?")


    st.header("Comic Style Profile")
    with st.expander("4. Edit Comic Style Profile", expanded=True):
        style_cols = st.columns(2)
        with style_cols[0]:
            st.subheader("Overall Style")
            style_options = list(REFERENCE_IMAGES["style"].keys()) + ["Other"]
            selected_style = st.selectbox("Base Style Name", style_options, index=0, key="style_name_select")
            if selected_style != "Other":
                style_name = selected_style
                show_reference_image("style", selected_style)
            else:
                style_name = st.text_input("Specify Other Style", "custom style name", key="style_name_other")

            st.subheader("Character Design")
            char_style = st.text_input("Character Style Description", "Cute, slightly chibi anthropomorphic cat, simple human elements", key="char_style")
            char_recurring = st.text_input("Recurring Character Note", "**关键：保持'咪咪'的橘猫虎斑设计和主人简洁风格一致**", key="char_recurring", help="Important if part of a series")
            char_expressions = st.text_area("Key Expressions / Emotions", "Cat: Expectant -> Pleading -> Innocent/Bold -> Satisfied/Smug. Human: Focused -> Annoyed -> Surprised -> Resigned", key="char_expressions", height=75)

            st.subheader("Line Art")
            line_weight = st.selectbox("Line Weight", ["clean, consistent medium line weight.", "fine line weight", "bold line weight", "varied line weight", "sketchy"], key="line_weight")
            line_style = st.selectbox("Line Style", ["digital ink look.", "pencil sketch look", "brush stroke look", "pixelated look"], key="line_style")
            line_color = st.text_input("Line Color", "dark brown", key="line_color")

        with style_cols[1]:
            st.subheader("Color Theme")
            color_palette_options = list(REFERENCE_IMAGES["coloring"].keys()) + ["Other"]
            selected_palette = st.selectbox("Palette Style", color_palette_options, index=0, key="palette_select")
            if selected_palette != "Other":
                 palette_style = selected_palette
                 show_reference_image("coloring", selected_palette)
            else:
                 palette_style = st.text_input("Specify Other Palette Style", "custom palette", key="palette_other")

            background = st.text_input("Background Description", "light cream or pale blue simple background per panel", key="background")
            overall_tone = st.selectbox("Overall Tone", ["warm and light pastel palette", "cool palette", "vintage palette", "high-contrast", "monochrome", "neon"], key="overall_tone")

            st.subheader("Panel Layout")
            grid_style = st.text_input("Grid Style", "standard 2x2", key="grid_style", disabled=True) # Keep simple for now
            gutter_color = st.color_picker("Gutter Color", "#FFFFFF", key="gutter_color")
            gutter_width = st.selectbox("Gutter Width", ["thin", "medium", "thick", "none"], index=1, key="gutter_width")
            border_style = st.selectbox("Border Style", ["solid thin line", "solid medium line", "solid thick line", "rounded corners", "no border"], index=0, key="border_style")
            border_color = st.color_picker("Border Color", "#4B3A26", key="border_color") # Dark brown default matching lines

            st.subheader("Text Rendering (Hints)")
            font_hint = st.text_input("Font Style Hint", "clean, rounded sans-serif comic font", key="font_hint")
            bubble_style = st.text_input("Bubble Style Hint", "standard oval (speech), cloud (thought)", key="bubble_style")


# --- Generate Prompt Output ---
st.header("Generated Prompt")

prompt = f"""
## 核心指令：生成一张包含2x2网格布局的四格漫画，主题：[{core_concept}]

**【整体故事板与叙事流】(Overall Storyboard & Narrative Flow):**
- **核心概念/主题：** {core_concept}
- **叙事弧线 (可选):** {narrative_arc}
- **目标读者感受 (可选):** {reader_feeling}

**【整体画面描述与布局要求】(Overall Scene Description & Layout Requirements):**
- **最终图像：** 生成一张单一图片，内部包含一个清晰的2x2网格，分隔出四个独立的漫画画格。
- **整体场景/环境：** {overall_scene}
- **主题/标题（尝试性）：** {comic_title}
- **内容梗概：** {content_summary} 风格遵循下方的【漫画风格配置文件】。

**【参考图像 (可选)】(Reference Images - Optional):**
- **整体风格参考:** {ref_overall_style}
- **角色设计参考:** {ref_character}
- **环境/物品参考:** {ref_environment}
- **姿势/构图参考:** {ref_pose}
- **其他参考:** {ref_other}
*注：AI可能无法直接访问URL，请同时提供关键描述。参考图主要用于启发和指导风格/元素，而非直接复制。*

**【各画格内容描述】(Individual Panel Content Descriptions):**
"""

# Add Panel Details
for i in range(1, 5):
    panel = panels[i]
    panel_loc = {'1': '左上格 (Panel 1: Top-Left)', '2': '右上格 (Panel 2: Top-Right)', '3': '左下格 (Panel 3: Bottom-Left)', '4': '右下格 (Panel 4: Bottom-Right)'}
    prompt += f"""
{i}.  **{panel_loc[str(i)]}:**
    *   **叙事作用 (Panel Purpose):** {panel['purpose']}
    *   **画面描述 (Visual Description):** {panel['desc']}
    *   **构图/视角 (Composition/Angle):** {panel['comp']}
    *   **文字内容 (Text Content):** "{panel['text']}"
    *   **文字位置 (Text Placement):** {panel['placement']}
    *   **音效 (Sound Effects - 可选):** {panel['sfx']}
    *   **具体参考 (Specific Reference - 可选):** {panel['ref']}
    *   **与前格联系 (Transition from Prev. - 可选):** {panel['transition']}
"""

# Add Style Profile
prompt += f"""
---

**【漫画风格配置文件】(Comic Style Profile):**
{{
  "style_name": "{style_name}",
  "visual_elements": {{
    "character_design": {{
      "style": "{char_style}",
      "recurring_character": "{char_recurring}",
      "expressions": "{char_expressions}"
    }},
    "line_art": {{
      "weight": "{line_weight}",
      "style": "{line_style}",
      "color": "{line_color}"
    }},
    "color_theme": {{
      "palette_style": "{palette_style}",
      "background": "{background}",
      "overall_tone": "{overall_tone}"
    }},
    "panel_layout": {{
       "grid_style": "{grid_style}",
       "gutter_color": "{gutter_color}",
       "gutter_width": "{gutter_width}",
       "border_style": "{border_style} using color {border_color}" // Adjusted border description
    }},
    "text_rendering": {{
       "font_style_hint": "{font_hint}",
       "bubble_style": "{bubble_style}"
    }}
  }}
}}
"""

# Display the prompt in a code block (which usually has a copy button)
st.code(prompt, language='markdown')

# Optional: Add explicit copy button using a third-party component if needed
# (Requires installation: pip install streamlit-clipboard)
# try:
#     from streamlit_clipboard import st_clipboard
#     st_clipboard(prompt)
# except ImportError:
#     st.warning("Install 'streamlit-clipboard' for a dedicated copy button: pip install streamlit-clipboard")

# --- Sidebar for Reference Image Previews (Less intrusive) ---
with col2:
    st.header("Reference Previews")
    st.markdown("Quick examples of some terms:")

    with st.expander("Composition Angles", expanded=False):
        for key in REFERENCE_IMAGES["composition"]:
            show_reference_image("composition", key)

    with st.expander("Example Styles", expanded=False):
        for key in REFERENCE_IMAGES["style"]:
            show_reference_image("style", key)

    with st.expander("Example Coloring", expanded=False):
         for key in REFERENCE_IMAGES["coloring"]:
            show_reference_image("coloring", key)