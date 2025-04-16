"""Story form component for the UI."""
from typing import Callable, Dict, Any

import streamlit as st

from ..utils.reference_images import show_reference_image, REFERENCE_IMAGES
from ..core.models import Panel, StyleProfile
from ..utils.translations import en_translations


def render_story_section(t: Callable[[str], str]) -> Dict[str, Any]:
    """Render the overall story and scene section.

    Args:
        t: The translation function.

    Returns:
        A dictionary containing the story input data.
    """
    st.header(t("story_header"))

    with st.expander(t("story_expander_1"), expanded=True):
        core_concept = st.text_input(
            t("story_core_concept"), 
            placeholder=t("default_core_concept")
        )
        narrative_arc = st.text_area(
            t("story_narrative_arc"), 
            placeholder=t("default_narrative_arc"),
            height=100
        )
        reader_feeling = st.text_input(
            t("story_reader_feeling"), 
            placeholder=t("default_reader_feeling")
        )

    with st.expander(t("story_expander_2"), expanded=True):
        overall_scene = st.text_input(
            t("story_overall_scene"), 
            placeholder=t("default_overall_scene")
        )
        comic_title = st.text_input(
            t("story_comic_title"), 
            placeholder=t("default_comic_title")
        )
        content_summary_char = st.text_input(
            t("story_content_char"), 
            placeholder=t("default_content_char")
        )
        content_summary_action = st.text_input(
            t("story_content_action"), 
            placeholder=t("default_content_action")
        )

    with st.expander(t("story_expander_3"), expanded=False):
        st.markdown(t("story_ref_markdown"))
        ref_overall_style = st.text_input(
            t("story_ref_style"), 
            placeholder=t("default_ref_style")
        )
        ref_character = st.text_input(
            t("story_ref_char"), 
            placeholder=t("default_ref_char")
        )
        ref_environment = st.text_input(
            t("story_ref_env"), 
            placeholder=t("default_ref_env")
        )
        ref_pose = st.text_input(
            t("story_ref_pose"), 
            placeholder=t("default_ref_pose")
        )
        ref_other = st.text_input(t("story_ref_other"), placeholder="Optional")
        
    return {
        "core_concept": core_concept,
        "narrative_arc": narrative_arc,
        "reader_feeling": reader_feeling,
        "overall_scene": overall_scene,
        "comic_title": comic_title,
        "content_summary_char": content_summary_char,
        "content_summary_action": content_summary_action,
        "ref_overall_style": ref_overall_style,
        "ref_character": ref_character,
        "ref_environment": ref_environment,
        "ref_pose": ref_pose,
        "ref_other": ref_other
    }


