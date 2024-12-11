from flask import Flask, request, jsonify
from utils.summarizer import generate_summary

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Hackathon!"


@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    articles = data.get("articles", [])
    language = data.get("language", "中文")
    
    if not articles:
        return jsonify({"error": "No articles provided"}), 400
    
    # Generate summaries
    summaries = [generate_summary(article, language) for article in articles]
    
    # Combine and generate final summary
    combined_summary = "\n".join(summaries)
    final_prompt = f"以下是几篇文章的摘要，请进一步总结核心内容，用{language}表达：\n\n{combined_summary}"
    final_summary = generate_summary(final_prompt, language)
    
    return jsonify({
        "individual_summaries": summaries,
        "final_summary": final_summary
    })

if __name__ == "__main__":
    app.run(debug=True)


