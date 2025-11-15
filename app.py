"""Top-level Streamlit entrypoint.

Use `streamlit run app.py` or set this file as the app file in Streamlit Cloud.
"""

from lifting_plan_automation.gui import streamlit_app


if __name__ == "__main__":
    streamlit_app()
