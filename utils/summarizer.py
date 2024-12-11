import openai

# OpenAI API Key
openai.api_key = "your_openai_api_key"

def generate_summary(article_text, language="中文"):
    prompt = f"请总结以下文章的核心内容，用{language}表达：\n\n{article_text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
