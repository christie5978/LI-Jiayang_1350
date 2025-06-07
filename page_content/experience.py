import streamlit as st

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Intern
    **Burson, Financial Communication** | *April 2024 - July 2024*
    
    - Analyse 100+ industry news and companies updates on a daily basis
    - Produced daily monitoring reports to provide key insights for media strategy and investors; 
    - Assisted in the execution of media events in industry exhibitions and conferences
    """)
    
    st.markdown("""
    ### Journalist
    **Beijing Dagongwang Technology Co., Ltd., News Department** | *June 2023 - August 2023*
    
    - Planned and produced a promotional video for the Hong Kong Space of the Palace Museum
    - Planned and filmed a number of short news videos on the cultural exchange activities
    - Operated 3 accounts for updating news on different social media platforms
    """)
    
    st.markdown("""
    ### Journalist
    **Ningxia Radio and Television Station, News Department** | *June 2022 - August 2022*
    
    - Executed the theme reports on local news covering ESG, economy and technology
    - Produced a number of short news videos on the local events
    - Editing and post-producted news videos for local news channels
    """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Overseas Media Strategy Campaign for Maoyan",
            "description": "Developed media strategies based on oversea media trends for published Chinese movies.",
            "skills": ["Python", "Web  Scraping", "Data Visualization"],
            "outcome": "Reports were forwarded by 10 media platforms in 5 regions."
        },
        {
            "title": "Promtional Video for 120-year Anniversary of the Palace Museum",
            "description": "Produced the promtional video for 120-year Anniversary of the Palace Museum.",
            "skills": ["Photo Shop", "After Effects", "Premiere Pro"],
            "outcome": "Released on the Palace Museum official website, effectively reaching over 10,000 people."
        },
        {
            "title": "Theme Report on Technology Innovations of the Industrial Park",
            "description": "Reported on scientific and technological innovations in Hedong Industrial Park.",
            "skills": ["Photo Shop", "After Effects", "Premiere Pro"],
            "outcome": "Enhanced the comprehensive score of the park's high-quality development."
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL
        - **Data Processing:** Pandas, NumPy, PySpark
        - **Visualization:** Matplotlib, Seaborn, Plotly
        - **Video Production:** Photo Shop, After Effects, Premiere Pro
        - **Cloud Platforms:** Google Cloud
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in Agile environments
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner who thrives in dynamic environments
        """)
    
    st.markdown("---") 