from pydub import AudioSegment
import time

queue = [
    'dark',
    'day1',
    ['countdown', 10],
    'day2',
    ['countdown', 10],
    'day3',
    ['countdown', 10],
    'day4',
    ['countdown', 10],
    'day5',
    ['countdown', 10],
    'day6',
    ['countdown', 10],
    'select',
    ['countdown', 6],
    'communicate',
    ['countdown', 10],
    'end'
]


def add_pause(duration_ms):
    return AudioSegment.silent(duration=duration_ms)


def create_countdown(start):
    countdown_audio = AudioSegment.empty()
    for i in range(start, 0, -1):
        countdown_audio += AudioSegment.from_mp3(f'./audio/{i}.mp3')
        countdown_audio += add_pause(500)
    return countdown_audio


def process_queue():
    audio = AudioSegment.empty()

    for step in queue:
        if isinstance(step, list) and step[0] == 'countdown':
            countdown_audio = create_countdown(step[1])
            audio += countdown_audio
        else:
            audio += AudioSegment.from_mp3(f'./audio/{step}.mp3')

        audio += add_pause(2000)

    return audio


final_audio = process_queue()

final_audio.export("audio.mp3", format="mp3")
