import subprocess
import os


def make(url, extension):
    response_process = subprocess.Popen(
        ['python', 'youParse.py', url],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    resp, err = response_process.communicate()
    urls = resp.split()
    for v_link in urls:
        if extension == 'mp3':
            command = 'youtube-dl --extract-audio --audio-format {extension}\
            {v_link}'.format(
                v_link=v_link, extension=extension)
        else:
            command = 'youtube-dl {v_link}'.format(v_link=v_link)
        os.system(command)


def main():
    url = raw_input('Enter with playlist url: ')
    while True:
        extension = raw_input('Do you wanna mp3 or mp4 files? (mp3/mp4): ')
        if not extension in ['mp3', 'mp4']:
            print 'Enter with a valid format!'
        else:
            break
    make(url, extension)


if __name__ == "__main__":
    main()
