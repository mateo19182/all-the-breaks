import os
import json
from pydub import AudioSegment

def process_audio_file(file_path):
    # Load audio file
    audio = AudioSegment.from_wav(file_path)
    
    # Get audio properties
    duration = len(audio) / 1000  # Duration in seconds
    sample_rate = audio.frame_rate
    
    return {
        "path": file_path,
        "duration": duration,
        "sample_rate": sample_rate,
        "amplitude": None,
        "weight": None,
        "info_path": None
    }

def process_wav_directory(directory):
    processed_data = []
    
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.wav'):
                file_path = os.path.join(root, filename)
                relative_path = os.path.relpath(file_path, directory)
                processed_item = process_audio_file(file_path)
                processed_item["path"] = "dataset/dataset/" + relative_path.replace(os.sep, '/')
                processed_data.append(processed_item)
    
    return processed_data

# Specify the directory containing your WAV files
directory = 'dataset'
# Process all WAV files
results = process_wav_directory(directory)

# Save the results in the specified format
with open('breaks.jsonl', 'w') as f:
    for item in results:
        json.dump(item, f, separators=(',', ':'))
        f.write('\n')  # Line break between items

print("Processing complete. Results saved to 'processed_samples.txt'")
