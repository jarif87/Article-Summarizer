# Text-Summarizer

***Utilizing Hugging Face Transformers and Blurr, I streamlined data scraping and text summarization. Three specialized models were integrated seamlessly, allowing for accurate summaries. Deployment on Hugging Face Spaces ensured easy sharing and accessibility. This project showcases the efficiency of modern NLP for succinct text summarization.***

***Article Wordcloud***

<img src = "notebooks/article.png" width="700" height="500">

***Highlights Wordcloud***

<img src = "notebooks/highlights.png" width="700" height="500">

***Most Common Words in Highlights***

<img src = "notebooks/highlights_words.png" width="700" height="500">

***Most Common Words in Article***

<img src = "notebooks/article_words.png" width="700" height="500">

***Highlights Text Length***

<img src = "notebooks/highlights_len.png" width="700" height="500">

***Article Text Length***

<img src = "notebooks/article_len.png" width="700" height="500">


# Model Training

***I have trained three models for text summarization: distilbart-cnn-6-6, distilbart-cnn-12-6, and facebook/bart-large-cnn. Out of these, I've deployed the distilbart-cnn-12-6 model, which is a transformer model from Hugging Face.For implementing text summarization, I utilized the Blurr library along with Fastai. All the notebooks detailing the training and deployment process for these models are available [here](https://github.com/jarif87/Text-Summarizer/tree/main/notebooks).Feel free to explore the notebooks to understand the methodologies and techniques employed in training and deploying these models for text summarization.***


# Model Performance

***distilbart-cnn-6-6***

|accuracy|precision|recall|f1|
|---|---|---|---|
|0.91|0.90|0.97|0.93|



# Model Deployment

The text summarization model has been deployed on the HuggingFace Spaces Gradio App. You can access the implementation either by going to the deployment folder or directly through the provided [link](https://huggingface.co/spaces/jarif/Summarization) to the application.

<img src = "deployment/gradio_app_1.png" width="700" height="500">


<img src = "deployment/gradio_app_2.png" width="700" height="500">


# Web Deployment

***I've developed a Flask application specifically for text summarization. It's designed to take input text and generate a condensed summary. You're invited to explore the Flask branch to delve into the implementation details further. To try out the application in real-time, simply visit the live website accessible through the provided [link](https://text-summarizer-z6vl.onrender.com/).***


<img src = "deployment/flask_app_1.png" width="700" height="500">



<img src = "deployment/flask_app_2.png" width="700" height="500">

