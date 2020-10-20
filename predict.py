from flair.data import Sentence
from flair.models import SequenceTagger

tagger: SequenceTagger = SequenceTagger.load("ner")

sentence: Sentence = Sentence("George Washington went to Washington .")
tagger.predict(sentence)

<<<<<<< HEAD
print("Analysing the hotfix sentence %s“ % sentence)
=======
print("Irgendwas")
print("Analysing sentence %s“ % sentence)
>>>>>>> hotfix
print("\nThe following NER tags are found: \n")
print(sentence.to_tagged_string())
