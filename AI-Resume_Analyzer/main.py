import streamlit as st 
import PyPDF2
import io
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client=OpenAI()

st.set_page_config(page_title="AI-Resume Critiquer", page_icon="📃", layout="centered")
st.title("AI- Resume Critiquer")
st.markdown("Upload Your resume and get Ai-powered feedback tailored to your needs!")

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

uploaded_file=st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf","txt"])
job_role=st.text_input("Enter the job role that you are targeting (optional)")

analyze=st.button("Analyze Resume")

def extract_text_from_pdf(uploaded_file):
    pdf_reader=PyPDF2.pdf(uploaded_file)
    text=""
    for page in pdf_reader.pages:
        text+=page.extract_text() + '\n'
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type=="application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")  

    if analyze and uploaded_file:
        try:
            file_content=extract_text_from_file(uploaded_file)
                
            if not file_content.strip():
                    st.error("File does not have any content...")
                    st.stop()
                    
                    
            prompt=f"""Please analyze this resume and provide constructive feedback.
            Focus on the following aspects:
            1. Content clarity and impact 
            2. Skill presentation
            3. Experience Description
            4. Specific improvements for {job_role if job_role else 'general job applications'}
            
            resume content:
            {file_content}
            
            please provide your analysis in a clear, structured format with a specific recommendations.
            """
            client=OPENAI(api_key=OPENAI_API_KEY)
            response=client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "you are an expert resume reviewer with years of experience in HR and recruitment"},
                {"role": "user", "content": prompt}
                
            ],
            
            temperature=0.7,
             max_tokens=1000
            )
    
            st.markdown("### Analysis Results")
            st.markdown(response.choices[0].message.content)
        
        except Exception as e:
            st.error(f"an error occurred: {str(e)}")
        