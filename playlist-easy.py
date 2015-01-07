import subprocess
import os


def make(url):
    response_process = subprocess.Popen(
        ['python', 'youParse.py', url],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    resp, err = response_process.communicate()
    for v_link in resp.split():
        os.system(
            'youtube-dl --extract-audio --audio-format mp3 {v_link}'.format(
                v_link=v_link))


def main():
    url = raw_input('Enter with playlist url: ')
    make(url)


if __name__ == "__main__":
    main()
