# STranslator

STranslator is GUI application based on Python 3.8

  - Translate your text to another language
  - Voice input and playback of text
  - Save all your translations to your history and add them to your favorites
  - Automatically add voice synthesizers to the program
  - Import and save to files translations

### Tech

STranslator uses a number of python libraries:

* **Googletrans** - translates your text
* **Pyttsx3 (2.71)** - playback of text
* **Speech Recognition** - voice input
* **Sqlite3** - working with the database
* **PyQt5** - GUI application

### Installation

STranslator requires [Python](https://www.python.org/downloads/release/python-380/) 3.8 to run.


```sh
pip install googletrans
pip install pyttsx3==2.71
pip install SpeechRecognition
pip install PyQt5
```

For **Speech Recognition** you aslo should install **PyAudio**:
Download from [this site](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) file *PyAudio‑0.2.11‑cp38‑cp38‑win_amd64.whl*, where cp38 indicates the version of python3.8.x, and amd64 indicates the corresponding bit depth

**Then**:
 
```sh
cd <folder with the pyaudio.whl package>
pip install name_of_installed_file.whl
```
