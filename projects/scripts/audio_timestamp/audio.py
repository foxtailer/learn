import speech_recognition as sr
from pydub import AudioSegment
import os

def transcribe_audio_with_timestamps(audio_path):
    # Load the audio file
    audio = AudioSegment.from_mp3(audio_path)
    recognizer = sr.Recognizer()

    # Split the audio into small chunks for better accuracy
    chunk_length_ms = 30000  # 30 seconds
    chunks = list(audio[::chunk_length_ms])

    transcription = []
    for i, chunk in enumerate(chunks):
        chunk.export("chunk.wav", format="wav")
        with sr.AudioFile("chunk.wav") as source:
            audio_listened = recognizer.record(source)
            try:
                # Recognize the chunk
                text = recognizer.recognize_google(audio_listened)
                start_time = i * chunk_length_ms
                end_time = start_time + len(chunk)
                transcription.append((start_time, end_time, text))
            except sr.UnknownValueError:
                # Speech is unintelligible
                transcription.append((start_time, end_time, ""))
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

    # Clean up the temporary chunk file
    os.remove("chunk.wav")

    return transcription

def format_time(milliseconds):
    hours = milliseconds // 3600000
    milliseconds %= 3600000
    minutes = milliseconds // 60000
    milliseconds %= 60000
    seconds = milliseconds // 1000
    milliseconds %= 1000
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{int(milliseconds):03}"

def align_text_with_timestamps(transcription, text_lines):
    # Combine the transcription into one string
    full_transcription = " ".join([text for _, _, text in transcription])

    # Split the combined transcription into words
    transcribed_words = full_transcription.split()

    # Create a list of start times for each word
    word_start_times = []
    current_time = 0
    for start, end, text in transcription:
        words = text.split()
        word_duration = (end - start) // len(words) if words else 0
        for word in words:
            word_start_times.append((word, current_time))
            current_time += word_duration

    # Align the lines with the transcribed words
    aligned_text = []
    word_index = 0

    for idx, line in enumerate(text_lines):
        line = line.strip()
        if not line:
            continue

        line_words = line.split()
        if word_index >= len(word_start_times):
            break

        start_time = word_start_times[word_index][1]
        end_time = (word_start_times[word_index + len(line_words) - 1][1]
                    if word_index + len(line_words) - 1 < len(word_start_times)
                    else word_start_times[-1][1] + 1000)

        aligned_text.append(f"{idx}\n{format_time(start_time)} --> {format_time(end_time)}\n{line}\n")
        word_index += len(line_words)

    return aligned_text

# Main function to integrate everything
def main(audio_path, text_file_path, output_file_path):
    transcription = transcribe_audio_with_timestamps(audio_path)
    with open(text_file_path, "r") as file:
        text_lines = file.readlines()

    aligned_text = align_text_with_timestamps(transcription, text_lines)
    
    with open(output_file_path, "w") as output_file:
        for line in aligned_text:
            output_file.write(line + "\n")

    print(f"Aligned text with timestamps has been saved to {output_file_path}")

# Example usage
if __name__ == "__main__":
    audio_path = "your_audio.mp3"
    text_file_path = "input.txt"
    output_file_path = "output.txt"

    main(audio_path, text_file_path, output_file_path)