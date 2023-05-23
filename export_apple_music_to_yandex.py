# -*- coding: utf-8 -*-

import re
import urllib.request

def get_text_from_url(url):
    response = urllib.request.urlopen(url)
    return response.read().decode()


def get_text_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def extract_song_titles(text):
    pattern1 = r'<div\s+class="songs-list-row__song-name\s+svelte-17mxcgw"\s+tabindex="-1"\s+role="checkbox"\s+dir="auto"\s+data-testid="track-title">(.*?)<\/div>'
    return re.findall(pattern1, text)


def extract_authors(text):
    pattern2 = r'<a\s+data-testid="click-action"\s+class="click-action\s+svelte-1nh012k"\s+href="([^"]*)">(.*?)<\/a>'
    return re.findall(pattern2, text)


def process_blocks(song_titles, authors):
    i = 0
    current_authors = []
    grouped_authors = []

    while i < len(authors):
        if not current_authors or authors[i][1] != current_authors[0]:
            current_authors.append(authors[i][1])
        elif authors[i][1] == current_authors[0]:
            grouped_authors.append(", ".join(current_authors))
            i += len(current_authors)
            current_authors = []

        i += 1

    return list(zip(song_titles, grouped_authors))

def get_user_input():
    mode = input("Input preferred mode of using from: \nFile\nUrl\n").lower()

    if "url" in mode:
        url = input("url: ")
        text = get_text_from_url(url)
    elif "file" in mode:
        filename = input("file name: ")
        text = get_text_from_file(filename)
    else:
        print("Sorry, don't know what way you want to use (")
        exit()

    return text


def print_results(results):
    for result in results:
        print(result)


def main():
    text = get_user_input()
    song_titles = extract_song_titles(text)
    authors = extract_authors(text)
    results = process_blocks(song_titles, authors)
    print_results(results)
    final_action = input("If you want to save results then type file name without extension or just click the Enter button\n")
    if len(final_action.strip()) == 0:
        return
    
    with open(final_action + ".txt", 'w', encoding='utf-8') as file:
        file.write("\n".join([str(i) for i in results]))

if __name__ == "__main__":
    main()
