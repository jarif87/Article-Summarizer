import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        input_text = request.form['text']
        summary = summarize(input_text)
        return render_template("result.html", input_text=input_text, output_text=summary)
    else:
        return render_template("index.html")

def summarize(article):
    response = requests.post("https://jarif-summarization.hf.space/run/predict", json={
        "data": [
            article,
        ]
    }).json()
    data = response["data"]
    if data:
        return data[0]  # Assuming the summarized data is returned as a list with one element
    else:
        return "Error: Unable to summarize the text."

if __name__ == "__main__":
    app.run(debug=True)
