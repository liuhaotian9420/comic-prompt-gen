"""UI components for displaying and managing prompts."""
from typing import Callable, Dict, Any

import streamlit as st

from ..core.models import ComicPrompt
from ..storage.prompt_storage import get_storage


def display_prompt(t: Callable[[str], str], prompt_text: str) -> bool:
    """Display a generated prompt with copy button and approval options.
    
    Args:
        t: The translation function.
        prompt_text: The prompt text to display
        
    Returns:
        True if the prompt was approved, False otherwise
    """
    st.header(t("prompt_display_header"))
    
    # Display the prompt in a code block (which usually has a copy button)
    st.code(prompt_text, language="markdown")
    
    # Optional: Add explicit copy button using a third-party component if needed
    # (Uncomment if you install streamlit-clipboard)
    # try:
    #     from streamlit_clipboard import st_clipboard
    #     st_clipboard(prompt_text)
    # except ImportError:
    #     st.warning(t("prompt_clipboard_warn"))
    
    # Prompt feedback and approval
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(t("prompt_save_question"))
    
    with col2:
        approved = st.button(t("prompt_approve_button"), key="approve_prompt")
        
    if approved:
        st.success(t("prompt_approved_success"))
        
    return approved


def render_saved_prompts(t: Callable[[str], str]):
    """Render the saved prompts page.
    
    Args:
        t: The translation function.
    """
    st.header(t("prompt_saved_header"))
    
    # Get the storage instance
    storage = get_storage()
    
    # List all saved prompts
    prompts = storage.list_prompts()
    
    if not prompts:
        st.info(t("prompt_saved_empty"))
        return
    
    # Display each prompt in a card-like format
    for prompt_meta in prompts:
        with st.expander(f"**{prompt_meta['core_concept']}**", expanded=False):
            # Load the full prompt
            prompt_id = prompt_meta['id']
            prompt_obj = storage.load_prompt(prompt_id)
            
            if prompt_obj:
                # Display basic info
                created_dt_str = prompt_obj.created_at.strftime("%Y-%m-%d %H:%M")
                st.write(t("prompt_created_at").format(dt=created_dt_str))
                if prompt_obj.updated_at:
                    updated_dt_str = prompt_obj.updated_at.strftime("%Y-%m-%d %H:%M")
                    st.write(t("prompt_updated_at").format(dt=updated_dt_str))
                
                # Display the prompt
                st.code(prompt_obj.generated_prompt, language="markdown")
                
                # Actions
                col1, col2 = st.columns([1,3]) # Adjust column ratio for button placement
                with col1:
                    if st.button(t("prompt_delete_button"), key=f"delete_{prompt_id}"):
                        if storage.delete_prompt(prompt_id):
                            st.success(t("prompt_delete_success"))
                            st.rerun()
                        else:
                            st.error(t("prompt_delete_fail"))
                
                # Placeholder for potential future actions
                # with col2:
                #     pass 
            else:
                st.error(t("prompt_load_fail").format(id=prompt_id))


def save_prompt(t: Callable[[str], str], comic_prompt: ComicPrompt) -> None:
    """Save a prompt to storage.
    
    Args:
        t: The translation function.
        comic_prompt: The ComicPrompt object to save
    """
    storage = get_storage()
    prompt_id = storage.save_prompt(comic_prompt)
    
    if prompt_id:
        # We show success message in the display_prompt function upon button click
        pass
    else:
        st.error(t("prompt_save_fail")) 