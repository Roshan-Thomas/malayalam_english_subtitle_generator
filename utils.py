# Author: Roshan Thomas

def transcribe_malayalam_to_english(model, audio_filename: str, load_path: str):
    import os

    # Check if load_path folder exists, if not, create the folder
    filePathExist = os.path.exists(load_path)
    if not filePathExist:
        print(f"{load_path} does not exist. Creating folder....")
        os.makedirs(load_path)
        print(f"{load_path} folder created!")

    return model.transcribe(
            audio=f"{load_path}/{audio_filename}", 
            task='translate', 
            language='Malayalam', 
            verbose=True, 
            condition_on_previous_text=True, 
            fp16=False,
        )

def format_timestamp(seconds: float, always_include_hours: bool = False, decimal_marker: str = '.'):
    assert seconds >= 0, "non-negative timestamp expected"
    milliseconds = round(seconds * 1000.0)

    hours = milliseconds // 3_600_000
    milliseconds -= hours * 3_600_000

    minutes = milliseconds // 60_000
    milliseconds -= minutes * 60_000

    seconds = milliseconds // 1_000
    milliseconds -= seconds * 1_000

    hours_marker = f"{hours:02d}:" if always_include_hours or hours > 0 else ""
    return f"{hours_marker}{minutes:02d}:{seconds:02d}{decimal_marker}{milliseconds:03d}"

def write_to_srt(result: dict, audio_filename: str, save_path: str):
    import os

    # Check if save_path folder exists, if not, create the folder
    filePathExist = os.path.exists(save_path)
    if not filePathExist:
        print(f"{save_path} does not exist. Creating folder....")
        os.makedirs(save_path)
        print(f"{save_path} folder created!")

    with open(f"{save_path}/{audio_filename}_transcribed_Export.srt", 'w', encoding="utf-8") as srt:
        for i, segment in enumerate(result["segments"], start=1):
            # write srt lines
            srt.write(
                f"{i}\n"
                f"{format_timestamp(segment['start'], always_include_hours=True, decimal_marker=',')} --> "
                f"{format_timestamp(segment['end'], always_include_hours=True, decimal_marker=',')}\n"
                f"{segment['text'].strip().replace('-->', '->')}\n\n",
            )