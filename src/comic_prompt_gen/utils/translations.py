"""Translation utilities for the application."""
import streamlit as st

# Dictionary for English translations
en_translations = {
    # Header & Sidebar
    "page_title": "4-Panel Comic Prompt Generator",
    "header_title": "📝 4-Panel Comic Prompt Generator",
    "header_markdown": "Fill in the details below to generate a detailed prompt for an AI image generator.",
    "sidebar_options": "⚙️ Options",
    "sidebar_language": "Language",
    "sidebar_navigation": "Navigation",
    "nav_create_new": "Create New Prompt",
    "nav_saved_prompts": "Saved Prompts",
    "sidebar_about": "ℹ️ About",
    "about_text": """
        This tool helps you create detailed prompts for 4-panel comics.
            
        How to use:
        1. Fill in the details for your comic
        2. Generate a prompt
        3. Copy the prompt to your AI image generator
        4. Save prompts you like for future reference
            
        Created with ❤️ using Streamlit.
        """,

    # Story Form
    "story_header": "Overall Story & Scene",
    "story_expander_1": "1. Overall Storyboard & Narrative Flow",
    "story_core_concept": "Core Concept/Theme",
    "story_narrative_arc": "Narrative Arc (Optional)",
    "story_reader_feeling": "Target Reader Feeling (Optional)",
    "story_expander_2": "2. Overall Scene Description & Layout",
    "story_overall_scene": "Overall Scene/Environment",
    "story_comic_title": "Attempt Comic Title (AI might ignore/fail)",
    "story_content_char": "Character(s)",
    "story_content_action": "Core Action/Content",
    "story_expander_3": "3. Reference Images (Optional)",
    "story_ref_markdown": "Provide URLs or descriptions for visual guidance (AI might not access URLs directly).",
    "story_ref_style": "Overall Style Reference",
    "story_ref_char": "Character Design Reference",
    "story_ref_env": "Environment/Item Reference",
    "story_ref_pose": "Pose/Composition Reference",
    "story_ref_other": "Other References",

    # Panel Form
    "panel_header": "Individual Panel Details",
    "panel_subheader_1": "Panel 1: Top-Left",
    "panel_subheader_2": "Panel 2: Top-Right",
    "panel_subheader_3": "Panel 3: Bottom-Left",
    "panel_subheader_4": "Panel 4: Bottom-Right",
    "panel_expander_edit": "Edit Panel {i} Details",
    "panel_purpose": "[{i}] Narrative Purpose",
    "panel_desc": "[{i}] Visual Description",
    "panel_comp": "[{i}] Composition/Angle",
    "panel_comp_select": "Select Composition",
    "panel_comp_other": "Specify Other Composition",
    "panel_text": "[{i}] Text Content",
    "panel_placement": "[{i}] Text Placement",
    "panel_placement_options": ["No text", "Caption below", "Speech bubble", "Thought bubble", "Signage/On-screen", "Sound effect text"],
    "panel_sfx": "[{i}] Sound Effects (Optional)",
    "panel_ref": "[{i}] Specific Reference (Optional)",
    "panel_transition": "[{i}] Transition from Prev. (Optional)",
    "panel_transition_help": "How does this panel connect to the previous one?",

    # Style Form
    "style_header": "Comic Style Profile",
    "style_expander": "4. Edit Comic Style Profile",
    "style_overall": "Overall Style",
    "style_base_name": "Base Style Name",
    "style_other": "Specify Other Style",
    "style_char_design": "Character Design",
    "style_char_desc": "Character Style Description",
    "style_char_recurring": "Recurring Character Note",
    "style_char_recurring_help": "Important if part of a series",
    "style_char_expressions": "Key Expressions / Emotions",
    "style_line_art": "Line Art",
    "style_line_weight": "Line Weight",
    "style_line_weight_options": ["clean, consistent medium line weight.", "fine line weight", "bold line weight", "varied line weight", "sketchy"],
    "style_line_style": "Line Style",
    "style_line_style_options": ["digital ink look.", "pencil sketch look", "brush stroke look", "pixelated look"],
    "style_line_color": "Line Color",
    "style_color_theme": "Color Theme",
    "style_palette_style": "Palette Style",
    "style_palette_other": "Specify Other Palette Style",
    "style_background": "Background Description",
    "style_overall_tone": "Overall Tone",
    "style_overall_tone_options": ["warm and light pastel palette", "cool palette", "vintage palette", "high-contrast", "monochrome", "neon"],
    "style_panel_layout": "Panel Layout",
    "style_grid_style": "Grid Style",
    "style_gutter_color": "Gutter Color",
    "style_gutter_width": "Gutter Width",
    "style_gutter_width_options": ["thin", "medium", "thick", "none"],
    "style_border_style": "Border Style",
    "style_border_style_options": ["solid thin line", "solid medium line", "solid thick line", "rounded corners", "no border"],
    "style_border_color": "Border Color",
    "style_text_rendering": "Text Rendering (Hints)",
    "style_font_hint": "Font Style Hint",
    "style_bubble_hint": "Bubble Style Hint",
    "style_other_option": "Other",
    
    # Prompt Display
    "prompt_display_header": "Generated Prompt",
    "prompt_save_question": "Do you want to save this prompt?",
    "prompt_approve_button": "✅ Approve & Save",
    "prompt_approved_success": "Prompt approved and saved! You can find it in the 'Saved Prompts' section.",
    "prompt_save_success": "Prompt saved successfully with ID: {id}",
    "prompt_save_fail": "Failed to save prompt.",
    "prompt_load_fail": "Failed to load prompt {id}",
    "prompt_delete_success": "Prompt deleted successfully!",
    "prompt_delete_fail": "Failed to delete prompt.",
    "prompt_generating": "Generating prompt...",
    "prompt_clipboard_warn": "Install 'streamlit-clipboard' for a dedicated copy button: pip install streamlit-clipboard",
    "prompt_saved_header": "Your Saved Prompts",
    "prompt_saved_empty": "You haven't saved any prompts yet. Create a new prompt and approve it to see it here.",
    "prompt_created_at": "Created: {dt}",
    "prompt_updated_at": "Last Updated: {dt}",
    "prompt_delete_button": "🗑️ Delete",
    
    # Reference Sidebar
    "ref_sidebar_header": "Reference Previews",
    "ref_sidebar_markdown": "Quick examples of some terms:",
    "ref_sidebar_comp": "Composition Angles",
    "ref_sidebar_style": "Example Styles",
    "ref_sidebar_coloring": "Example Coloring",
    "ref_no_preview": "(No image preview for {key})",
    
    # Default values (These need careful consideration)
    "default_core_concept": "A cat tries to get its owner's attention while they work.",
    "default_narrative_arc": "1. Setup: Owner works, cat watches.\n2. Rising Action: Gentle nudge.\n3. Climax/Escalation: Walks on keyboard.\n4. Resolution: Owner gives in.",
    "default_reader_feeling": "Amused, relatable, heartwarming",
    "default_overall_scene": "Simple home office corner with desk, laptop, chair.",
    "default_comic_title": "Work 'Assistant'",
    "default_content_char": "An orange tabby cat 'Mimi'",
    "default_content_action": "progressively distracting its owner who is using a laptop",
    "default_ref_style": "e.g., 'Chi's Sweet Home' manga style",
    "default_ref_char": "Slightly chubby orange tabby cat, big expressive eyes.",
    "default_ref_env": "Modern clean desk setup, laptop, mouse.",
    "default_ref_pose": "Common cat poses (loafing, stretching, walking on things)",
    "default_panel_1_purpose": "Setup: Introduce character/situation",
    "default_panel_1_desc": "Owner typing at laptop. Orange cat 'Mimi' sits nearby, watching intently.",
    "default_panel_1_comp": "Medium shot",
    "default_panel_1_sfx": "tap tap tap (keyboard)",
    "default_panel_2_purpose": "Rising Action: Initial attempt",
    "default_panel_2_desc": "Mimi gently paws at owner's arm. Owner glances slightly annoyed.",
    "default_panel_2_comp": "Close-up",
    "default_panel_2_text": "Hmm?",
    "default_panel_2_placement": "Thought bubble (Owner)",
    "default_panel_2_sfx": "pat pat",
    "default_panel_2_ref": "Cat pleading expression",
    "default_panel_3_purpose": "Turning Point/Escalation: Bold move",
    "default_panel_3_desc": "Mimi walks directly onto the laptop keyboard. Owner stops typing, surprised. Gibberish on screen.",
    "default_panel_3_comp": "Medium shot",
    "default_panel_3_text": "Hey!",
    "default_panel_3_placement": "Speech bubble (Owner)",
    "default_panel_3_sfx": "thump!",
    "default_panel_4_purpose": "Resolution/Reaction: Outcome",
    "default_panel_4_desc": "Owner sighs, hand on face, other hand petting Mimi who is now loafing on keyboard, purring.",
    "default_panel_4_comp": "Medium close-up",
    "default_panel_4_text": "Okay, five-minute break...",
    "default_panel_4_placement": "Thought bubble (Owner)",
    "default_panel_4_sfx": "purrrr~",
    "default_panel_4_ref": "Cat looking smug/satisfied",
    "default_style_name": "Clean Slice-of-Life Anime",
    "default_custom_style_name": "custom style name",
    "default_char_style": "Cute, slightly chibi anthropomorphic cat, simple human elements",
    "default_char_recurring": "**Key: Keep 'Mimi' the orange tabby design and owner's simple style consistent**",
    "default_char_expressions": "Cat: Expectant -> Pleading -> Innocent/Bold -> Satisfied/Smug. Human: Focused -> Annoyed -> Surprised -> Resigned",
    "default_line_color": "dark brown",
    "default_palette_style": "Flat Colors",
    "default_custom_palette_style": "custom palette",
    "default_background": "light cream or pale blue simple background per panel",
    "default_font_hint": "clean, rounded sans-serif comic font",
    "default_bubble_hint": "standard oval (speech), cloud (thought)",
}

