from flask import Flask, render_template, request
from gradio_client import Client

app = Flask(__name__)

# Gradio client setup
client = Client("https://jarif-summarization.hf.space/--replicas/ajzu9/")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        article = request.form["article"]
        # Make a prediction using the Gradio client
        result = client.predict(
            article,  # str in 'article' Textbox component
            api_name="/predict"
        )
        # Pass the result to the template
        return render_template("result.html", article=article, summary=result)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
