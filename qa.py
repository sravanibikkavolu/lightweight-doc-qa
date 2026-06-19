import ollama

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

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]