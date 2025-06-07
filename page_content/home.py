import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>LI Jiayang</h4>
        <p>Recent Master's Graduate in Marketing<br>
        The Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:christinali_1010@163.com">christinali_1010@163.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image.png")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a marketing and communications professional with PR, media, and data analytics experience, fluent in English and Cantonese. Currently pursuing an MSc in Marketing at CUHK, I combine strategic thinking with creative execution. 

        At Burson Hong Kong, I analyzed 100+ daily financial news reports and assisted in media events with 2,800+ attendees. 
        
        As a journalist at Takungpao, I produced viral videos reaching 10,000+ viewers and directed a top-performing documentary. My data skills include Python, R, and Excel, while my multimedia expertise covers Photoshop and Premiere Pro. 

        As a student leader, I organized orientation camps and mentored scholarship-winning teams, demonstrating strong organizational abilities.
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Data Analysis: Pandas, Matplotlib
        - Statistical Analysis: Hypothesis Testing, Regression Analysis
        - Multimedia: Photoshop, Premiere Pro, Canvas, After Effects
        - Communication: Presentation Skills, Technical Writing
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page