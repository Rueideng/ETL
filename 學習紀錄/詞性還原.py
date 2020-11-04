from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

# 獲取單字的詞性
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

sentence = "The pot is much more fun than giving it 50 points, but that would make the total of this turn too high. I could have put all kinds of figures on it, but bottom line is: I think it's gruesome stuff. It smells really repulsive, it tastes slightly less miserable than it smells, and that is what I'm saying with everything."
tokens = word_tokenize(sentence)  # 分詞
tagged_sent = pos_tag(tokens)     #獲取單字的詞性

wnl = WordNetLemmatizer()
lemmas_sent = []
sentence_merge =""
for tag in tagged_sent:
    wordnet_pos = get_wordnet_pos(tag[1]) or wordnet.NOUN
    lemmas_sent.append(wnl.lemmatize(tag[0], pos=wordnet_pos)) # 詞性還原
for sent in lemmas_sent:
    sentence_merge =sentence_merge+ " "+sent
print(sentence_merge)