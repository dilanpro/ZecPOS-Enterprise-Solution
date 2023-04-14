"""Login Page"""
import streamlit as st

from app import Routes
from consts import Roles
from models import Domain, db, User
from services.auth import login


def render():
    """Render login page"""

    domains = db.query(Domain).all()
    if len(domains) == 0:
        print("IN")
        _, main_column, _ = st.columns([1, 2, 1])
        with main_column:

            admin_name = st.text_input(label="Admin Name", placeholder="Admin Name")
            admin_username = st.text_input(label="Admin Username", placeholder="Admin Email")
            admin_password = st.text_input(label="Admin Password", placeholder="Admin Password", type="password")
            domain_name = st.text_input(label="Domain Name", placeholder="Domain Name")

            def __signup_call():
                # Admin Name is required
                if admin_name == "":
                    st.error("Admin Name is required")
                    return

                # Admin Username is required
                if admin_username == "":
                    st.error("Admin Username is required")
                    return
                # Admin Username should be at least 6 characters
                if len(admin_username) < 6:
                    st.error("Admin Username should be at least 6 characters")
                    return

                # Admin Password is required
                if admin_password == "":
                    st.error("Admin Password is required")
                    return
                # Admin Password should be at least 12 characters
                if len(admin_password) < 12:
                    st.error("Admin Password should be at least 12 characters")
                    return
                # Admin Password should contain at least 1 number
                if not any(char.isdigit() for char in admin_password):
                    st.error("Admin Password should contain at least 1 number")
                    return
                # Admin Password should contain at least 1 uppercase
                if not any(char.isupper() for char in admin_password):
                    st.error("Admin Password should contain at least 1 uppercase")
                    return
                # Admin Password should contain at least 1 lowercase
                if not any(char.islower() for char in admin_password):
                    st.error("Admin Password should contain at least 1 lowercase")
                    return
                # Admin Password should contain at least 1 special character
                if not any(not char.isalnum() for char in admin_password):
                    st.error("Admin Password should contain at least 1 special character")
                    return

                # Domain Name is required
                if domain_name == "":
                    st.error("Domain Name is required")
                    return

                # Create Admin Record
                admin = User()
                admin.name = admin_name
                admin.username = admin_username
                admin.password = User.hash(admin_password)
                admin.role = Roles.ADMIN.value
                db.add(admin)

                # Create Domain Record
                domain = Domain()
                domain.name = domain_name
                domain.onboard_admin_id = db.query(User).filter(User.username == admin_username).first().id
                db.add(domain)

            st.button("Submit", use_container_width=True, on_click=__signup_call)

    else:
        _, main_column, _ = st.columns([1, 2, 1])
        with main_column:
            username = st.text_input(label="Email", placeholder="Your Email")
            password = st.text_input(label="Password", placeholder="Your Password", type="password")

            def __login_call():

                # Username is required
                if username == "":
                    st.session_state["error"] = True
                    return

                # Password is required
                if password == "":
                    st.session_state["error"] = True
                    return

                is_valid = login(username=username, password=password)
                if is_valid:
                    st.session_state["route"] = Routes.DASHBOARD
                else:
                    st.session_state["error"] = True

            st.button("Login", use_container_width=True, on_click=__login_call)
            if st.session_state.get("error"):
                st.error('Invalid Credentials')
