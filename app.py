import nltk
import json

# Download the punkt tokenizer if you haven't already
nltk.download('punkt')

def map_sentences_to_json(sentence1, sentence2):
    # Tokenize the sentences
    tokens1 = nltk.word_tokenize(sentence1)
    tokens2 = nltk.word_tokenize(sentence2)
    
    # Create a dictionary by zipping tokens1 and tokens2
    result_dict = dict(zip(tokens1, tokens2))
    
    # Convert the dictionary to a JSON string
    json_result = json.dumps(result_dict, indent=4)
    
    return json_result

# Example sentences
sentence1 = "1 2 3"
sentence2 = "4   6"

# Get the JSON result
json_result = map_sentences_to_json(sentence1, sentence2)

# Print the JSON result
print(json_result)
