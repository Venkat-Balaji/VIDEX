# Video Description AI with Jina

This repository contains code for utilizing Jina AI to describe the content of videos using various algorithms. The script sends a video to the Jina AI API for processing and waits for the results. The summary of the video content is then saved to a text file.

## Features

- **Video Description:** Utilize Jina AI to generate a textual summary of the content of a given video.
  
- **Text-to-Speech Conversion:** Convert the generated text summary to speech using a text-to-speech (TTS) engine.

- **Language Translation:** Translate the generated text summary into different languages using machine translation.

## Getting Started

### Prerequisites

- Python 3.x
- [Jina AI](https://github.com/jina-ai/jina) installed. Follow the [official installation guide](https://docs.jina.ai/chapters/firststeps/install/) for instructions.

### Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/mrnithish/Videx-Video-Summarizer.git
cd your-repository
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Usage
Obtain API Key

Obtain an API key from Jina AI. Replace YOUR_GENERATED_SECRET in the script with your actual API key.

Run the Script

Execute the script to send a video for processing:

bash
Copy code
python video_description.py
Text-to-Speech and Language Translation (Optional)

Uncomment the relevant sections in the script (text_to_speech.py and language_translation.py) to enable text-to-speech conversion and language translation.

bash
Copy code
# Uncomment the following lines to enable text-to-speech conversion
# python text_to_speech.py

# Uncomment the following lines to enable language translation
# python language_translation.py
Check Results

The script will print the raw response data, save the video summary to summary.txt, and generate additional outputs based on enabled features.

Configuration
Modify the data dictionary in the script to process different videos with specific algorithms and languages.
Important Note
Ensure that your API key is kept confidential. Do not share it publicly.
Contributing
Feel free to contribute by opening issues or submitting pull requests. We welcome any improvements or bug fixes.

License
This project is licensed under the MIT License - see the LICENSE file for details.
