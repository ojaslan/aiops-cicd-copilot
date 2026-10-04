import streamlit as st
from agent import analyze_logs


st.set_page_config(
    page_title="AIOps CI/CD Copilot",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 AIOps CI/CD Copilot")

st.write(
    "AI-powered CI/CD failure analysis using "
    "Strands Agents and AWS Bedrock."
)

st.divider()

st.header("🔍 Pipeline Failure Analysis")


logs = st.text_area(
    "Paste GitHub Actions logs",
    height=300,
    placeholder="Paste your failed CI/CD logs here..."
)


if st.button("Analyze Failure", type="primary"):

    if not logs.strip():

        st.warning("Please provide CI/CD logs.")

    else:

        with st.spinner("🤖 AIOps Agent analyzing pipeline..."):

            result = analyze_logs(logs)

        st.subheader("🧠 AIOps Analysis")

        st.markdown(result)