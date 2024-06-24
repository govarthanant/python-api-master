import openai

# Set your OpenAI API key here
openai.api_key = ''

def get_chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model you want to use
        messages=[
            {"role": "system", "content": "You are ChatGPT, a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,  # Adjust the max tokens to control the length of the response
        temperature=0.7,  # Adjust the temperature for the creativity of the response
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message['content']

# Example usage
prompt = """I want to get the executedBy and executedTimestamp from the below json and get the output as a json 
and all the date fields in the output json should be in the datetime format and I don't want a code I want output json only

input json is 
{
"random": "53",
	"random float": "97.059",
	"bool": "true",
	"date": "1990-12-18",
"execution" : "Monday 24, June, 2024",
	"regEx": "hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo to you",
	"enum": "generator",
	"firstname": "Danika",
	"lastname": "Heisel",
	"city": "Fort-de-France",
	"country": "Saint Vincent and the Grenadines",
	"countryCode": "GW",
"person executed" : "Test",
}"""
response = get_chatgpt_response(prompt)
print(response)
