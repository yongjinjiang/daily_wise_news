async function summarizeArticles() {
    const articles = document.getElementById("articles").value.split("\n\n");
    const language = document.getElementById("language").value;

    const response = await fetch("/summarize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ articles, language })
    });

    const data = await response.json();
    if (response.ok) {
        document.getElementById("output").innerText = `最终总结：\n${data.final_summary}`;
    } else {
        document.getElementById("output").innerText = `错误：${data.error}`;
    }
}
