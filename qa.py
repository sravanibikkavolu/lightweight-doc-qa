import streamlit as st
from groq import Groq

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

def answer_question(question, context):

    prompt = f"""
Context:
{context}

Question:
{question}

Answer only using the context above.

If the answer is not present in the context, say:
'I could not find that information in the document.'
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content