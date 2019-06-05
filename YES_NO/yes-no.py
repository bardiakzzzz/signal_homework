#!/usr/bin/env python3
from scipy.io import wavfile as wav
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

FORMAT = pyaudio.paInt16  # format of sampling 16 bit int
CHANNELS = 1  # number of channels it means number of sample in every sampling
RATE = 44100  # number of sample in 1 second sampling
CHUNK = 1024  # length of every chunk
RECORD_SECONDS = 1.5  # time of recording in seconds
WAVE_OUTPUT_FILENAME = "file.wav"  # file name

x = 1
while True:
    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("recording number ", x, " ...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # find function

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # storing voice
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    # reading voice
    rate, data = wav.read('file.wav')

    # my code
    # data is voice signal. its type is list(or numpy array)
    function = np.fft.fft(data)

    for j in range(int(len(function) / 2), len(function)):
        function[j] = 0  # change half of it to zero

    function_to_list = []
    for i in function:
        function_to_list.append(abs(i))

    function = function_to_list[0:10000]

    if np.mean(function[2900:3600]) > 60000 and np.mean(function[1500:2400]) < 1300000:
        print("YES\n")
    elif np.mean(function[1000:2000]) > 150000:
        print("NO\n")
    elif np.mean(function[2000:4000]) < 20000:
        print("Null\n")
    x += 1
