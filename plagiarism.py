import tkinter as tk
from tkinter import scrolledtext, messagebox
import nltk

nltk.download('punkt')

def get_cosine_similarity(text1, text2):
    tokens1 = set(nltk.word_tokenize(text1))
    tokens2 = set(nltk.word_tokenize(text2))

    intersection = len(tokens1.intersection(tokens2))
    union = len(tokens1.union(tokens2))

    if union == 0:
        return 0.0

    similarity = intersection / union
    return similarity * 100

def check_plagiarism():
    text1 = text_box1.get("1.0", tk.END)
    text2 = text_box2.get("1.0", tk.END)

    if not (text1.strip() and text2.strip()):
        messagebox.showerror("Error", "Both text boxes must be filled.")
        return

    similarity = get_cosine_similarity(text1, text2)

    result_text = f"Similarity: {similarity:.2f}%"
    result_label.config(text=result_text)

    if similarity > 50:
        result_label.config(fg="red")
    else:
        result_label.config(fg="black")

# Create main window
root = tk.Tk()
root.title("Plagiarism Checker")

# Styling
root.configure(bg="#e6e6e6")
root.geometry("600x400")

# Header
header_label = tk.Label(root, text="Plagiarism Checker", font=("Helvetica", 24), bg="#333", fg="white", pady=10)
header_label.pack(fill="x")

# Text boxes for comparison
label_style = {"font": ("Helvetica", 14), "bg": "#e6e6e6"}
text_box_style = {"wrap": tk.WORD, "height": 5, "width": 60, "bg": "#f2f2f2", "fg": "#333", "font": ("Helvetica", 12)}

tk.Label(root, text="Text 1:", **label_style).pack(pady=10)
text_box1 = scrolledtext.ScrolledText(root, **text_box_style)
text_box1.pack(expand=True, fill="both")

tk.Label(root, text="Text 2:", **label_style).pack(pady=10)
text_box2 = scrolledtext.ScrolledText(root, **text_box_style)
text_box2.pack(expand=True, fill="both")

# Check plagiarism button
check_button = tk.Button(root, text="Check Plagiarism", command=check_plagiarism, bg="#4CAF50", fg="white", font=("Helvetica", 14))
check_button.pack(pady=15)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 18), bg="#e6e6e6")
result_label.pack()

# Run the application
root.mainloop()
