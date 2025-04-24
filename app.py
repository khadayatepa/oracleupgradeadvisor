import streamlit as st
import openai

st.set_page_config(page_title="Oracle DB Upgrade Advisor", layout="centered")

st.title("Oracle Database Upgrade & Migration Advisor")

# OpenAI API key input
openai_api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Source DB version
source_db_version = st.selectbox(
    "Select Source Database Version",
    ["11g", "12cR1", "12cR2", "18c", "19c", "21c"]
)

# Target DB version
target_db_version = st.selectbox(
    "Select Target Database Version",
    ["19c", "23ai"]
)

# Source OS version
source_os_version = st.selectbox(
    "Select Source Operating System and Version",
    [
        "RHEL 6", "RHEL 7", "RHEL 8", "AIX 7.1", "AIX 7.2",
        "Windows Server 2012", "Windows Server 2016", "Solaris 11"
    ]
)

# Target OS version
target_os_version = st.selectbox(
    "Select Target Operating System and Version",
    [
        "RHEL 7", "RHEL 8", "RHEL 9", "AIX 7.2",
        "Windows Server 2016", "Windows Server 2019", "Solaris 11"
    ]
)

# DB size
db_size = st.select_slider(
    "Select Database Size",
    options=[f"{i}GB" for i in range(100, 10001, 500)]
)

# Submit
if st.button("Get Upgrade & Migration Option"):
    if not openai_api_key:
        st.error("Please enter your OpenAI API key.")
    else:
        openai.api_key = openai_api_key

        prompt = f"""
        Given the following Oracle database environment details:
        - Source Database Version: {source_db_version}
        - Target Database Version: {target_db_version}
        - Source OS and Version: {source_os_version}
        - Target OS and Version: {target_os_version}
        - Database Size: {db_size}

        Suggest the most suitable upgrade and migration option with either minimal downtime or substantial downtime, including whether to use Data Pump, RMAN, Transportable Tablespaces, GoldenGate, ZDM, or any other recommended tool or method. Justify the recommendation briefly.
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a database upgrade advisor."},
                    {"role": "user", "content": prompt}
                ]
            )

            recommendation = response.choices[0].message.content
            st.subheader("Recommended Option:")
            st.write(recommendation)

        except Exception as e:
            st.error(f"Error calling OpenAI API: {e}")
