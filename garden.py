# Lesson SE-T37
# Task 1


# Import module
import spacy 


# Load language module
nlp = spacy.load('en_core_web_sm')


# Initiate list to store the garden sentences in.
gardenpathSentence = []

sentence1 = "The cotton clothing is made of grows in Mississippi USA."
sentence2 = "The person told the story laught at 12."
sentence3 = "When Joe Summers eats food gets thrown."
sentence4 = "The cat I have really likes chicken."
sentence5 = "I painted the Hollywood wall with cracks." 

gardenpathSentence.append(sentence1)
gardenpathSentence.append(sentence2)
gardenpathSentence.append(sentence3)
gardenpathSentence.append(sentence4)
gardenpathSentence.append(sentence5)


# Tokenize the sentences in the list.
tokenized = [words.split() for words in gardenpathSentence]
nlp_tokenized = nlp(str(tokenized))
print()
print("Tokenized list: ", nlp(str(tokenized)))


# Perform entity recognition and display to the screen.
print()
print("Entity labels: " , [(i, i.label_, i.label) for i in nlp_tokenized.ents])

# Display the meanings of two entities.
entity_fac = spacy.explain("PERSON")
print("""
    Meaning of labels:
                    """)
print(f"    PERSON: {entity_fac}")

print()
entity_fac = spacy.explain("GPE")
print(f"    GPE: {entity_fac}")
print()

# I did look up the Person entity and the exlpaination was People,  including fictional.
# Yes the explaination makes sense in terms of the word associated.

# I did look up the GPE entity and the exlpaination was Countries, cities, states.
# Yes the explaination makes sense in terms of the word associated.
