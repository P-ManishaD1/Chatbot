Objective:
To create a simple AI chatbot that reads questions and answers from a CSV file, processes them using natural language processing (NLP), and interacts with the user through a graphical interface built using Tkinter.

Module 1: Data Preparation and Processing
This module processes the CSV data to prepare it for chatbot use.

Steps:
Read CSV File:

Use pandas to load a CSV file with two columns: Question and Answer.

Tokenization:

Use nltk.word_tokenize() to split each question into words.

Stopword Removal:

Remove common stopwords using NLTK’s stopword list.

POS Tagging and Lemmatization:

Use nltk.pos_tag() and WordNetLemmatizer to reduce words to their base form based on part of speech.

Combine with Hyphen:

Join the cleaned tokens using a hyphen (-) to form a processed version of the question.

Map to Answers:

Link each processed question to its original answer.

Save to Output CSV:

Store the processed data in a new CSV (e.g., processed_qa.csv) using pandas.

Module 2: User Interaction and Response Retrieval (Using Tkinter)
This module provides a GUI using Tkinter for user interaction.

Steps:
User Input Box:

Use a Tkinter Entry widget to accept a question from the user.

Preprocess the Input:

Apply the same steps (tokenization, stopword removal, lemmatization, and join with hyphen).

Answer Retrieval:

Compare the user’s processed question with those in processed_qa.csv.

Use fuzzy matching if there’s no exact match.

Display Response:

Show the answer in a separate Label or Text widget.

Show a fallback response if no match is found.

Chat History:

Append each question and answer to a chat window (e.g., using Text widget or a scrolling Listbox).

Theme Customization (Optional):

Use Tkinter’s ttk.Style() or custom background and font settings to personalize the chat window.

Additional Enhancements (Implemented or Optional)
Feature	Description
Chat History	Maintains a running log of all Q&A
Fuzzy Matching	Finds closest matching question if input is different
Colorful GUI	Background color, font styles can be changed
Scrollable Chat	Can scroll to view full conversation
