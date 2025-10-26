# 📝 Survey Feedback Analyzer

## 📌 Project Overview
The **Survey Feedback Analyzer** is a beginner-friendly Python project that demonstrates how to process and analyze textual feedback data using core Python programming concepts. The project simulates a small-scale survey system that stores user feedback, cleans and standardizes text, extracts meaningful insights, and provides summary statistics.

This project focuses on practical applications of **data cleaning**, **string operations**, **loops**, **conditionals**, and **user-defined functions** — all fundamental skills in **data analytics and data science**.

---

## 🎯 Objectives
The goal of this project is to:
- Collect and manage feedback data efficiently.
- Clean and standardize text data for analysis.
- Identify common keywords and sentiment indicators in feedback.
- Generate basic insights such as average rating, longest feedback, and frequently used words.

---

## 🧠 Key Features

### 1. **Preloaded Feedback Data**
The program begins with a dictionary containing 10 sample feedback entries.  
Each entry includes:
- Serial Number (`S_No`)
- Name
- Text Feedback
- Rating (1–5)

### 2. **Dynamic Feedback Entry**
Users can add any number of new feedbacks through console input.  
The program automatically increments serial numbers and appends new entries to the dictionary.

### 3. **Text Cleaning**
All feedbacks are cleaned using string operations:
- Punctuation marks are removed (`.,!?`)
- Extra spaces are reduced to single spaces
- Leading/trailing spaces are trimmed
- Text is converted to lowercase for uniformity

### 4. **Word Count Insights**
A user-defined function `count_word_in_feedbacks(word)` identifies how many feedbacks mention specific words such as:
- “good”
- “poor”
- “excellent”

The matching is **case-insensitive**.

### 5. **Summary & Insights**
The program displays:
- The final cleaned feedback dataset  
- The **average rating** across all feedbacks  
- The **feedback with the longest comment** (based on word count)
