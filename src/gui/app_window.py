import tkinter as tk
from tkinter import ttk
from data_structures.trie import Trie
from algorithms.auto_correct import AutoCorrect
from web_scraping.dictionary_scraper import get_definition
import time

class Cache:
    def __init__(self, expiration_time=3600):  # Cache entries expire after 1 hour by default
        self.cache = {}
        self.expiration_time = expiration_time

    def get(self, key):
        if key in self.cache:
            entry = self.cache[key]
            if time.time() - entry['time'] < self.expiration_time:
                return entry['value']
            else:
                del self.cache[key]
        return None

    def set(self, key, value):
        self.cache[key] = {'value': value, 'time': time.time()}

class WordLookupDictionary:
    def __init__(self):
        self.trie = Trie()
        self.window = tk.Tk()
        self.window.title("Word Lookup Dictionary")
        self.setup_gui()
        self.load_dictionary()
        self.cache = Cache()
        self.history = []

    def setup_gui(self):
        self.frame = ttk.Frame(self.window, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.word_var = tk.StringVar()
        self.word_entry = ttk.Entry(self.frame, width=30, textvariable=self.word_var)
        self.word_entry.grid(column=0, row=0, sticky=(tk.W, tk.E))

        self.search_button = ttk.Button(self.frame, text="Search", command=self.search_word)
        self.search_button.grid(column=1, row=0)

        self.result_text = tk.Text(self.frame, wrap=tk.WORD, width=40, height=10)
        self.result_text.grid(column=0, row=1, columnspan=2, sticky=(tk.W, tk.E))

        self.suggest_button = ttk.Button(self.frame, text="Suggest", command=self.auto_suggest)
        self.suggest_button.grid(column=0, row=2)

        self.correct_button = ttk.Button(self.frame, text="Auto-correct", command=self.auto_correct)
        self.correct_button.grid(column=1, row=2)

        # Add history display
        self.history_frame = ttk.Frame(self.window, padding="10")
        self.history_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        ttk.Label(self.history_frame, text="Recent Lookups:").grid(column=0, row=0, sticky=tk.W)
        
        self.history_listbox = tk.Listbox(self.history_frame, height=10)
        self.history_listbox.grid(column=0, row=1, sticky=(tk.W, tk.E))
        self.history_listbox.bind('<<ListboxSelect>>', self.on_history_select)

    def load_dictionary(self):
        try:
            with open('data/word_list.txt', 'r') as file:
                self.words = set(file.read().split())
            for word in self.words:
                self.trie.insert(word.lower())
            self.autocorrect = AutoCorrect(self.words)
            print(f"Loaded {len(self.words)} words into the dictionary.")
        except FileNotFoundError:
            print("Error: word_list.txt not found. Creating a new file.")
            self.words = set()
        except Exception as e:
            print(f"An error occurred while loading the dictionary: {str(e)}")
            self.words = set()

    def search_word(self):
        word = self.word_var.get().lower()
        
        # Check cache first
        cached_definition = self.cache.get(word)
        if cached_definition:
            self.display_result(word, cached_definition)
            self.update_history(word)
            return

        try:
            definition = get_definition(word)
            
            if definition != "Definition not found.":
                self.cache.set(word, definition)  # Cache the result
                if word not in self.words:
                    self.add_word_to_dictionary(word)
                self.display_result(word, definition)
            else:
                if self.trie.search(word):
                    self.display_result(word, "Word is in the dictionary, but no definition was found.")
                else:
                    self.display_result(word, "Word not found in the dictionary.")
            
            self.update_history(word)
        
        except Exception as e:
            self.display_result(word, f"An error occurred: {str(e)}")

    def display_result(self, word, text):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Definition of '{word}':\n{text}")

    def on_history_select(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            word = event.widget.get(index)
            self.word_var.set(word)
            self.search_word()

    def update_history(self, word):
        if word not in self.history:
            self.history.append(word)
            if len(self.history) > 10:  # Keep only the 10 most recent lookups
                self.history.pop(0)
        self.update_history_display()

    def update_history_display(self):
        self.history_listbox.delete(0, tk.END)
        for word in reversed(self.history):
            self.history_listbox.insert(tk.END, word)

    def add_word_to_dictionary(self, word):
        self.words.add(word)
        self.trie.insert(word)
        with open('data/word_list.txt', 'a') as file:
            file.write(f"\n{word}")
        print(f"Added '{word}' to the dictionary.")

    def auto_suggest(self):
        partial_word = self.word_var.get().lower()
        suggestions = self.trie.suggest(partial_word)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Suggestions for '{partial_word}':\n" + "\n".join(suggestions))

    def auto_correct(self):
        word = self.word_var.get().lower()
        corrected = self.autocorrect.correct(word)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Auto-corrected: '{corrected}'")

    def run(self):
        self.window.mainloop()