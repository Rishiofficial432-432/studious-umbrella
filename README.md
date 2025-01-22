
# Jarvis A.I - Voice Controlled AI Assistant

## Project Overview

Jarvis A.I is a command-line based personal AI assistant designed to run on Chrome OS Flex. It leverages the power of Google's Gemini API for natural language processing and AI-related tasks, allowing for interactive chat and prompt-based AI generation. This project is built using Python and incorporates the `speech_recognition` library for voice input, allowing for hands-free interaction. The assistant uses `espeak` for text-to-speech output, making it a fully functional voice-driven tool.

## Key Features

*   **Voice-Activated Interaction:** Uses the `speech_recognition` library to process voice commands, allowing for seamless hands-free control.
*   **Gemini API Integration:** Employs the Google Gemini API for both conversational chat and general AI prompt processing, providing powerful language capabilities.
*   **Command-Line Interface:** Uses the command line, and can run on your terminal.
*   **Text-to-Speech Output:** Provides audio feedback using the `espeak` text-to-speech engine, making the interactions more conversational.
*   **Web Browsing Control:** Supports basic web browsing commands, such as opening specified websites.
*   **Music Playback:** Enables playing local music files through voice commands.
*  **Basic AI Prompt Interaction:** Has the ability to use Gemini's AI by simply saying 'using artificial intelligence'.
*   **Optimized for Chrome OS Flex:** Developed and tested to run effectively on Chrome OS Flex, a lightweight and flexible operating system.

## Prerequisites

Before you can run Jarvis A.I, ensure you have the following installed and configured:

*   **Python 3.7+:** This project is built using Python, so you need a suitable installation.
*   **pip:** The Python package installer.
*   **Google Gemini API Key:** You'll need an API key from Google AI Studio.
*   **Required Python Libraries:**
    *   `speechrecognition`
    *   `google-generativeai`
    *   `numpy`
    *   `pyaudio`
*   **espeak:** A text-to-speech engine for Linux systems.

## Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Rishiofficial432-432/studious-umbrella.git
    ```
2.  **Navigate to the Project Directory:**
    ```bash
    cd studious-umbrella
    ```
3.  **Install Python Libraries:**
   ```bash
       pip install -r requirements.txt
    ```
4.  **Install `espeak`**
  ```bash
      sudo apt install espeak
content_copy
download
Use code with caution.
Markdown
Configuration

Set Google Gemini API Key: You must set the Google Gemini API Key by setting the environment variable GOOGLE_API_KEY. Otherwise replace the YOUR_API_KEY_HERE text with your key directly in the main.py file.

Get Microphone Index:

Run arecord -l in your terminal to list your audio devices.

Note the device information and test that device using arecord -d 5 test.wav -D <device id>.

If aplay test.wav works set the microphone_device_index with that device.

Set the microphone_device_index variable in main.py to the appropriate device ID you want to use.

Set the PA_ALSA_PLUGHW variable: The code will set the PA_ALSA_PLUGHW variable, but if there are any issues you can also set this manually with export PA_ALSA_PLUGHW=1

How to Run

Make main.py executable:

chmod +x main.py
content_copy
download
Use code with caution.
Bash

Run the script:

python3 main.py
content_copy
download
Use code with caution.
Bash
Example Usage

Open a website: "Open youtube"

Ask for the current time: "What is the time"

Start a chat: "hello how are you"

Use AI generation: "Using artificial intelligence, generate a short story about cats"

Troubleshooting

If you run into audio issues:

Run python3 main.py and note the output of the pyaudio device listing.

Use arecord to test the device.

Set the microphone_device_index variable correctly.

Make sure you have pyaudio and espeak installed correctly.

Contributing

Contributions to Jarvis A.I are always welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

License

This project is licensed under the MIT License (or specify the license you're using).

