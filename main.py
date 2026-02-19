import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 1️⃣ Bad Prompt
bad_prompt = "Summarize this text: AI is transforming industries."

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": bad_prompt}],
    temperature=0.9
)

print("Bad Prompt Output:")
print(response.choices[0].message.content)

# 2️⃣ Improved Prompt
good_prompt = """
Summarize the following text in 2 concise bullet points:

AI is transforming industries by automating processes,
enhancing decision-making, and enabling predictive analytics.
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": good_prompt}],
    temperature=0.3
)

print("\nImproved Prompt Output:")
print(response.choices[0].message.content)

# 3️⃣ Structured Output Prompt
structured_prompt = """
Extract name, skills, and experience from the text below.
Return output in valid JSON format only.

Text:
John Doe is a Python developer with 3 years of experience
in machine learning and backend development.
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": structured_prompt}],
    temperature=0
)

print("\nStructured Output:")
print(response.choices[0].message.content)
