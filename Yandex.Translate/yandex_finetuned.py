import requests
import json
import re


# Set up Yandex.Translate API parameters
api_key = 'trnsl.1.1.20230427T022344Z.96aa13b97191a101.a7cc917f3cf506cc343464b2544f7285670de671'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
params = {
    'key': api_key,
    'lang': 'pl-ko',  # Translate from Polish to Korean
    'format': 'plain',
}



with open('1.txt', 'r', encoding="utf-8") as input_file, open('output9.txt', 'w', encoding="utf-8") as output_file:
    for line in input_file:
        line = line.strip()
        
        if not line:
            continue

        params['text'] = line

        response = requests.get(url, params=params)
        
        translation = json.loads(response.text)['text'][0]

        if "없다.$" in translation: 
            translation = translation[:-len("없다. ")] + " 없어요."
        elif "것이다.$" in translation: 
            translation = translation[:-len("것이다. ")] + " 것 입니다."
        elif "되었다" in translation: 
            translation = translation[:-len("되었다 ")] + "되었습니다."
        elif "입었다" in translation: 
            translation = translation[:-len("입었다 ")] + "입었습니다."  
        elif "싶다." in translation: 
            translation = translation[:-len("싶다. ")] + " 싶어요."
        elif "있다." in translation: 
            translation = translation[:-len("있다. ")] + "있습니다."
        elif "었다.$" in translation: 
            translation = translation[:-len("었다. ")] + "었습니다."
        elif "해." in translation: 
            translation = translation[:-len("해. ")] + "합니다."
        elif "했다" in translation: 
            translation = translation[:-len("했다 ")] + "했습니다."
        elif "갔다." in translation: 
            translation = translation[:-len("갔다. ")] + "갔습니다."
        elif "았다." in translation: 
            translation = translation[:-len("았다. ")] + "았습니다."
        elif "란다." in translation: 
            translation = translation[:-len("란다. ")] + "랍니다."
        elif "이다." in translation: 
            translation = translation[:-len("이다. ")] + "입니다."
        elif "쳤다." in translation: 
            translation = translation[:-len("쳤다. ")] + "쳤습니다."
        elif "왔다." in translation: 
            translation = translation[:-len("왔다. ")] + "왔습니다." 
    
        translation = translation.strip()
        

        output_file.write(translation + '\n')
