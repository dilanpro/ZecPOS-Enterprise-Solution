"""Admin Page"""
import streamlit as st
from services.auth import logout
from streamlit_option_menu import option_menu


def render():
    """Render admin page"""

    with st.sidebar:
        selected_page = option_menu(
            menu_title=None,
            options=["POS", "Inventory", "Reports"],
            icons=["laptop", "box-seam", "file-earmark-ruled"],
        )

    with st.container():
        st.text("Hi There")

    st.selectbox("Select", ["Option 1", "Option 2"])

    st.button("Logout", on_click=logout)
