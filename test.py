import re

def split_sentence(sentence):
    # Split the sentence using a regex that matches single spaces or multiple spaces
    words = re.split(r'(\s+)', sentence)
    # Filter out empty strings that result from consecutive spaces
    words = [word for word in words if word]
    return words

# Example sentence
sentence = "value1 value2  value3"

# Split the sentence
split_words = split_sentence(sentence)

# Print the result
print(split_words)