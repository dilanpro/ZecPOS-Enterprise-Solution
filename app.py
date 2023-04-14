"""Main Initializer of the Application"""
from typing import List
import streamlit as st
import os
from views import login, dashboard


class Routes:
    """Routes Enum"""
    LOGIN = "login"
    DASHBOARD = "dashboard"


def init():
    """Main Entry Point"""
    print("REQUEST", {
        "username": st.session_state.get("username", "NOT LOGGED IN"),
        "route": st.session_state.get("route", "/")
    })

    st.set_page_config(
        page_title="ZecPOS | The Most Affordable POS Solution",
        page_icon=":smile:",
        layout="wide",
    )

    if st.session_state.get("route", Routes.LOGIN) == Routes.LOGIN:
        login.render()
    elif st.session_state["route"] == Routes.DASHBOARD:
        dashboard.render()

    __include_css()

    # Commit DB changes if any
    # noinspection PyBroadException
    try:
        from models import db
        db.commit()
    except Exception:
        pass


def __include_css():
    css: str = ""
    static_css_path: str = "static/css"
    css_files: List = os.listdir(static_css_path)
    for _file in css_files:
        with open(f"{static_css_path}/{_file}") as f:
            css += f.read()

    st.markdown(f"<style>\n{css}\n</style>", unsafe_allow_html=True)


if __name__ == "__main__":
    init()
