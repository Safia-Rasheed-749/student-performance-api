import streamlit as st


def section_header(title: str, subtitle: str | None = None):
    """Consistent section styling."""
    st.markdown(
        f"""
        <div style="padding: 14px 16px; border-radius: 14px; background: rgba(49, 112, 255, 0.08); border: 1px solid rgba(49, 112, 255, 0.20);">
            <div style="font-size: 18px; font-weight: 800; color: #0B3D91;">{title}</div>
            {f'<div style="margin-top:6px; color: rgba(11,61,145,0.85);">{subtitle}</div>' if subtitle else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )


def pill(label: str, value: str):
    st.markdown(
        f"""
        <span style="display:inline-flex; align-items:center; padding:6px 10px; border-radius:999px; background: rgba(0,0,0,0.04); border: 1px solid rgba(0,0,0,0.06); font-weight:700;">
            <span style="color: rgba(0,0,0,0.55); font-weight:800; margin-right:8px;">{label}</span>
            <span style="color:#111;">{value}</span>
        </span>
        """,
        unsafe_allow_html=True,
    )


def set_global_style():
    # Avoid calling markdown repeatedly in environments that may trigger reruns
    # during startup; keep this as a single, cached operation.
    if st.session_state.get("_global_style_applied"):
        return

    st.markdown(
        """
        <style>
            /* App background */
            .stApp { background: linear-gradient(135deg, rgba(49,112,255,0.06), rgba(0,0,0,0) 55%), #FFFFFF; }

            /* Sidebar */
            section[data-testid="stSidebar"] { background: #4d8cf7; color: black; }
            section[data-testid="stSidebar"] * { color: black; }

            /* Buttons */
            div.stButton > button {
                border-radius: 12px;
                font-weight: 800;
                padding: 8px 14px;
            }

            /* Primary buttons */
            div.stButton > button[kind="primary"], div.stButton > button[data-testid="baseButton-primary"] {
                background-color: #0B3D91 !important;
                border-color: #0B3D91 !important;
            }

            div.stButton > button[kind="primary"]:hover,
            div.stButton > button[data-testid="baseButton-primary"]:hover {
                background-color: #083066 !important;
                border-color: #083066 !important;
            }

            /* Inputs */
            div[data-baseweb="input"] > div { border-radius: 12px; }

            /* Success banner */
            div[data-testid="stSuccess"] { border-radius: 14px; border: 1px solid rgba(34,197,94,0.25); }

            /* Error banner */
            div[data-testid="stError"] { border-radius: 14px; border: 1px solid rgba(239,68,68,0.25); }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.session_state["_global_style_applied"] = True


