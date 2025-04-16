"""Reference sidebar component for the UI."""
from typing import Callable

import streamlit as st

from ..utils.reference_images import show_reference_image, REFERENCE_IMAGES
from ..utils.translations import get_translation # Need this for default caption


def render_reference_sidebar(t: Callable[[str], str]):
    """Render the reference image sidebar.
    
    Args:
        t: The translation function.
    """
    st.header(t("ref_sidebar_header"))
    st.markdown(t("ref_sidebar_markdown"))

    with st.expander(t("ref_sidebar_comp"), expanded=False):
        for key in REFERENCE_IMAGES["composition"]:
            # Use translated caption if available, otherwise use key
            translated_caption = t(f"comp_{key.lower().replace(' ', '_')}") # Example key format
            caption_to_show = translated_caption if "MISSING_KEY" not in translated_caption else key
            show_reference_image("composition", key, caption_to_show)

    with st.expander(t("ref_sidebar_style"), expanded=False):
        for key in REFERENCE_IMAGES["style"]:
            translated_caption = t(f"style_{key.lower().replace(' ', '_')}")
            caption_to_show = translated_caption if "MISSING_KEY" not in translated_caption else key
            show_reference_image("style", key, caption_to_show)

    with st.expander(t("ref_sidebar_coloring"), expanded=False):
        for key in REFERENCE_IMAGES["coloring"]:
            translated_caption = t(f"coloring_{key.lower().replace(' ', '_')}")
            caption_to_show = translated_caption if "MISSING_KEY" not in translated_caption else key
            show_reference_image("coloring", key, caption_to_show)
            
# Need to update show_reference_image to accept a caption override
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