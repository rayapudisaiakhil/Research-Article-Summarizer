from flask import Flask, render_template, request
import torch
import spacy
from transformers import PegasusTokenizer, PegasusForConditionalGeneration
import re
app = Flask(__name__)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load model and tokenizer
# Replace 'PegasusForConditionalGeneration' with your specific model class if different
model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-large")
model.load_state_dict(torch.load('C:/Users/nikhi/Downloads/test/model.pth', map_location=torch.device('cpu')))
tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-large")
def preprocess_text_spacy(text):
    # Pattern to capture everything up to and including "Abstract"
    pattern = r'(?is)^.*?\babstract\b'
    
    # Remove the matched content
    text = re.sub(pattern, '', text)

    # Pattern to capture acknowledgements section
    # Adjust the pattern as needed based on the document structure
    ack_pattern = r"(?i)(\n|^).*acknowledg(e|ing?ments?|ed?ments?)([\s\S]*?)(\n\w+|\Z)"
    
    # Remove the acknowledgements section
    text = re.sub(ack_pattern, '\n', text, flags=re.MULTILINE)

    # Pattern to capture references section
    # This pattern assumes that references section is near the end of the document
    ref_pattern = r"(?i)(\n|^).*\b(references|bibliography)\b([\s\S]*?)\Z"
    
    # Remove the references section
    text = re.sub(ref_pattern, '\n', text, flags=re.MULTILINE)
    # Process text with spaCy
    doc = nlp(text)
    # Keep only alphanumeric tokens
    clean_tokens = [token.text for token in doc if token.is_alpha or token.is_digit]
    # Rejoin tokens into a single string
    cleaned_text = ' '.join(clean_tokens)
    return cleaned_text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['text']
    cleaned_text = preprocess_text_spacy(text)
    summary_length = int(request.form.get('summary_length', 200))  # Default to 200 if not specified
    # New text summarizer function using the loaded model
    def model_based_summarizer(input_text, max_length):
        inputs = tokenizer(input_text, return_tensors='pt', max_length=1024, truncation=True)
        summary_ids = model.generate(inputs['input_ids'], max_length=max_length, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary

    summary = model_based_summarizer(cleaned_text,summary_length)
    return render_template('result.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)