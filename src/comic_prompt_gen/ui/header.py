"""Header component for the Streamlit UI."""
from typing import Callable

import streamlit as st

from ..utils.translations import get_translator, translations, initialize_language


def render_header(t: Callable[[str], str]):
    """Render the application header.

    Args:
        t: The translation function.
    """
    # st.set_page_config(page_title=t("page_title"), layout="wide")
    st.title(t("header_title"))
    st.markdown(t("header_markdown"))


def render_sidebar() -> tuple[str, str]:
    """Render the application sidebar and return selected page and language.
    
    Returns:
        A tuple containing the selected page and the selected language.
    """
    initialize_language() # Set default language if not already set
    
    with st.sidebar:
        t = get_translator(st.session_state.language)
        st.header(t("sidebar_options"))
        
        # Language Selector
        selected_language = st.selectbox(
            t("sidebar_language"), 
            options=list(translations.keys()),
            key="language" # Use session state key
        )
        
        # Update translator if language changed
        if selected_language != st.session_state.language:
             t = get_translator(selected_language)
             # No need to rerun here, session state handles updates
             
        # Navigation
        st.divider()
        st.subheader(t("sidebar_navigation"))
        page = st.radio(
            t("sidebar_navigation"), 
            options=[t("nav_create_new"), t("nav_saved_prompts")],
            label_visibility="collapsed",
            index=0,
            key="navigation"
        )
        
        # About section
        st.divider()
        with st.expander(t("sidebar_about"), expanded=False):
            st.markdown(t("about_text"))
        
        return page, selected_language 