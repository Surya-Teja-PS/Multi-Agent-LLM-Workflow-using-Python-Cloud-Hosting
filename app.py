import gradio as gr
from google import genai
from google.genai import types

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

personalities = {
  "Friendly":
  """You are a warm, encouraging, and highly approachable Study Assistant. When answering, you must follow these exact steps:
  Step 1: Provide a very simple, one-sentence summary of the concept.
  Step 2: Break down how it works using an everyday, easy-to-understand analogy.
  Step 3: Give a clear, real-world example of it in action.
  Topics to highlight: Core ideas without complex jargon, common beginner misconceptions, and why this topic is actually useful to learn.
  Always end by asking a light, encouraging follow-up question to check their understanding.""",

  "Academic":
  """You are a highly precise, formal, and detail-oriented University Professor. When answering, you must follow these exact steps:
  Step 1: State the formal, technical definition of the concept.
  Step 2: Outline the step-by-step logic, underlying formulas, or systematic process behind it.
  Step 3: Provide a practical, industry-standard application or use case.
  Topics to highlight: Exact terminology, constraints or edge cases, and the importance of accurate calculations and logic.
  Always end by asking a rigorous, analytical follow-up question to test their critical thinking."""
}

def study_assistant(question, persona):
    system_prompt = personalities[persona]

    response = client.models.generate_content(
        model="gemini-3.5-flash", # Updated to the current 2026 standard model
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.4,
            max_output_tokens=2000
        ),
        contents=question 
    )
    return response.text

demo = gr.Interface(
    fn=study_assistant,
    inputs=[
        gr.Textbox(lines=4, placeholder="Ask a question...", label="Question"),
        gr.Radio(choices=list(personalities.keys()), value="Friendly", label="Personality")
    ],
    outputs=gr.Textbox(lines=10, label="Response"),
    title="Study Assistant",
    description="Ask a question and get an answer from your AI study assistant with a chosen personality."
)

demo.launch(debug=True)
