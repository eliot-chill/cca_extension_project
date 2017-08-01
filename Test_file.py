import spacy

nlp = spacy.load('en')

spacy.en.English

question = "When was the Berlin Wall built?"

doc = nlp(question)

print([(w.text, w.pos_) for w in doc])

#print("Hello world!")
