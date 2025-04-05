# AI Chatbot using Tkinter and NLP

## 📌 Project Explanation

This project is a simple **AI chatbot** application developed using **Python** and **Tkinter** for the graphical user interface. It uses **Natural Language Processing (NLP)** techniques from the `nltk` library to process a dataset of questions and answers stored in a CSV file.

The chatbot works in two main modules:

- **Module 1 (Data Preparation):** Processes each question using tokenization, stopword removal, POS tagging, and lemmatization, and stores the cleaned data in a new CSV file.
- **Module 2 (User Interaction):** Allows users to interact through a GUI, where the chatbot responds with relevant answers using fuzzy matching if an exact match is not found.

---

## ✅ Requirements

To run this project, you need to have the following Python libraries installed:

```bash
pip install pandas
pip install nltk
pip install fuzzywuzzy
pip install python-Levenshtein
Also, download the required nltk packages:

python
Copy
Edit
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
📂 Project Structure
bash
Copy
Edit
AI_Chatbot_Tkinter/
│
├── qa.csv                # Original CSV with raw Questions and Answers
├── processed_qa.csv      # CSV with processed questions and original answers
├── preprocess_data.py    # Python script to process data and create processed_qa.csv
├── chatbot_app.py        # Main GUI chatbot application using Tkinter
└── README.md             # Project documentation (this file)
▶️ How to Run the Project
Step 1: Prepare the Dataset
Make sure you have a CSV file named qa.csv with two columns:

Column 1: Questions

Column 2: Answers

Step 2: Run Preprocessing
Process the questions by running:

bash
Copy
Edit
python preprocess_data.py
This will generate processed_qa.csv with cleaned question formats.

Step 3: Launch the Chatbot
Start the GUI application by running:

bash
Copy
Edit
python chatbot_app.py
The chatbot window will open. You can type a question, and it will respond based on the processed CSV data.

📎 Example
User Input:
What is artificial intelligence?

Bot Response:
Artificial intelligence is the simulation of human intelligence by machines.

📌 Notes
The chatbot uses fuzzy matching to find the closest question in the dataset if an exact match is not found.

The GUI maintains chat history and is designed with basic styling using Tkinter.

You can modify the chatbot_app.py file to customize themes, fonts, or behavior.

📘 License
This project is created for academic and educational purposes.

yaml
Copy
Edit

---

You can copy and paste this into a file named `README.md` and place it in the root of your GitHub repository.

Let me know if you also want me to generate the Python files (`preprocess_data.py` and `chatbot_app.py`) with full code.








