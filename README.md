# ResumeFlow - AI-Powered Resume Screening for HR Efficiency

ResumeFlow is an intelligent recruitment solution that leverages DeepSeek's NLP capabilities and Django to automate resume screening. It analyzes resumes against job descriptions and provides ranked candidate lists, enabling HR teams to prioritize top applicants efficiently.

[Demo Preview](https://www.linkedin.com/posts/mwaqaranwar123_hrtech-hrsoftware-recruitment-activity-7296840695271571456-Qc7L/)  
*Video demonstration available on LinkedIn*

## Key Features

- **Batch PDF Processing**: Analyze multiple resumes simultaneously (PDF format only)
- **Smart Job Description Parsing**: Automatically extracts key requirements and qualifications
- **AI Ranking Engine**: Scores candidates using:
  - Skills relevance (e.g. NLP expertise for data science roles)
  - Experience alignment
  - Qualification matching
- **Explainable Rankings**: Provides clear rationale for candidate prioritization

## Technical Requirements

- Python 3.8+
- DeepSeek V3 API access (Free tier available via [OpenRouter](https://openrouter.ai/))
- PDF file format for resumes

## Setup

1. Clone repository
2. Make a virtual environment and activate it.
3. Inside the directory of the project, run:
```bash
pip install -r requirements.txt
```
4. Get an API key of Deepseek-V3 free version from [OpenRouter](https://openrouter.ai/) and put it in a .env file in project root directory (open .env.example file for seeing variable naming)
5. Then run: 
```bash
python manage.py runserver
```
6. Then go to localhost:8000 on your browser to use the AI App. 


