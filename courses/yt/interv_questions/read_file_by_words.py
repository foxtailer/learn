def read_file_by_words(path:str) -> """generator""":
    with open(path, 'r') as file:
        file_iterator = iter(file)

        for line in file_iterator:
            words = line.strip().split()

            for word in words:
                yield word

rfbw_generator = read_file_by_words('/home/zoy/vscode/file.txt')

for word in rfbw_generator:
    print(word)


##################################
def file_word_generator(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            for word in line.split():  # Split the line by whitespace to get words
                yield word


#################################
def file_word_generator(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        words_buffer = []  # Buffer to accumulate words
        num_words = 1  # Default number of words to yield
        
        for line in file:
            words_buffer.extend(line.split())  # Split the line and add to buffer
            
            while len(words_buffer) >= num_words:
                # Yield `num_words` words at a time
                yield words_buffer[:num_words]
                words_buffer = words_buffer[num_words:]  # Remove the yielded words
                
                # Wait for the next `send()` to get the new batch size
                num_words = (yield) or num_words  # Use the sent value or keep current batch size

        # Yield any remaining words in the buffer after file is done
        if words_buffer:
            yield words_buffer



