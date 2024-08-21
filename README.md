# Research-Article-Summarizer

This project is an article or text summarizer that uses frequency analysis to extract key sentences from a given text. It can be used to quickly generate summaries for long paragraphs or articles.

## How it Works

The text summarizer works by following these steps:

1. The input text is tokenized into individual words.
2. A frequency table is created to count the occurrence of each word, excluding common stop words.
3. Sentences are tokenized from the input text.
4. Each sentence is assigned a value based on the frequency of the words it contains.
5. The average value of the sentences is calculated.
6. Sentences with a value greater than 1.25 times the average value are considered key sentences.
7. The key sentences are combined to generate the summary.

## Requirements

- Python 3.x
- nltk library: `pip install nltk`

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/rayapudisaiakhil/Research-Article-Summarizer.git
   cd Text_Summarizer
   ```
2. Install the required dependencies using pip:
   ```
   pip install nltk
   ```
3. Run the text summarizer:
   ```
   python app.py
   ```
4. Enter the input text when prompted and press Enter. The program will generate a summary of the input text and display it.

## Customization

You can customize the text summarizer to suit your specific needs:

1. Add or modify stop words: You can edit the `stop_words` set in the `text_summarizer` function to include additional stop words or remove existing ones. Stop words are commonly occurring words that are typically excluded from the frequency analysis.
2. Adjust the sentence value threshold: The current threshold for considering a sentence as a key sentence is 1.25 times the average value. You can modify this threshold in the `text_summarizer` function to adjust the sensitivity of the summarization process.

This README.md file provides a high-level overview of the text summarizer project, along with instructions for setting it up and customizing it. Feel free to customize and expand upon this README.md file to provide additional information about your project, its features, and any other relevant details you'd like to include.
