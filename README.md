# Export Apple Music Playlist to Yandex Music

This script allows you to export a playlist from Apple Music and convert it to a format compatible with Yandex Music for easy import. It extracts the song titles and authors from the Apple Music playlist and saves them to a text file that can be used to import the playlist into Yandex Music using the [Yandex Music Import Tool](https://music.yandex.ru/import/).

## Prerequisites

- Python 3.x installed on your system.
- Internet connectivity to access Apple Music and Yandex Music websites.

## Installation

1. Download the script file (`export_apple_music_to_yandex.py`) to your computer.

## Usage

1. Open a terminal or command prompt and navigate to the directory where the script file is located.

2. Run the following command to execute the script:

```
python export_apple_music_to_yandex.py
```

3. You will be prompted to select the mode of input: either "File" or "URL".

- If you choose "File", you need to provide the path to a text file containing the HTML source code of the Apple Music playlist.
- If you choose "URL", you need to provide the URL of the Apple Music playlist.

4. Once the script processes the input, it will display the extracted song titles and authors.

5. If you want to save the results to a file, enter the desired file name (without the extension) when prompted. If you don't want to save the results, simply press Enter.

6. If you entered a file name, a text file (`filename.txt`) will be created in the same directory, containing the playlist information in the format: "song title - artist".

7. Visit the [Yandex Music Import Tool](https://music.yandex.ru/import/) and follow the instructions to import the playlist. Choose the created text file (`filename.txt`) when prompted.

8. Enjoy your imported playlist on Yandex Music!

Note: Ensure that you have a valid Apple Music playlist URL or HTML source code file for proper functioning of the script.

## Troubleshooting

- If you encounter any issues or errors, make sure you have a stable internet connection and check that the provided Apple Music playlist URL or file is valid.

- If the imported playlist in Yandex Music doesn't match the expected results, ensure that the Apple Music playlist's HTML structure hasn't changed, as it may affect the extraction process.

- For any other problems or questions, feel free to contact the script author.

## Disclaimer

This script is provided as-is, without any warranty. Use it at your own risk. The script author is not responsible for any misuse or any consequences resulting from the use of this script.

Please ensure that you comply with the terms and conditions of Apple Music and Yandex Music while using this script.

**Note:** This script is not affiliated with or endorsed by Apple Music or Yandex Music. It is an independent project created to facilitate playlist export between the two platforms.
