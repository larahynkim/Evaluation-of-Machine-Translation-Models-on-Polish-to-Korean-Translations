# This program is used to get 500 machine translated sentences into a text file
# Uses the polish_translations.txt file that has a collection of 500 human made polish sentences



import requests
import json

# Set up Yandex.Translate API parameters
api_key = 'trnsl.1.1.20230427T022344Z.96aa13b97191a101.a7cc917f3cf506cc343464b2544f7285670de671'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
params = {
    'key': api_key,
    'lang': 'en-ko',  # Translate from Polish to Korean
    'format': 'plain',
}

# Open the input and output files
with open('english_machine_translations.txt', 'r',encoding="utf-8") as input_file, open('korean_pivot_translations.txt', 'w',encoding="utf-8") as output_file:
    # Loop over each line in the input file
    for line in input_file:
        # Remove any leading/trailing whitespace and newlines
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Set the text to be translated
        params['text'] = line
        
        # Send the translation request to the Yandex.Translate API
        response = requests.get(url, params=params)
        
        # Parse the response JSON and get the translation
        translation = json.loads(response.text)['text'][0]
        
        # Write the translation to the output file
        output_file.write(translation + '\n')