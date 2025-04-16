"""Reference image utilities for the comic prompt generator."""
from typing import Dict, Any

import streamlit as st
from ..utils.translations import get_translation # Import for fallback message

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

def show_reference_image(category: str, key: str, caption: str = None) -> None:
    """Display a reference image from the predefined categories.
    
    Args:
        category: The category of the reference image
        key: The key for the specific image within the category
        caption: Optional override caption. If None, uses the key.
    """
    display_caption = caption if caption is not None else key
    if key in REFERENCE_IMAGES.get(category, {}):
        st.image(REFERENCE_IMAGES[category][key], caption=display_caption, width=150)
    else:
        # Use translator for the fallback message
        lang = st.session_state.get('language', 'English') # Get current language
        fallback_caption = get_translation("ref_no_preview", lang).format(key=key)
        st.caption(fallback_caption) 