from .abstraction import AbstractionService
from ..excpetions import WrongQuestion
import pdfplumber
from openai import OpenAI
from project.config.development import Development
import os

class Default(AbstractionService):
    def __init__(self, data_access):
        self.data_access = data_access
        self.client = OpenAI(api_key=Development.API_KEY)

    def Create_Qa(self, question, answer):
        qa = self.data_access.Create_Qa(question, answer)
        if not qa:
            raise WrongQuestion(question=question)
        return qa

    def extract_text_from_pdf(self, pdf_path):
     text = ""
     try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        print("Extracted PDF Text:", text)  # Print to check content
     except FileNotFoundError:
        return "Error: PDF file not found."
     except Exception as e:
        return f"Error: {str(e)}"
     return text
 

    def load_text_data(self, directory_path):
     texts = []
     for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    texts.append(f.read())
     print("Loaded Text Data:", texts)  # Print to check content
     if not texts:
        return ["No text data available."]
     return texts


    def query_openai(self, prompt, texts):
     context = "\n\n".join(texts)
     full_prompt = (f"Context:\n{context}\n\n"
                   f"Based on the above context from the PDF, answer the following question. "
                   f"Do not provide any information that is not present in the context.\n\n"
                   f"User Question:\n{prompt}")

     print("Full Prompt:", full_prompt)  # Print to check prompt
     try:
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": full_prompt}
            ]
        )
        return response.choices[0].message.content.strip()
     except Exception as e:
        return f"Error: {str(e)}"


    def chatbot(self, question):
        pdf_path = r"C:/Python/chatbot/docs/Noor-Book.com  250 تقنية في التلاعب النفسي.pdf"
        pdf_text = self.extract_text_from_pdf(pdf_path)
        texts = self.load_text_data("docs")
        texts.append(pdf_text)
        response = self.query_openai(question, texts)
        return response
