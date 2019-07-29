def transcribe(podcast_name, episod):
    get_mp3_file(podcast_name, episod)
    print('transcription for podcast %s for episod %s is: ' % (podcast_name, episod))


def get_mp3_file(podcast_name, episod):
    print('getting mp3 file of podcast %s episod %s...' % (podcast_name, episod))


if __name__ == '__main__':
    transcribe('ink', 1)
