# Malayalam to English Automatic Subtitle Generation

## Setup (First Run)

1. Install OpenAI's Whisper on your local computer via Python's package manager `pip`.
    ```bash
    pip install -U openai-whisper
    ```

2. Whisper requires you to have `ffmpeg` installed on your system, which is available from most package managers.
    ```bash
    # on Ubuntu or Debian
    sudo apt update && sudo apt install ffmpeg

    # on Arch Linux
    sudo pacman -S ffmpeg

    # on MacOS using Homebrew (https://brew.sh/)
    brew install ffmpeg

    # on Windows using Chocolatey (https://chocolatey.org/)
    choco install ffmpeg

    # on Windows using Scoop (https://scoop.sh/)
    scoop install ffmpeg
    ```

3. You will require `setuptools-rust` as well (to avoid unecssary errors).
    ```
    pip install setuptools-rust
    ```

## Command-Line Usage

1. Clone the git repo to your system via command-line or by downloading the .zip file (at the top of this page).
    ```bash
    git clone https://github.com/Roshan-Thomas/malayalam_english_subtitle_generator.git

    ```

2. Change directory to newly downloaded folder
    ```bash
    cd malayalam_english_subtitle_generator
    ```

3. Run the following command to generate subtitles for a sample audio file 'sample.wav'.
    ```bash
    python translate_message_to_srt.py -a "sample.wav" 

    # Or, you can run the following
    python translate_message_to_srt.py --audio "sample.wav"
    ```

### Optional Commands
1. To specify a custom Whisper model, use the `-m` or `--model` argument
    ```bash
    python translate_message_to_srt.py -a "sample.wav" -m large

    # Or you can use the following
    python translate_message_to_srt.py -a "sample.wav" --model large
    ```

2. To specify a custom save location for the generated `.srt` files, use the `-s` or `--save` argument
    ```bash
    python translate_message_to_srt.py -a "sample.wav" -s save_location_file_path

    # Or, you can use the following
    python translate_message_to_srt.py -a "sample.wav" --save save_location_file_path
    ```

3. To specify a custom load location for your audio (.wav or .mp3) file, use the `-l` or `--load` argument
    ```bash
    python translate_message_to_srt.py -a "sample.wav" -l load_location_file_path

    # Or, you can use the following
    python translate_message_to_srt.py -a "sample.wav" --load load_location_file_path
    ```

4. Command which uses all the above optional arguments 
    ```bash
    python translate_message_to_srt.py -a "sample.wav" -l audios -s srt_files -m large
    ```