def render_panel_section(t: Callable[[str], str]) -> Dict[str, Panel]:
    """Render the panel details section.
    
    Args:
        t: The translation function.
        
    Returns:
        A dictionary mapping panel numbers (as strings) to Panel objects.
    """
    st.header(t("panel_header"))

    panels = {}
    # Define keys for default values
    default_panel_keys = {
        1: {
            "purpose": "default_panel_1_purpose", 
            "desc": "default_panel_1_desc", 
            "comp": "default_panel_1_comp", 
            "text": "", # Empty default text
            "placement": "No text", # Use EN string as key, map later if needed
            "sfx": "default_panel_1_sfx", 
            "ref": "",
            "transition": ""
        },
        2: {
            "purpose": "default_panel_2_purpose", 
            "desc": "default_panel_2_desc", 
            "comp": "default_panel_2_comp", 
            "text": "default_panel_2_text", 
            "placement": "Thought bubble (Owner)",
            "sfx": "default_panel_2_sfx", 
            "ref": "default_panel_2_ref",
            "transition": ""
        },
        3: {
            "purpose": "default_panel_3_purpose", 
            "desc": "default_panel_3_desc", 
            "comp": "default_panel_3_comp", 
            "text": "default_panel_3_text", 
            "placement": "Speech bubble (Owner)",
            "sfx": "default_panel_3_sfx", 
            "ref": "",
            "transition": ""
        },
        4: {
            "purpose": "default_panel_4_purpose", 
            "desc": "default_panel_4_desc", 
            "comp": "default_panel_4_comp", 
            "text": "default_panel_4_text", 
            "placement": "Thought bubble (Owner)",
            "sfx": "default_panel_4_sfx", 
            "ref": "default_panel_4_ref",
            "transition": ""
        },
    }

    panel_cols = st.columns(2)
    panel_placement_options_en = en_translations["panel_placement_options"] # Use EN for keys
    panel_placement_options_translated = t("panel_placement_options")

    for i in range(1, 5):
        col_index = (i - 1) % 2
        with panel_cols[col_index]:
            panel_subheaders = {
                1: t("panel_subheader_1"),
                2: t("panel_subheader_2"),
                3: t("panel_subheader_3"),
                4: t("panel_subheader_4")
            }
            st.subheader(panel_subheaders[i])
            with st.expander(t("panel_expander_edit").format(i=i), expanded=(i==1)):
                defaults = default_panel_keys[i]
                panels[str(i)] = {}
                
                # Get translated default values for placeholders
                default_purpose = t(defaults['purpose'])
                default_desc = t(defaults['desc'])
                default_comp_key = defaults['comp']
                default_text = t(defaults['text']) if defaults['text'] else ""
                default_sfx = t(defaults['sfx'])
                default_ref = t(defaults['ref']) if defaults['ref'] else ""
                default_transition = t(defaults['transition']) if defaults['transition'] else ""
                default_placement_en = defaults['placement']
                default_placement_index = panel_placement_options_en.index(default_placement_en) if default_placement_en in panel_placement_options_en else 0
                
                panels[str(i)]['purpose'] = st.text_input(
                    t("panel_purpose").format(i=i), 
                    placeholder=default_purpose, # Use placeholder
                    key=f"p{i}_purpose"
                )
                panels[str(i)]['desc'] = st.text_area(
                    t("panel_desc").format(i=i), 
                    placeholder=default_desc, # Use placeholder
                    key=f"p{i}_desc", 
                    height=100
                )

                # Composition with Reference Image
                st.write(t("panel_comp").format(i=i))
                comp_options = list(REFERENCE_IMAGES["composition"].keys()) + [t("style_other_option")]
                # Find index for default composition
                default_comp_index = comp_options.index(default_comp_key) if default_comp_key in comp_options else len(comp_options)-1
                selected_comp = st.selectbox(
                    t("panel_comp_select"), 
                    comp_options, 
                    index=default_comp_index, # Keep default selection index
                    key=f"p{i}_comp_select"
                )
                if selected_comp != t("style_other_option"):
                    panels[str(i)]['comp'] = selected_comp
                    show_reference_image("composition", selected_comp)
                else:
                    # Placeholder for 'Other' composition input
                    panels[str(i)]['comp'] = st.text_input(t("panel_comp_other"), placeholder=t("panel_comp_other"), key=f"p{i}_comp_other")

                panels[str(i)]['text'] = st.text_input(
                    t("panel_text").format(i=i), 
                    placeholder=default_text if default_text else "Optional text", # Use placeholder
                    key=f"p{i}_text"
                )
                
                selected_placement_display = st.selectbox(
                    t("panel_placement").format(i=i), 
                    panel_placement_options_translated, 
                    index=default_placement_index, # Keep default selection index
                    key=f"p{i}_placement"
                )
                selected_placement_index = panel_placement_options_translated.index(selected_placement_display)
                panels[str(i)]['placement'] = panel_placement_options_en[selected_placement_index]
                
                panels[str(i)]['sfx'] = st.text_input(
                    t("panel_sfx").format(i=i), 
                    placeholder=default_sfx if default_sfx else "e.g., WOOSH, BANG", # Use placeholder
                    key=f"p{i}_sfx"
                )
                panels[str(i)]['ref'] = st.text_input(
                    t("panel_ref").format(i=i), 
                    placeholder=default_ref if default_ref else "e.g., specific character expression", # Use placeholder
                    key=f"p{i}_ref"
                )
                panels[str(i)]['transition'] = st.text_input(
                    t("panel_transition").format(i=i), 
                    placeholder=default_transition if default_transition else "e.g., zoom in, next day", # Use placeholder
                    key=f"p{i}_transition", 
                    help=t("panel_transition_help")
                )
                
    panel_objects = {i: Panel(**panels[i]) for i in panels}
    return panel_objects


