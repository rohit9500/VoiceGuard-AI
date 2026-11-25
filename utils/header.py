import streamlit as st


def header():

    col1, col2 = st.columns([1, 7])

    with col1:

        st.image(
            "assets/logo.png",
            width=75
        )

    with col2:

        st.markdown("""
<h1 style="
margin-bottom:0px;
font-size:35px;
font-weight:300;
color:white;">

VoiceGuard AI

</h1>
""", unsafe_allow_html=True)

    st.divider()