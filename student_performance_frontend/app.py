import streamlit as st
from ui_components import section_header, set_global_style



st.set_page_config(page_title="Student Performance Predictor", page_icon="📚", layout="wide")
set_global_style()
if 'page' not in st.session_state:
    st.session_state.page = "Study Habits"

def navigate_to(page):
    st.session_state.page = page
    st.rerun()

st.sidebar.title("📋 Navigation")
st.sidebar.markdown("<div style='color: rgba(255,255,255,0.9); font-weight:700; margin-top:6px;'>Build a quick student profile, then predict.</div>", unsafe_allow_html=True)

page_options = ["Study Habits", "Subject Scores", "Background & Method", "Predict"]
selected_page = st.sidebar.radio(
    "Go to section",
    page_options,
    index=page_options.index(st.session_state.page) if st.session_state.page in page_options else 0,
    key="sidebar_page_radio",
)


if selected_page != st.session_state.page:
    st.session_state.page = selected_page
    st.rerun()

if st.session_state.page == "Study Habits":
    section_header("📖 Study Habits", "How much time the student studies")

    left, right = st.columns([2, 1])
    with left:
        st.session_state.study_hours = st.number_input(
            "Weekly Study Hours (0–8.0)",
            min_value=0.0,
            max_value=8.0,
            value=st.session_state.get('study_hours', 8.0),
            step=0.1, 
            key="study_hours_input",
        )


    with right:
        st.markdown(
            """
            <div style="padding:14px; border-radius:16px; background:rgba(49,112,255,0.08); border:1px solid rgba(49,112,255,0.18);">
              <div style="font-weight:900; color:#0B3D91;">Tip</div>
              <div style="margin-top:6px; color:rgba(11,61,145,0.85); font-weight:650;">More consistent study hours usually improve outcomes.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()
    c1, c2 = st.columns([1, 3])
    with c1:
        if st.button(
            "Next →",
            type="primary",
            use_container_width=True,
            key="study_next"
        ):
            navigate_to("Subject Scores")

elif st.session_state.page == "Subject Scores":
    section_header("📊 Subject Scores", "Enter scores for core subjects")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.session_state.math_score = st.number_input(
            "Math Score (0–100)",
            min_value=0.0,
            max_value=100.0,
            value=st.session_state.get('math_score', 85.0),
            step=0.1,
            key="math_score_input",
        )

    with col2:
        st.session_state.science_score = st.number_input(
            "Science Score (0–100)",
            min_value=0.0,
            max_value=100.0,
            value=st.session_state.get('science_score', 82.0),
            step=0.1,
            key="science_score_input",
        )

    with col3:
        st.session_state.english_score = st.number_input(
            "English Score (0–100)",
            min_value=0.0,
            max_value=100.0,
            value=st.session_state.get('english_score', 88.0),
            step=0.1, 
            key="english_score_input",
        )


    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button(
            "← Back",
            use_container_width=True,
            key="subject_back"
        ):
            navigate_to("Study Habits")
    with col2:
        if st.button(
            "Next →",
            type="primary",
            use_container_width=True,
            key="subject_next"
        ):
            navigate_to("Background & Method")

elif st.session_state.page == "Background & Method":
    section_header("👤 Background & Study Method", "Context + learning approach")

    parent_options = ["diploma", "post graduate", "graduate", "no formal", "phd", "high school"]
    travel_options = ["<15 min", "15-30 min", "30-60 min", ">60 min"]
    method_options = ["online videos", "textbook", "coaching", "notes", "mixed", "group study"]

    st.session_state.parent_education = st.selectbox(
        "Parent Education",
        parent_options,
        index=parent_options.index(st.session_state.get('parent_education', 'graduate'))
        if st.session_state.get('parent_education', 'graduate') in parent_options
        else parent_options.index('graduate'),
        key="parent_education_select",
    )


    st.session_state.travel_time = st.selectbox(
        "Travel Time",
        travel_options,
        index=travel_options.index(st.session_state.get('travel_time', '<15 min'))
        if st.session_state.get('travel_time', '<15 min') in travel_options
        else 0,
        key="travel_time_select",
    )


    st.session_state.study_method = st.selectbox(
        "Study Method",
        method_options,
        index=method_options.index(st.session_state.get('study_method', 'online videos'))
        if st.session_state.get('study_method', 'online videos') in method_options
        else 0,
        key="study_method_select",
    )


    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button(
            "← Back",
            use_container_width=True,
            key="background_back"
        ):
            navigate_to("Subject Scores")
    with col2:
        if st.button(
            "Next →",
            type="primary",
            use_container_width=True,
            key="background_next"
        ):
            navigate_to("Predict")

elif st.session_state.page == "Predict":
    section_header("🎯 Predict Overall Score", "Model prediction from your entered profile")

    # Top-level import (works when Streamlit root is `student_performance_frontend/`)
    from utils import call_prediction_api

    with st.container():
        st.markdown(
            """
            <div style="padding:14px; border-radius:16px; background:rgba(0,0,0,0.02); border:1px solid rgba(0,0,0,0.06);">
                <div style="font-weight:950; color:#111827;">Student profile</div>
                <div style="margin-top:8px; color:rgba(17,24,39,0.8); font-weight:700; line-height:1.8;">
                    <div>📚 Study hours: <span style="color:#0B3D91;">{study_hours}</span></div>
                    <div>🧠 Math/Science/English: <span style="color:#0B3D91;">{math_score} / {science_score} / {english_score}</span></div>
                    <div>👪 Parent education: <span style="color:#0B3D91;">{parent_education}</span></div>
                    <div>🚗 Travel time: <span style="color:#0B3D91;">{travel_time}</span></div>
                    <div>📘 Study method: <span style="color:#0B3D91;">{study_method}</span></div>
                </div>
            </div>
            """.format(
                study_hours=st.session_state.get('study_hours', 20.0),
                math_score=st.session_state.get('math_score', 85.0),
                science_score=st.session_state.get('science_score', 82.0),
                english_score=st.session_state.get('english_score', 88.0),
                parent_education=st.session_state.get('parent_education', 'graduate'),
                travel_time=st.session_state.get('travel_time', '<15 min'),
                study_method=st.session_state.get('study_method', 'online videos'),
            ),
            unsafe_allow_html=True,
        )

    st.divider()

    if st.button("🔮 Predict", type="primary", use_container_width=True, key="predict_btn"):
        data = {
            "study_hours": st.session_state.get('study_hours', 20.0),
            "math_score": st.session_state.get('math_score', 85.0),
            "science_score": st.session_state.get('science_score', 82.0),
            "english_score": st.session_state.get('english_score', 88.0),
            "parent_education": st.session_state.get('parent_education', 'graduate'),
            "travel_time": st.session_state.get('travel_time', '<15 min'),
            "study_method": st.session_state.get('study_method', 'online videos'),
        }

        result = call_prediction_api(data)
        if result:
            score = float(result['predicted_score'])
            st.markdown(
                """
                <div style="padding:18px; border-radius:18px; background:rgba(34,197,94,0.10); border:1px solid rgba(34,197,94,0.25);">
                    <div style="font-weight:1000; color:#065F46; font-size:16px;">Predicted Overall Score</div>
                    <div style="margin-top:8px; font-weight:1000; color:#064E3B; font-size:40px;">{score:.2f}</div>
                    <div style="margin-top:-4px; font-weight:800; color:rgba(6,78,59,0.85);">out of 100</div>
                </div>
                """.format(score=score),
                unsafe_allow_html=True,
            )

            if result.get('confidence_score') is not None:
                conf = float(result['confidence_score'])
                if conf >= 85:
                    st.success(f"📈 Confidence Score: {conf:.2f}% - High Confidence 🟢")
                elif conf >= 75:
                    st.warning(f"📈 Confidence Score: {conf:.2f}% - Medium Confidence 🟡")
                else:
                    st.error(f"📈 Confidence Score: {conf:.2f}% - Low Confidence 🔴")

            if st.button("🔄 Start Over", use_container_width=True,key="restart_btn"):
                st.session_state.clear()
                st.rerun()

else:
    # Safe fallback without triggering another rerun (prevents navigation break on Streamlit Cloud)
    st.session_state.page = "Study Habits"
    section_header("📖 Study Habits", "How much time the student studies")
    left, right = st.columns([2, 1])
    with left:
        st.session_state.study_hours = st.number_input(
            "Weekly Study Hours (0–8.0)",
            min_value=0.0,
            max_value=40.0,
            value=st.session_state.get('study_hours', 20.0),
            step=0.1, 
        )

