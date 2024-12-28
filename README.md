# 📚 Word Lookup Dictionary

The **Word Lookup Dictionary** is a powerful, user-friendly desktop application designed to provide quick access to word definitions. Built with Python, this tool integrates a local word database and online definition lookup, delivering a comprehensive and efficient reference experience. Whether you’re a student, professional, or language enthusiast, this application offers a fast and reliable way to search for word meanings, correct spelling errors, and enhance vocabulary.


![](world_lookup.png)

## ✨ Key Features

- **Word Definition Lookup**: Instantly search for the definitions of English words.
- **Local Dictionary**: A robust local word list for fast, offline word verification.
- **Online Definition Retrieval**: Fetches up-to-date definitions from Merriam-Webster's online dictionary.
- **Auto-suggestion**: Intelligent word suggestions based on partial user input.
- **Auto-correction**: Automatically suggests corrections for misspelled words.
- **Caching**: Stores recently accessed definitions for rapid retrieval.
- **Search History**: Tracks recent word lookups for easy reference.
- **User-friendly GUI**: A clean and intuitive graphical user interface for a seamless user experience.

---

## 🚀 Setup and Installation

Follow these steps to set up and run the application:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/adityakch/Word-Lookup-Dictionary.git
   ```

2. **Install Required Packages**:
   Navigate to the project directory and install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Word List**:
   Ensure you have a `data/word_list.txt` file containing a list of English words (one word per line).

4. **Run the Application**:
   Execute the following command to start the application:
   ```bash
   python src/main.py
   ```

---

## 📖 Usage

1. Enter a word in the search box and click "Search" or press **Enter** to view its definition.
2. The word definition will be displayed in the result area.
3. Use the **"Suggest"** button to get word suggestions based on partial input.
4. Use the **"Auto-correct"** button to get spelling suggestions for misspelled words.
5. Recent lookups are displayed in the **History** section, allowing easy access to previous searches.

---

## 🙏 Acknowledgments

- **Merriam-Webster**: For providing a comprehensive and reliable online dictionary service.
