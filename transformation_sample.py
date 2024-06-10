import json
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Initialize the tokenizer and model
tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')

# Sample data: pairs of input and output attributes
data = [
    {"input": {"name": "John", "age": "30"}, "output": {"first_name": "John", "years": "30"}},
    {"input": {"name": "Alice", "age": "25"}, "output": {"first_name": "Alice", "years": "25"}}
]

# Prepare the data for training
train_data = []
for item in data:
    input_str = json.dumps(item['input'])
    output_str = json.dumps(item['output'])
    train_data.append((input_str, output_str))

# Tokenize the data
def tokenize_function(input_str, output_str):
    input_enc = tokenizer(input_str, padding='max_length', truncation=True, return_tensors='pt', max_length=32)
    output_enc = tokenizer(output_str, padding='max_length', truncation=True, return_tensors='pt', max_length=32)
    return input_enc, output_enc

# Create training tensors
inputs = []
labels = []
for input_str, output_str in train_data:
    input_enc, output_enc = tokenize_function(input_str, output_str)
    inputs.append(input_enc.input_ids)
    labels.append(output_enc.input_ids)

inputs = torch.cat(inputs)
labels = torch.cat(labels)

# Define the training loop
def train(model, inputs, labels, epochs=3, lr=1e-4):
    model.train()
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    for epoch in range(epochs):
        optimizer.zero_grad()
        outputs = model(input_ids=inputs, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}, Loss: {loss.item()}")

# Train the model
train(model, inputs, labels)

# Function to transform new JSON attributes
def transform_attributes(input_json):
    model.eval()
    input_str = json.dumps(input_json)
    input_enc = tokenizer(input_str, return_tensors='pt', max_length=32, truncation=True, padding='max_length')
    output_ids = model.generate(input_enc.input_ids, max_length=32, num_beams=4, early_stopping=True)
    output_str = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return json.loads(output_str)

# Example usage
new_input = [
    {"input": {"name": "John", "age": "30"},},
   
]
transformed_output = transform_attributes(new_input)
print(transformed_output)
