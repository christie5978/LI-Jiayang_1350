import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="LI Jiayang_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("LI Jiayang")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** christinali_1010@163.com
    - **Phone:** +852 5442 1628
    - **LinkedIn**: [linkedin.com/in/jiayang-li](https://www.linkedin.com/in/jiayang-li-7b94852b0/?trk=contact-info)
    - **GitHub**: [github.com/christie5978](https://github.com/christie5978)
    - **Address:** Flat H on 15th of Block 3, Phase 1 of Double Cove, no. 8 Wu Kai Sha Road, Ma On Shan, ShaTin N. T., Hong Kong 999077
    """)

    st.header("Professional Summary")
    st.markdown("""
    I am a marketing and communications professional with PR, media, and data analytics experience, fluent in English and Cantonese. 
    """)

    st.header("Work Experience")
    st.markdown("""
    **Intern, Burson**
    - *April 2024 - July 2024*
    - Analyse 100+ industry news and companies updates on a daily basis
    - Produced daily monitoring reports to provide key insights for media strategy and investors
    - Assisted in the execution of media events in industry exhibitions and conferences

    **Journalist, Beijing Dagongwang Technology Co., Ltd.**
    - *June 2023 - August 2023*
    - Planned and produced a promotional video for the Hong Kong Space of the Palace Museum
    - Produced and filmed a number of short news videos on the cultural exchange activities
    - Operated 3 accounts for updating news on different social media platforms

    **Journalist, Ningxia Radio and Television Station**
    - *June 2022 - August 2022*
    - Executed the theme reports on local news covering ESG, economy and technology
    - Produced a number of short news videos on the local events
    - Editing and post-producted news videos for local news channels
    """)

    st.header("Education")
    st.markdown("""
    **Master of Science in Marketing**
    - The Chinese University of Hong Kong
    - *Graduated: June 2025*
    - GPA: 3.4/4.0

    **Bachelor of Social Science in Journalism and Communication**
    - The Chinese University of Hong Kong
    - *Graduated: June 2024*
    - GPA: 3.2/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, R, SQL
    - **Data Processing:** Pandas, NumPy, PySpark
    - **Visualization:** Matplotlib, Seaborn, Plotly
    - **Video Production:** Photo Shop, After Effects, Premiere Pro
    - **Cloud Platforms:** Google Cloud
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)

    st.header("Projects")
    st.markdown("""
    **Sentiment Analysis of Product Reviews**
    - Developed a deep learning model to analyze customer reviews and predict sentiment
    - Collected 300+ product comments from social media platforms
    - Generated a comprehensive report on the findings and insights
    
    **Descriptive Analysis of JD Customers' Behaviors**
    - Conducted a comprehensive analysis of JD customers' behaviors
    - Generated a report on the findings and insights
    - Utilized statistical techniques and data visualization to present findings

    **Oversea Media Strategy Campaign**
    - Developed media strategies based on foreign media trends for published Chinese movies
    - Reports were forwarded by 10 media platforms in 5 regions

    **Promtional Video for 120-year Anniversary of the Palace Museum**
    - Produced the promtional video for 120-year Anniversary of the Palace Museum
    - Released on the Palace Museum official website, effectively reaching over 10,000 people
    """)

    st.header("Languages")
    st.markdown("""
    - **English:** Fluent
    - **Mandarin:** Native
    - **Cantonese:** Professional Working Proficiency
    """)

    st.header("Interests")
    st.markdown("""
    - Vidoeo editing
    - Blogging about fashion and lifestyle trends
    - Hiking and outdoor activities
    """)

    st.markdown("---") 