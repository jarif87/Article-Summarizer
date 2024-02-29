import torch
import gradio as gr
from fastai.text.all import *
from transformers import BartTokenizer
from datasets import load_dataset, load_metric

# Load the pre-trained model and tokenizer (adjust for Bart if needed)
pretrained_model_name = "facebook/bart-large-cnn"  # Or "facebook/bart-base"
hf_tokenizer = BartTokenizer.from_pretrained(pretrained_model_name)

# Load the SQuAD dataset
squad = load_dataset("squad")

# Load the SQuAD metric
squad_metric = load_metric("squad", data_dir="path/to/squad/dataset", trust_remote_code=True)

def summarize(article):
    # Define your data transformation pipeline here, if applicable
    # ...

    # Load the exported model
    learn = load_learner('article_highlights.pkl')

    # Generate the summary
    summary = learn.blurr_generate(article)[0]

    return summary

# Create the Gradio interface
iface = gr.Interface(
    fn=summarize,
    inputs="text",
    outputs="text",
    title="Article Summarizer",
    description="Enter an article and get a summary.",
    examples=[["This is an example article..."]]
)

# Launch the Gradio interface
iface.launch()
