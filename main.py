# Import necessary libraries
import spacy
from spacy import displacy
from spacy.tokens import Span
nlp = spacy.load('en_core_web_sm')
print(nlp.pipe_names)
text = nlp("Tesla Inc is going to acquire twitter for 45 billion")
for ent in text.ents:
    print(ent.text,"|",ent.label_ ,"|",spacy.explain(ent.label_))
print(displacy.render(text,style='ent'))
# Setting our own entities
doc = nlp("Tesla Inc is going to acquire twitter for 45 billion")
for ent in doc.ents:
    print(ent.text,"|",ent.label_)
s = doc[3:6]
print(s)
print(type(s))
s1 = Span(doc,0,2,label='ORG')
s2 = Span(doc,8,10,label='ORG')
doc.set_ents([s1,s2],default='unmodified')
for ent in doc.ents:
    print(ent.text,"|",ent.label_)
