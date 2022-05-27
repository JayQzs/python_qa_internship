# Write a python program that will replace a word with a given length by the provided word
# Example if I have a sentence:
# This is a brown fox
# Add more tests for this as an example below

sentence = "Beginners when start programming often get bored if they do not get a chance to " \
           "play with some interesting code."

sentence2 = "London is the capital of Great Britain."
sentence3 = "Have you ever been in South Africa?"

def replace_words(text, length_to_replace, word):
    list_words = text.split()
    for words in range(len(list_words)):
        if len(list_words[words]) == length_to_replace:
            text = text.replace(list_words[words], word)
    return text


assert replace_words(sentence, 3, "test") == "Beginners when start programming often test bored if they do test test a chance " \
                                "to play with some interesting code."

assert replace_words(sentence2, 5, "test") == "London is the capital of test Britain."

assert replace_words(sentence3, 4, "test") == "test you test test in South Africa?"
