"""User Authentication"""
import streamlit as st
from models import db, User


def login(username: str, password: str):
    """Login a User"""
    print("UN", username, "PW", password)

    user = db.query(User).filter(User.username == username).first()
    if user and user.check_password(password):
        st.session_state["username"] = username
        return True
    return False


def logout():
    """Logout a User"""
    # TODO: Implement Logout with Firebase
    st.session_state.clear()
