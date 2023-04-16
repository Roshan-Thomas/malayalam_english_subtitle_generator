# Author: Roshan Thomas

import whisper 
from utils import write_to_srt, transcribe_malayalam_to_english
import argparse

# Command Line Arguments
parser = argparse.ArgumentParser()

parser.add_argument("-a", "--audio", help="Audio file name (to be converted), must be .wav or .mp3 file")
parser.add_argument("-l", "--load", help="Load file path for loading audio files. Default is current directory")
parser.add_argument("-s", "--save", help="File path for saving .srt files [Optional]")
parser.add_argument("-m", "--model", help="Whisper Model to be used (tiny, small, medium, large) [Optional]")

args = parser.parse_args()



def load_model(model_size):
    model = whisper.load_model(model_size)   
    return model

if __name__ == "__main__":
    audio_filename = args.audio                                    # Enter name of the audio file to be translated here
    model_size = "large"                                           # Enter size of the model to be used (tiny, small, medium, or large)
    load_path = f"{args.load}"                                     # Load Path of Input
    save_path = "."                                                # Save Path of Output

    if args.model:
        model_size = f"{args.model}"

    if args.save:
        save_path = f"{args.save}" 

    if args.load:
        load_path = "."

    model = load_model(model_size)
    print(f"Loaded the Whisper AI {model_size} model.\n")

    result = transcribe_malayalam_to_english(model, audio_filename, load_path)             # Translate from Malayalam to English
    print("\n\nTranscribing Completed.\n")
  
    write_to_srt(result, audio_filename, save_path)                                        # Export results to an srt

    print("\n\nSuccessfully exported to a .srt file format.")                       # Message informing user of successful completion



