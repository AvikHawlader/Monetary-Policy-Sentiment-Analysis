import tkinter as tk
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment():
    user_input = entry.get().lower()

    # Initialize Vader SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()

    # Tokenize the user input into words
    words = user_input.split()

    # Initialize sentiment score
    total_sentiment = 0

    # Check sentiment of each word
    for word in words:
        word_sentiment = sentiment_data.get(word, None)
        if word_sentiment is not None:
            total_sentiment += word_sentiment
        else:
            # If word is not in the Excel sheet, use Vader
            sentiment = analyzer.polarity_scores(word)['compound']
            total_sentiment += sentiment

    show_result(total_sentiment)

def show_result(sentiment):
    result_window = tk.Toplevel(window)
    result_window.title("Sentiment Result")

    result_label = tk.Label(result_window, text=f"Total Sentiment Score: {sentiment:.2f}")
    result_label.pack()

# Load data from Excel sheet using pandas
sentiment_data = pd.read_excel("economic_sentiment_data.xlsx")
sentiment_data = sentiment_data.set_index("Word").squeeze().to_dict()

# Create the main window
window = tk.Tk()
window.title("Monetary Policy Sentiment Analysis")

# Create input entry field
label = tk.Label(window, text="Enter a paragraph from RBI Monetary Policy:")
label.pack()
entry = tk.Entry(window, width=50)
entry.pack()

# Create a button to trigger sentiment analysis
analyze_button = tk.Button(window, text="Analyze", command=analyze_sentiment)
analyze_button.pack()

# Start the main event loop
window.mainloop()
