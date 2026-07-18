# Multi-Agent-LLM-Workflow-using-Python-Cloud-Hosting
🚀 AI-Powered Study Assistant
[https://ai-learning-workflow-uxh6.onrender.com](url)

An intelligent, multi-persona AI Study Assistant built to provide adaptive learning support. Whether you need a friendly, simplified explanation or a rigorous, academic breakdown, this assistant tailors its responses to your specific needs.

🛠️ Features
Persona-Based Learning: Switch between "Friendly" (everyday analogies) and "Academic" (formal, technical definitions) modes.

Interactive UI: Built with Gradio for a clean, user-friendly interface.

Powered by Gemini: Uses the latest Google Gemini API for high-quality, context-aware responses.

Cloud-Ready: Deployed and permanently hosted on Render.

💻 Tech Stack
Language: Python 3.12

AI Engine: Google Gemini API (gemini-3.5-flash)

Frontend: Gradio

Hosting: Render (Web Service)

🚀 How to Run Locally
Clone the repository:

Bash
git clone https://github.com/YourUsername/YourRepoName.git
cd YourRepoName
Install dependencies:

Bash
pip install -r requirements.txt
Set your API Key:

Bash
export GEMINI_API_KEY='your_api_key_here'
Run the application:

Bash
python app.py
🌐 Deployment
This project is configured for seamless deployment on platforms like Render. It uses environment variables for secure API key management and standard port binding for cloud compatibility.

💡 Technical TakeawaysAPI Integration: Successfully integrated the Google GenAI SDK for secure, environment-variable-based authentication.  Cloud Deployment: Overcame containerization challenges by correctly binding network ports (0.0.0.0) for live cloud hosting.  User-Centric Design: Implemented personality-driven prompting to tailor AI outputs for different user needs.  

📝 Credits
Built by P.S.Surya Teja. Feel free to contribute or reach out if you have suggestions for improvement!
![Study Assistant UI](app-screenshot.png)
