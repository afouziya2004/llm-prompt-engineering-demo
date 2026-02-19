reasoning_prompt = """
A store had 120 apples. It sold 35 in the morning
and 40 in the afternoon. How many apples remain?
Explain your reasoning step by step.
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": reasoning_prompt}],
    temperature=0
)

print("\nReasoning Output:")
print(response.choices[0].message.content)