def render_style_section(t: Callable[[str], str]) -> StyleProfile:
    """Render the comic style profile section.
    
    Args:
        t: The translation function.
        
    Returns:
        A StyleProfile object containing the style input data.
    """
    st.header(t("style_header"))
    with st.expander(t("style_expander"), expanded=True):
        style_cols = st.columns(2)
        other_option_translated = t("style_other_option")
        
        with style_cols[0]:
            st.subheader(t("style_overall"))
            style_options = list(REFERENCE_IMAGES["style"].keys()) + [other_option_translated]
            default_style_name_en = en_translations["default_style_name"] 
            default_style_index = style_options.index(default_style_name_en) if default_style_name_en in style_options else 0
            
            selected_style = st.selectbox(
                t("style_base_name"), 
                style_options, 
                index=default_style_index, # Keep default selection index
                key="style_name_select"
            )
            if selected_style != other_option_translated:
                style_name = selected_style
                show_reference_image("style", selected_style)
            else:
                style_name = st.text_input(t("style_other"), placeholder=t("default_custom_style_name"), key="style_name_other") # Placeholder

            st.subheader(t("style_char_design"))
            char_style = st.text_input(
                t("style_char_desc"), 
                placeholder=t("default_char_style"), # Placeholder
                key="char_style"
            )
            char_recurring = st.text_input(
                t("style_char_recurring"), 
                placeholder=t("default_char_recurring"), # Placeholder
                key="char_recurring", 
                help=t("style_char_recurring_help")
            )
            char_expressions = st.text_area(
                t("style_char_expressions"), 
                placeholder=t("default_char_expressions"), # Placeholder
                key="char_expressions", 
                height=75
            )

            st.subheader(t("style_line_art"))
            line_weight_options_en = en_translations["style_line_weight_options"]
            line_weight_options_translated = t("style_line_weight_options")
            default_lw_index = 0 # Default to first option
            line_weight_display = st.selectbox(
                t("style_line_weight"), 
                line_weight_options_translated,
                index=default_lw_index, # Keep default selection index
                key="line_weight"
            )
            line_weight = line_weight_options_en[line_weight_options_translated.index(line_weight_display)]
            
            line_style_options_en = en_translations["style_line_style_options"]
            line_style_options_translated = t("style_line_style_options")
            default_ls_index = 0 # Default to first option
            line_style_display = st.selectbox(
                t("style_line_style"), 
                line_style_options_translated,
                index=default_ls_index, # Keep default selection index
                key="line_style"
            )
            line_style = line_style_options_en[line_style_options_translated.index(line_style_display)]
            
            line_color = st.text_input(t("style_line_color"), placeholder=t("default_line_color"), key="line_color") # Placeholder

        with style_cols[1]:
            st.subheader(t("style_color_theme"))
            color_palette_options = list(REFERENCE_IMAGES["coloring"].keys()) + [other_option_translated]
            default_palette_style_en = en_translations["default_palette_style"]
            default_palette_index = color_palette_options.index(default_palette_style_en) if default_palette_style_en in color_palette_options else 0
            
            selected_palette = st.selectbox(
                t("style_palette_style"), 
                color_palette_options, 
                index=default_palette_index, # Keep default selection index
                key="palette_select"
            )
            if selected_palette != other_option_translated:
                 palette_style = selected_palette
                 show_reference_image("coloring", selected_palette)
            else:
                 palette_style = st.text_input(t("style_palette_other"), placeholder=t("default_custom_palette_style"), key="palette_other") # Placeholder

            background = st.text_input(
                t("style_background"), 
                placeholder=t("default_background"), # Placeholder
                key="background"
            )
            
            overall_tone_options_en = en_translations["style_overall_tone_options"]
            overall_tone_options_translated = t("style_overall_tone_options")
            default_ot_index = 0 # Default to first option
            overall_tone_display = st.selectbox(
                t("style_overall_tone"), 
                overall_tone_options_translated,
                index=default_ot_index, # Keep default selection index
                key="overall_tone"
            )
            overall_tone = overall_tone_options_en[overall_tone_options_translated.index(overall_tone_display)]

            st.subheader(t("style_panel_layout"))
            grid_style = st.text_input(t("style_grid_style"), "standard 2x2", key="grid_style", disabled=True) # Grid style likely doesn't need placeholder
            gutter_color = st.color_picker(t("style_gutter_color"), "#FFFFFF", key="gutter_color") # Color picker needs a default value
            
            gutter_width_options_en = en_translations["style_gutter_width_options"]
            gutter_width_options_translated = t("style_gutter_width_options")
            default_gw_index = 1 # Default to medium
            gutter_width_display = st.selectbox(
                t("style_gutter_width"), 
                gutter_width_options_translated,
                index=default_gw_index, # Keep default selection index
                key="gutter_width"
            )
            gutter_width = gutter_width_options_en[gutter_width_options_translated.index(gutter_width_display)]
            
            border_style_options_en = en_translations["style_border_style_options"]
            border_style_options_translated = t("style_border_style_options")
            default_bs_index = 0 # Default to solid thin line
            border_style_display = st.selectbox(
                t("style_border_style"), 
                border_style_options_translated,
                index=default_bs_index, # Keep default selection index
                key="border_style"
            )
            border_style = border_style_options_en[border_style_options_translated.index(border_style_display)]
            
            border_color = st.color_picker(t("style_border_color"), "#4B3A26", key="border_color") # Color picker needs a default value

            st.subheader(t("style_text_rendering"))
            font_hint = st.text_input(
                t("style_font_hint"), 
                placeholder=t("default_font_hint"), # Placeholder
                key="font_hint"
            )
            bubble_style = st.text_input(
                t("style_bubble_hint"), 
                placeholder=t("default_bubble_hint"), # Placeholder
                key="bubble_style"
            )
    
    # Create StyleProfile object
    style_profile = StyleProfile(
        style_name=style_name,
        char_style=char_style,
        char_recurring=char_recurring,
        char_expressions=char_expressions,
        line_weight=line_weight,
        line_style=line_style,
        line_color=line_color,
        palette_style=palette_style,
        background=background,
        overall_tone=overall_tone,
        grid_style=grid_style,
        gutter_color=gutter_color,
        gutter_width=gutter_width,
        border_style=border_style,
        border_color=border_color,
        font_hint=font_hint,
        bubble_style=bubble_style
    )
    
    return style_profile 