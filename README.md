# ResumeFlow

Tired of filtering Resumes of candidates? Introducing ResumeFlow!

ResumeFlow is an AI App built using DeepSeek API and Django that makes it easier for HR to screen candidates 
by automating resume ranking based on job description relevancy.

## Core Functionality:

1. Batch Resume Processing: Accepts a batch of resumes (only PDF) in a single workflow.
2. Job Description Analysis: Parses key requirements, skills, and qualifications from the provided job description.
3. AI-Driven Ranking: Leverages DeepSeek’s NLP capabilities to rank resumes based on job description relevance, technical skills, experience alignment, and keyword matching.
4. Ranked Output: Delivers an ordered list of candidates, prioritized by fit for the role.

## Demo Link:
https://www.linkedin.com/feed/update/urn:li:activity:7296840695271571456/

## Limitations:

1. It may take 1 to 2 minutes to respond, depends upon the number of resumes being input.

## Setup

1. Download the source code
2. Make a virtual environment and activate it.
3. Inside the directory of the project, run:

```bash
pip install -r requirements.txt
```

4. Get an API key of Deepseek-V3 free version from OpenRouter and put it in a .env file in project root directory.

5. Then run: 

```bash
python manage.py runserver
```

6. Then go to localhost:8000 on your browser to use the AI App. 


