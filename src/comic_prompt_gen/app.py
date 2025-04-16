"""Main Streamlit application for Comic Prompt Generator."""
import streamlit as st

from .ui.header import render_header, render_sidebar
from .ui.story_form import render_story_section, render_panel_section, render_style_section
from .ui.prompt_display import display_prompt, render_saved_prompts, save_prompt
from .ui.reference_sidebar import render_reference_sidebar
from .core.models import ComicPrompt
from .core.prompt_generator import generate_prompt
from .utils.translations import get_translator, translations # Import translator


def create_new_prompt(t):
    """Create a new comic prompt.
    
    Args:
        t: The translation function.
    """
    # Main layout with two columns
    col1, col2 = st.columns([2, 1])  # Main input area and reference sidebar

    with col1:
        # Render story, panel, and style sections using the translator
        story_data = render_story_section(t)
        panels = render_panel_section(t)
        style = render_style_section(t)
        
        # Create a comic prompt object
        comic_prompt = ComicPrompt(
            **story_data,
            panels=panels,
            style=style
        )
        
        # Generate button
        if st.button(t("prompt_generating"), type="primary"):
            with st.spinner(t("prompt_generating")):
                # Generate the prompt text
                prompt_text = generate_prompt(comic_prompt)
                
                # Store the generated prompt in the object
                comic_prompt.generated_prompt = prompt_text
                
                # Display the prompt and get approval status
                is_approved = display_prompt(t, prompt_text)
                
                # If approved, save it
                if is_approved:
                    comic_prompt.is_approved = True
                    save_prompt(t, comic_prompt)

    # Reference sidebar
    with col2:
        render_reference_sidebar(t)


def main():
    """Main application function."""
    # Get selected language first, *before* any other st commands
    # This might require initializing language slightly differently or 
    # ensuring sidebar is setup to get language first if possible.
    # Let's call set_page_config first, using a default or initial language.
    
    # Initialize language state if not present
    from .utils.translations import initialize_language
    initialize_language()
    initial_lang = st.session_state.language
    initial_t = get_translator(initial_lang)
    st.set_page_config(page_title=initial_t("page_title"), layout="wide")
    
    # Now render sidebar to get the potentially updated language and page
    page_key, lang = render_sidebar() # Returns page key and language
    
    # Get the appropriate translator function based on sidebar selection
    t = get_translator(lang)
    
    # Render header (without set_page_config) 
    render_header(t)
    
    # Get translated page names for comparison
    create_page_name = t("nav_create_new")
    saved_page_name = t("nav_saved_prompts")
    
    # Display the appropriate page based on selection
    if page_key == create_page_name:
        create_new_prompt(t)
    elif page_key == saved_page_name:
        render_saved_prompts(t)


if __name__ == "__main__":
    main() 