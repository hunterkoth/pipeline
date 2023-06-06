
import nltk
nltk.download('punkt')

def split_into_sentences(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    sentences = nltk.sent_tokenize(text)
    return sentences

def write_sentences_to_file(sentences, output_file_path):
    with open(output_file_path, 'w') as file:
        for sentence in sentences:
            file.write(sentence + '\n')

# Example usage
input_file_path = input('Input path: ')
output_file_path = input('Output path: ')

sentences = split_into_sentences(input_file_path)
write_sentences_to_file(sentences, output_file_path)