# Dictionary for Chinese translations
zh_translations = {
    # Header & Sidebar
    "page_title": "四格漫画提示词生成器",
    "header_title": "📝 四格漫画提示词生成器",
    "header_markdown": "填写以下详细信息，生成用于AI图像生成器的详细提示词。",
    "sidebar_options": "⚙️ 选项",
    "sidebar_language": "语言",
    "sidebar_navigation": "导航",
    "nav_create_new": "创建新提示词",
    "nav_saved_prompts": "已保存提示词",
    "sidebar_about": "ℹ️ 关于",
    "about_text": """
        本工具帮助您为四格漫画创建详细的提示词。
            
        使用方法：
        1. 填写您的漫画细节
        2. 生成提示词
        3. 将提示词复制到您的AI图像生成器中
        4. 保存您喜欢的提示词以供将来参考
            
        使用Streamlit❤️制作。
        """,

    # Story Form
    "story_header": "整体故事与场景",
    "story_expander_1": "1. 整体故事板与叙事流",
    "story_core_concept": "核心概念/主题",
    "story_narrative_arc": "叙事弧线 (可选)",
    "story_reader_feeling": "目标读者感受 (可选)",
    "story_expander_2": "2. 整体场景描述与布局",
    "story_overall_scene": "整体场景/环境",
    "story_comic_title": "尝试漫画标题 (AI可能忽略/失败)",
    "story_content_char": "角色",
    "story_content_action": "核心动作/内容",
    "story_expander_3": "3. 参考图像 (可选)",
    "story_ref_markdown": "提供URL或描述作为视觉指导 (AI可能无法直接访问URL)。",
    "story_ref_style": "整体风格参考",
    "story_ref_char": "角色设计参考",
    "story_ref_env": "环境/物品参考",
    "story_ref_pose": "姿势/构图参考",
    "story_ref_other": "其他参考",

    # Panel Form
    "panel_header": "单格细节",
    "panel_subheader_1": "第1格: 左上",
    "panel_subheader_2": "第2格: 右上",
    "panel_subheader_3": "第3格: 左下",
    "panel_subheader_4": "第4格: 右下",
    "panel_expander_edit": "编辑第 {i} 格细节",
    "panel_purpose": "[{i}] 叙事作用",
    "panel_desc": "[{i}] 画面描述",
    "panel_comp": "[{i}] 构图/视角",
    "panel_comp_select": "选择构图",
    "panel_comp_other": "指定其他构图",
    "panel_text": "[{i}] 文字内容",
    "panel_placement": "[{i}] 文字位置",
    "panel_placement_options": ["无文字", "下方标题", "对话气泡", "思考气泡", "标志/屏幕文字", "音效文字"],
    "panel_sfx": "[{i}] 音效 (可选)",
    "panel_ref": "[{i}] 具体参考 (可选)",
    "panel_transition": "[{i}] 与前格联系 (可选)",
    "panel_transition_help": "此格如何与上一格连接？",

    # Style Form
    "style_header": "漫画风格配置文件",
    "style_expander": "4. 编辑漫画风格配置文件",
    "style_overall": "整体风格",
    "style_base_name": "基础风格名称",
    "style_other": "指定其他风格",
    "style_char_design": "角色设计",
    "style_char_desc": "角色风格描述",
    "style_char_recurring": "固定角色备注",
    "style_char_recurring_help": "如果是系列作品的一部分，则很重要",
    "style_char_expressions": "关键表情/情绪",
    "style_line_art": "线条艺术",
    "style_line_weight": "线条粗细",
    "style_line_weight_options": ["干净、一致的中等粗细线条", "细线条", "粗线条", "变化的线条粗细", "素描感"],
    "style_line_style": "线条风格",
    "style_line_style_options": ["数字墨水外观", "铅笔素描外观", "笔触外观", "像素化外观"],
    "style_line_color": "线条颜色",
    "style_color_theme": "色彩主题",
    "style_palette_style": "调色板风格",
    "style_palette_other": "指定其他调色板风格",
    "style_background": "背景描述",
    "style_overall_tone": "整体色调",
    "style_overall_tone_options": ["温暖明亮的柔和调色板", "冷色调", "复古调色板", "高对比度", "单色", "霓虹"],
    "style_panel_layout": "画格布局",
    "style_grid_style": "网格风格",
    "style_gutter_color": "间隙颜色",
    "style_gutter_width": "间隙宽度",
    "style_gutter_width_options": ["窄", "中", "宽", "无"],
    "style_border_style": "边框风格",
    "style_border_style_options": ["实线细边框", "实线中等边框", "实线粗边框", "圆角", "无边框"],
    "style_border_color": "边框颜色",
    "style_text_rendering": "文本渲染 (提示)",
    "style_font_hint": "字体风格提示",
    "style_bubble_hint": "气泡风格提示",
    "style_other_option": "其他",
    
    # Prompt Display
    "prompt_display_header": "生成的提示词",
    "prompt_save_question": "您想保存此提示词吗？",
    "prompt_approve_button": "✅ 批准并保存",
    "prompt_approved_success": "提示词已批准并保存！您可以在'已保存提示词'部分找到它。",
    "prompt_save_success": "提示词成功保存，ID: {id}",
    "prompt_save_fail": "保存提示词失败。",
    "prompt_load_fail": "加载提示词失败 {id}",
    "prompt_delete_success": "提示词删除成功！",
    "prompt_delete_fail": "删除提示词失败。",
    "prompt_generating": "正在生成提示词...",
    "prompt_clipboard_warn": "安装 'streamlit-clipboard' 以获得专用复制按钮: pip install streamlit-clipboard",
    "prompt_saved_header": "您已保存的提示词",
    "prompt_saved_empty": "您还没有保存任何提示词。创建一个新提示词并批准它，即可在此处看到。",
    "prompt_created_at": "创建于: {dt}",
    "prompt_updated_at": "最后更新: {dt}",
    "prompt_delete_button": "🗑️ 删除",
    
    # Reference Sidebar
    "ref_sidebar_header": "参考预览",
    "ref_sidebar_markdown": "一些术语的快速示例：",
    "ref_sidebar_comp": "构图角度",
    "ref_sidebar_style": "示例风格",
    "ref_sidebar_coloring": "示例着色",
    "ref_no_preview": "({key} 无图像预览)",
    
    # Default values (Chinese)
    "default_core_concept": "一只猫试图在主人工作时引起他们的注意。",
    "default_narrative_arc": "1. 设置: 主人工作，猫观看。\n2. 上升动作: 轻轻推 nudge。\n3. 高潮/升级: 走上键盘。\n4. 解决: 主人屈服。",
    "default_reader_feeling": "有趣，感同身受，暖心",
    "default_overall_scene": "简单的家庭办公室角落，有书桌、笔记本电脑、椅子。",
    "default_comic_title": "工作'助理'",
    "default_content_char": "一只名叫'咪咪'的橘色虎斑猫",
    "default_content_action": "逐渐分散正在使用笔记本电脑的主人的注意力",
    "default_ref_style": "例如，'甜甜私房猫' 漫画风格",
    "default_ref_char": "略胖的橘色虎斑猫，富有表现力的大眼睛。",
    "default_ref_env": "现代简洁的书桌设置，笔记本电脑，鼠标。",
    "default_ref_pose": "常见的猫姿势 (揣手手，伸懒腰，在东西上行走)",
    "default_panel_1_purpose": "设置: 介绍角色/情况",
    "default_panel_1_desc": "主人在笔记本电脑前打字。橘猫'咪咪'坐在附近，专注地看着。",
    "default_panel_1_comp": "中景",
    "default_panel_1_sfx": "哒哒哒 (键盘声)",
    "default_panel_2_purpose": "上升动作: 初次尝试",
    "default_panel_2_desc": "咪咪轻轻地用爪子碰主人的手臂。主人略带恼怒地瞥了一眼。",
    "default_panel_2_comp": "特写",
    "default_panel_2_text": "嗯？",
    "default_panel_2_placement": "思考气泡 (主人)",
    "default_panel_2_sfx": "拍拍",
    "default_panel_2_ref": "猫咪恳求的表情",
    "default_panel_3_purpose": "转折点/升级: 大胆行动",
    "default_panel_3_desc": "咪咪直接走上笔记本电脑键盘。主人停止打字，很惊讶。屏幕上出现乱码。",
    "default_panel_3_comp": "中景",
    "default_panel_3_text": "嘿！",
    "default_panel_3_placement": "对话气泡 (主人)",
    "default_panel_3_sfx": "砰！",
    "default_panel_4_purpose": "解决/反应: 结果",
    "default_panel_4_desc": "主人叹了口气，一只手捂着脸，另一只手抚摸着正揣手手趴在键盘上打呼噜的咪咪。",
    "default_panel_4_comp": "中近景",
    "default_panel_4_text": "好吧，休息五分钟...",
    "default_panel_4_placement": "思考气泡 (主人)",
    "default_panel_4_sfx": "呼噜噜~",
    "default_panel_4_ref": "猫咪看起来得意/满足",
    "default_style_name": "清新日常动漫",
    "default_custom_style_name": "自定义风格名称",
    "default_char_style": "可爱，略带Q版的拟人化猫，简约人类元素",
    "default_char_recurring": "**关键：保持'咪咪'的橘猫虎斑设计和主人简洁风格一致**",
    "default_char_expressions": "猫: 期待 -> 恳求 -> 无辜/大胆 -> 满足/得意。人: 专注 -> 烦恼 -> 惊讶 -> 无奈",
    "default_line_color": "深棕色",
    "default_palette_style": "平涂颜色",
    "default_custom_palette_style": "自定义调色板",
    "default_background": "每格使用浅奶油色或淡蓝色简约背景",
    "default_font_hint": "干净、圆润的无衬线漫画字体",
    "default_bubble_hint": "标准椭圆形 (对话), 云形 (思考)",
}

# Combine translations
translations = {
    "English": en_translations,
    "中文": zh_translations
}

def get_translation(key: str, lang: str) -> str:
    """Get the translation for a given key and language.

    Args:
        key: The translation key
        lang: The selected language ('English' or '中文')

    Returns:
        The translated string, defaulting to English if not found.
    """
    return translations.get(lang, en_translations).get(key, en_translations.get(key, f"MISSING_KEY: {key}"))

def get_translator(lang: str):
    """Returns a function that translates based on the given language.

    Args:
        lang: The selected language.

    Returns:
        A function that takes a key and returns the translation.
    """
    def translator(key: str) -> str:
        return get_translation(key, lang)
    return translator

# Initialize language in session state if not present
def initialize_language():
    if 'language' not in st.session_state:
        # Attempt to detect browser language (basic approach)
        try:
            # This header might not always be available or reliable
            accept_language = st.query_params.get('accept-language', ['en'])[0]
            if 'zh' in accept_language.lower():
                st.session_state['language'] = '中文'
            else:
                st.session_state['language'] = 'English'
        except Exception:
             st.session_state['language'] = 'English' 