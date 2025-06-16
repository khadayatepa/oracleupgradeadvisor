import streamlit as st

st.title("Oracle Upgrade Advisor")

option = st.selectbox(
    "Choose an option:",
    ("--Please select--", "Upgrade Implementation Plan", "Migration Plan")
)

UPGRADE_STEPS = [
    "Analyze the current Oracle Database version and environment.",
    "Review Oracle's official documentation for the target upgrade version.",
    "Check hardware, OS, and software prerequisites.",
    "Take a full database backup.",
    "Install the new Oracle software (in a new Oracle home).",
    "Run pre-upgrade checks using Oracle's pre-upgrade tool.",
    "Resolve any issues found in the pre-upgrade checks.",
    "Perform a test upgrade on a non-production environment.",
    "Schedule downtime for production upgrade.",
    "Shut down applications and database.",
    "Perform the upgrade using Database Upgrade Assistant (DBUA) or command-line tools.",
    "Run post-upgrade scripts and checks.",
    "Test applications and validate data integrity.",
    "Monitor performance and address any post-upgrade issues."
]

MIGRATION_STEPS = [
    "Assess source and target environments (Oracle versions, OS, hardware).",
    "Choose the migration method (Data Pump, RMAN, GoldenGate, etc.).",
    "Plan for downtime and communicate with stakeholders.",
    "Take a full backup of the source database.",
    "Set up the target environment (install Oracle, configure OS, storage, etc.).",
    "If required, create tablespaces and users in the target database.",
    "Export data from the source database (using chosen tool).",
    "Transfer export files to the target environment.",
    "Import data into the target database.",
    "Run post-migration scripts (recompile objects, update stats, etc.).",
    "Perform data validation and application testing.",
    "Switch over production traffic to the new environment.",
    "Monitor system for issues post-migration."
]

if st.button("Submit"):
    if option == "Upgrade Implementation Plan":
        st.subheader("Implementation Steps: Upgrade")
        for i, step in enumerate(UPGRADE_STEPS, 1):
            st.markdown(f"{i}. {step}")
    elif option == "Migration Plan":
        st.subheader("Implementation Steps: Migration")
        for i, step in enumerate(MIGRATION_STEPS, 1):
            st.markdown(f"{i}. {step}")
    else:
        st.warning("Please select an option before submitting.")
