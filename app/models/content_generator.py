import openai

def generate_content(topic):
    openai.api_key = "your_openai_api_key"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Write a blog post about {topic}.",
        max_tokens=200
    )
    return response.choices[0].text.strip()
