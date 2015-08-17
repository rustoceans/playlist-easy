import subprocess
import os
from os.path import expanduser

home = expanduser("~")


def make(playlist_name, url, extension):
    response_process = subprocess.Popen(
        ['python', 'youParse.py', url],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    resp, err = response_process.communicate()
    urls = resp.split()
    directory = "{home}/Downloads/youtube-dl/{playlist_name}/".format(
        playlist_name=playlist_name, home=home)
    for v_link in urls:
        if not os.path.exists(directory):
            os.makedirs(directory)
        if extension == 'mp3':
            command = 'youtube-dl -o "{directory}%(title)s-%(id)s.%(ext)s"\
            --extract-audio --audio-format --audio-quality  0 {extension}\
            {v_link}'.format(directory=directory, playlist_name=playlist_name, home=home, v_link=v_link, extension=extension)
        else:
            command = 'youtube-dl {v_link}'.format(v_link=v_link)
        print command
        os.system(command)


def main():
    playlist_name = raw_input('Enter with a playlist name: ')
    url = raw_input('Enter with playlist url: ')
    while True:
        extension = raw_input('Do you wanna mp3 or mp4 files? (mp3/mp4): ')
        if extension not in ['mp3', 'mp4']:
            print 'Enter with a valid format!'
        else:
            break
    make(playlist_name, url, extension)


if __name__ == "__main__":
    main()
