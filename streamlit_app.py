import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Oracle DB Upgrade Advisor - By Prashant K", layout="centered")
st.title("Oracle Database Upgrade & Migration Advisor - By Prashant K")

# API key input
openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Selections
source_db_version = st.selectbox("Select Source Database Version", ["11g", "12cR1", "12cR2", "18c", "19c", "21c"])
target_db_version = st.selectbox("Select Target Database Version", ["19c", "23ai"])

source_os_version = st.selectbox(
    "Select Source Operating System and Version",
    ["RHEL 6", "RHEL 7", "RHEL 8", "AIX 7.1", "AIX 7.2", "Windows Server 2012", "Windows Server 2016", "Solaris 11"]
)

target_os_version = st.selectbox(
    "Select Target Operating System and Version",
    ["RHEL 7", "RHEL 8", "RHEL 9", "AIX 7.2", "Windows Server 2016", "Windows Server 2019", "Solaris 11"]
)

db_size = st.select_slider("Select Database Size", options=[f"{i}GB" for i in range(100, 10001, 500)])

recommendation = None

# Submit button for advisor
if st.button("Get Upgrade & Migration Option"):
    if not openai_api_key:
        st.error("Please enter your OpenAI API key.")
    else:
        client = OpenAI(api_key=openai_api_key)

        prompt = f"""
        Given the following Oracle database environment details:
        - Source Database Version: {source_db_version}
        - Target Database Version: {target_db_version}
        - Source OS and Version: {source_os_version}
        - Target OS and Version: {target_os_version}
        - Database Size: {db_size}

        Suggest the most suitable upgrade and migration option with either minimal downtime or substantial downtime. 
        Recommend tools such as Data Pump, RMAN, GoldenGate, ZDM, or others, and justify the choice.
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a database upgrade advisor."},
                    {"role": "user", "content": prompt}
                ]
            )
            recommendation = response.choices[0].message.content
            st.subheader("Recommended Option:")
            st.write(recommendation)

            # Store recommendation in session state so that the next button can access it
            st.session_state['recommendation'] = recommendation
            st.session_state['advisor_prompt'] = prompt

        except Exception as e:
            st.error(f"Error calling OpenAI API: {e}")

# Button for detailed implementation steps
if 'recommendation' in st.session_state and st.button("Show Detailed Implementation Steps"):
    if not openai_api_key:
        st.error("Please enter your OpenAI API key.")
    else:
        try:
            client = OpenAI(api_key=openai_api_key)
            # Use the advisor's recommendation and prompt as context
            detail_prompt = f"""
            Based on this recommendation for Oracle DB upgrade/migration:

            {st.session_state['recommendation']}

            Environment details:
            {st.session_state['advisor_prompt']}

            Please provide a step-by-step detailed implementation plan for the suggested upgrade/migration approach, including all required pre-checks, tool usage, commands, validation steps, and post-migration checks. Make it actionable and sequential.
            """

            detailed_response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a database upgrade advisor who provides actionable stepwise implementation plans."},
                    {"role": "user", "content": detail_prompt}
                ]
            )
            steps = detailed_response.choices[0].message.content
            st.subheader("Detailed Implementation Steps:")
            st.write(steps)
        except Exception as e:
            st.error(f"Error calling OpenAI API for steps: {e}")
