# Named Entity Recognition (NER) with spaCy

## 📌 Project Overview

This project explores **Named Entity Recognition (NER)** using spaCy, a popular Python library for Natural Language Processing (NLP).

The project uses spaCy's pretrained English language model, `en_core_web_sm`, to identify named entities in text, examine their labels, and visualize them using displaCy. It also demonstrates how to create custom entity spans and manually assign entity labels to a document.

## 🎯 Objectives

- Understand how Named Entity Recognition works.
- Extract named entities from text using spaCy.
- Identify entity types such as organizations and monetary values.
- Explore spaCy's NLP processing pipeline.
- Visualize named entities using displaCy.
- Understand tokens, documents, and spans.
- Create custom entities using spaCy's `Span` class.
- Modify document entity annotations using `doc.set_ents()`.

## 🛠️ Technologies Used

- **Python** — Programming language
- **spaCy** — Natural Language Processing library
- **displaCy** — Named entity visualization tool

## 📂 Project Structure

```text
NER/
├── main.py
└── README.md
```

*Note: Adjust the Python filename to match your repository.*

## ⚙️ Project Implementation

### 1. Loading the spaCy Model

The project loads spaCy's small English language model to process text and identify named entities.

```python
import spacy

nlp = spacy.load("en_core_web_sm")

print(nlp.pipe_names)
```

The pipeline components perform tasks such as tokenization, part-of-speech tagging, dependency parsing, and named entity recognition.

### 2. Named Entity Recognition

The project processes a sentence and extracts the entities recognized by the pretrained model.

```python
text = nlp(
    "Tesla Inc is going to acquire twitter for 45 billion"
)

for ent in text.ents:
    print(
        ent.text,
        "|",
        ent.label_,
        "|",
        spacy.explain(ent.label_)
    )
```

Each entity provides:

- **Entity text:** The identified word or phrase.
- **Entity label:** The category assigned to the entity.
- **Label explanation:** A description of the entity category.

Examples of common entity labels include `PERSON`, `ORG`, `GPE`, `DATE`, and `MONEY`.

### 3. Visualizing Named Entities

The project uses displaCy to display recognized entities and their labels.

```python
from spacy import displacy

print(displacy.render(text, style="ent"))
```

For browser-based visualization in a regular Python script:

```python
displacy.serve(text, style="ent")
```

This helps visualize how the NLP model identifies and categorizes entities within a sentence.

### 4. Working with Token Spans

The project explores how to extract a sequence of tokens from a processed document.

```python
doc = nlp(
    "Tesla Inc is going to acquire twitter for 45 billion"
)

s = doc[3:6]

print(s)
print(type(s))
```

A `Span` represents a continuous sequence of tokens within a spaCy document. In this example, the selected span is `going to acquire`.

### 5. Creating Custom Named Entities

The project demonstrates how to manually define entity spans using spaCy's `Span` class.

```python
from spacy.tokens import Span

s1 = Span(doc, 0, 2, label="ORG")
s2 = Span(doc, 8, 10, label="MONEY")

doc.set_ents(
    [s1, s2],
    default="unmodified"
)

for ent in doc.ents:
    print(ent.text, "|", ent.label_)
```

This assigns the `ORG` label to `Tesla Inc` and the `MONEY` label to `45 billion`.

The `doc.set_ents()` method updates entity annotations in the current document. It does not retrain the pretrained model.

## 🧠 Key Learning Outcomes

Through this project, I explored:

- Fundamental NLP concepts and spaCy's processing pipeline.
- Automatic named entity recognition using a pretrained model.
- Entity labels and their meanings.
- Named entity visualization with displaCy.
- Token indexing and document spans.
- Manual entity annotation using `Span`.
- Updating entity annotations using `doc.set_ents()`.
- The difference between pretrained model predictions and manually assigned entities.

## 🚀 Potential Improvements

Future improvements could include:

- Implementing custom entity patterns using spaCy's `EntityRuler`.
- Processing larger datasets of text.
- Building a custom NER model with annotated training data.
- Evaluating entity recognition precision, recall, and F1-score.
- Developing an interactive NER application using Streamlit or Flask.
- Exploring domain-specific entity recognition for engineering, construction, or business documents.

## 👨‍💻 Author

**Vedline Ochieng**

Civil Engineering Student | Machine Learning Enthusiast | Python Developer

Interested in Natural Language Processing, Machine Learning, Artificial Intelligence, and practical AI applications.

- GitHub: [Vedline2547](https://github.com/Vedline2547)
- LinkedIn: [Vedline Ochieng](https://www.linkedin.com/in/vedline-ochieng-025146290/)

## 📜 License

This project is intended for educational purposes and personal learning.
