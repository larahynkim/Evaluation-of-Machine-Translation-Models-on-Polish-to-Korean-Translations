import re

def classify_sentences(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as f:
        sentences = f.readlines()
    
    # Classify each sentence as formal or informal
    classifications = []
    for sentence in sentences:
        if is_formal_korean(sentence):
            classifications.append('Formal')
        elif is_informal_korean(sentence):
            classifications.append('Informal')
        else:
            classifications.append('UNKNOWN')
    
    # Write the classifications to the output file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for i, sentence in enumerate(sentences):
            f.write(f'{classifications[i]}\n')
    
def is_formal_korean(sentence):
    formal_indicators = ['습니다','니다', '입니다', '한다', '니까', '시오','시다','신다','요']
    for indicator in formal_indicators:
        if indicator in sentence:
            return True
    return False

def is_informal_korean(sentence):
    informal_indicators = ['어', '해', '야', '이다', '었다', '돼','셔', '마','했다']
    for indicator in informal_indicators:
        if indicator in sentence:
            return True
    return False


classify_sentences('INPUT FILE HERE.txt', 'formality.txt')
print('Classification complete. Results written to output.txt.')