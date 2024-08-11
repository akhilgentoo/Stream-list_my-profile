from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "akhilkumar2024_Resume.pdf"
profile_pic = current_dir / "assets" / "akhil.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Akhilkumar"
PAGE_ICON = ":random:"
NAME = "Akhilkumar"
DESCRIPTION = """
Senior System Analyst, assisting enterprises by supporting Devops and Infrastructure-driven decision-making.
"""
EMAIL = "akeelkumar9068@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/akeelkumar",
    "GitHub": "https://github.com/akhilgentoo",
}
PROJECTS = {
    "🏆 Best Employee Reward - Recognized for outstanding performance and contributions to the team",
    "🏆 Automation Award -  Acknowledged for driving automation initiatives within the organization",
    "🏆 Spot Award  - Received for exceptional teamwork and problem-solving skills",
    "🏆 Automation Excellence Award  - Led the team's transition to automated and cloud-based solutions"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# # --- SOCIAL LINKS ---
# st.write('\n')
# cols = st.columns(len(SOCIAL_MEDIA))
# for index, (platform) in enumerate(SOCIAL_MEDIA.items()):
#     cols[index].write(f"[{platform}]")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 5 Years expereince Devops and Infrastructure Engineer
- ✔️ Strong hands on experience and knowledge in OCP,Bamboo,Docker,Kubernetes,Linux,Splunk,EKS,Ansible
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (django,Streamlit),Bash,SQL
- 📊 Data Visulization: PowerBi, MS Excel
- 🗄️ Databases: Oracle, MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior System Analyst | Carelon Global Solution**")
st.write("02/2020 - Present")
st.write(
    """
- ► Developed Multiple pipelines for cloud deployment
- ► Improve the performances of JVM’s and clusters
- ► Written 50+ Ansible playbook for automation strategy
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**System Analyst  | Legato Health**")
st.write("06/2019 - 07/2022")
st.write(
    """
- ► Built Multiple Dashboards for monitoring for multiple Apps to avoid outages
- ► Certificate generation and renewal external and internal
- ► Prompt Alert setups and Webhook to MS Team for Monitoring
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Assc Software Engineer | UST**")
st.write("01/2018 - 01/2019")
st.write(
    """
- ► Devised Data load Batch automation
- ► Prompt Alert setups and Webhook to MS Team for Monitoring
- ► API Monitoring of external services and coordination activities 
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
"🏆 Best Employee Reward - Recognized for outstanding performance and contributions to the team",
"🏆 Automation Award -  Acknowledged for driving automation initiatives within the organization",
"🏆 Spot Award  - Received for exceptional teamwork and problem-solving skills",
"🏆 Automation Excellence Award  - Led the team's transition to automated and cloud-based solutions"