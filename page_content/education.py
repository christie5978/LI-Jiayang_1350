import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown("""
    ### Master of Science in Marketing
    **The Chinese University of Hong Kong** | *September 2024 - June 2025*
    
    - GPA: 3.4/4.0
    - Relevant Coursework: Machine Learning in Marketing, Digital Marketing, Data Visualization, Big Data Strategy, Marketing Research
    
    ### Bachelor of Social Science in Journalism and Communication
    **The Chinese University of Hong Kong** | *September 2020 - June 2024*
    
    - GPA: 3.2/4.0
    - Relevant Coursework: Media Writing, Advertising and Society, Creative Media Curation and Management, Fundamentals in Visual Media, Law and Ethics for Communication
    """)
    
    st.markdown("---")
 
    st.markdown("## Scholarships")
    
    scholarship1, scholarship2 = st.columns(2)
    
    with scholarship1:
        st.markdown("""
        ### Clarks Social Science Budding Scholar Award
        **School of Journalism and Communication, CUHK** | *2021-2022*
        
        Awarded to top students for outstanding academic papers.
        """)
        
    with scholarship2:
        st.markdown("""
        ### Scholarships for General Education,
        **S.H. Ho College** | *2020-2021*
        
        Recognized for academic excellence and contributions in General Education.
        """)
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    ### Sentiment Analysis of Product Reviews
    - Developed a deep learning model to analyze customer reviews and predict sentiment
    - Collected 300+ product comments from social media platforms
    - Generated a comprehensive report on the findings and insights
    
    ### Descriptive Analysis of JD Customers' Behaviors
    - Conducted a comprehensive analysis of JD customers' behaviors
    - Generated a report on the findings and insights 
    - Utilized statistical techniques and data visualization to present findings
    """)
    
    st.markdown("---") 