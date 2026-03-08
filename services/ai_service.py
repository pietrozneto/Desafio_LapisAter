from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def generate_script(data):

    prompt = f"""
Gere uma meditação guiada personalizada para um adolecente. Alem das informações a seguir, considere que o paciente esta em uma situação estressante devido a pressão academica.

Idade {data['age_range']}
Emoção: {data['mood']}
Contexto: {data['context']}
Estilo: {data['style']}
Duração: {data['length']} minutos

Make it calm and supportive.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return completion.choices[0].message.content