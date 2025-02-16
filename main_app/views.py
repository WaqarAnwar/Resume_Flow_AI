from django.shortcuts import render
from openai import OpenAI
import PyPDF2
from dotenv import load_dotenv
import os
from main_app.utils import get_text_from_pdfs

load_dotenv()

client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://openrouter.ai/api/v1")

def home(request):
    return render(request, 'home.html')

def process_uploaded_files(request):
    if (request.method == 'POST'):
        pdf_files = request.FILES.getlist('pdf_files')
        job_description = request.POST.get('job_description')

        #below we get the text from the resumes submitted by the user
        resumes_info = get_text_from_pdfs(pdf_files)

        #below is the prompt given to Deepseek API to get the ranking of resumes based on job description
        user_content = f"""
        Hello, I have resumes of candidates and a job description. 
        The resumes will be given in the form of text at the end of this message.
        Each resume will be separated by 5 new lines (\n\n\n\n\n).
        Just match each resume with the job description and rank them 
        (best matching to worst matching) based on their relevance to the job description.
        Provide a short explanation of each ranking.
        Exclude thinking process from the response.
        Please provide the response in HTML format.

        Here is the job description:
        {job_description}

        and here are the resumes:
        {resumes_info}
        """

        response = client.chat.completions.create(
            model="deepseek/deepseek-chat:free",
            messages=[
                {"role": "system", "content": "You are a helpful assistant which extracts information from text."},
                {"role": "user", "content": user_content},
            ],
            stream=False
        )
        
        response =  response.choices[0].message.content

        response = response.replace("```html","").replace("```","")

        return render(request, 'result.html', {'response': response})

    else:
        return render(request, 'home.html')