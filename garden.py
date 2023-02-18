import spacy
nlp = spacy.load('en_core_web_sm')

print("=========================== GARDEN PATH SENTENCES ===========================\n")

text = "The man who hunts ducks out on the weekend. I told the girl the cat scratched Bill would help her. The cotton clothing is made of grows in Mississippi. British left waffles on Falklands. The tycoon sold the offshore oil tracts for a lot of money wanted to kill JR."
sep = '.'  #  Using '.' to seperate sentences.

#  Splits sentences and replaces period before adding to list.
gardenpathSentences = [x.strip(" ")+sep for x in text.split(sep)]  
gardenpathSentences.pop(-1)  #  Removes trailing sentence because of last period.

for count, sentence in enumerate(gardenpathSentences):
  #sentence = sentence.strip()  #  Strips redundant space for clean display.
  print(f"{count + 1}. {sentence}")
  
print("\n------ Tokenised ---------------\n")
for count, sentence in enumerate(gardenpathSentences):
  sample  = nlp(sentence)
  print(f"{count+1}.")
  print([(token, token.orth_, token.orth) for token in sample])
  print("")

print("\n------ Entity Recognition ------\n")
for count, sentence in enumerate(gardenpathSentences):
  text = nlp(sentence)
  print(f"{count+1}.")
  print([(word, word.label_, word.label) for word in text.ents])
  print("")


"""
4.
[(British, 'NORP', 381), (Falklands, 'ORG', 383)]
Found it strange to spaCy considered 'Falklands' an organisation.

5.
[(JR, 'PERSON', 380)]
Interesting the spaCY picked up 'JR' as a person. 

"""