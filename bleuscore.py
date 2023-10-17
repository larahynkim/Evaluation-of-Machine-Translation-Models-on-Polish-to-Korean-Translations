import sacrebleu

# Read the reference and translated files into lists of sentences
with open('korean_humantranslations.txt', 'r', encoding='utf-8') as ref_file, open('korean_machine_translations.txt', 'r', encoding='utf-8') as trans_file:
    reference = [line.strip() for line in ref_file]
    translated = [line.strip() for line in trans_file]

# Calculate the BLEU score using the sacrebleu library
bleu_score = sacrebleu.corpus_bleu(translated, [reference])

print("BLEU score:", bleu_score.score)