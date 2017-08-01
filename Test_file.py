import spacy                           # See "Installing spaCy"

nlp = spacy.load('en')

spacy.en.English                 # You are here.

doc = nlp(u'Hello, spacy!')            # See "Using the pipeline"

print([(w.text, w.pos_) for w in doc])


#print("Hello world!")
