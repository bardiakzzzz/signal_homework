#!/usr/bin/env python3
from scipy.io import wavfile as wav
import pyaudio
import wave
import numpy as np
import scipy.fftpack
from scipy.fftpack import fft, ifft


FORMAT = pyaudio.paInt16 # format of sampling 16 bit int
CHANNELS = 1 # number of channels it means number of sample in every sampling
RATE = 44100 # number of sample in 1 second sampling
CHUNK = 1024 # length of every chunk
RECORD_SECONDS = 1 # time of recording in seconds
WAVE_OUTPUT_FILENAME = "file.wav" # file name


    
for i in range(10):
    audio = pyaudio.PyAudio()
 
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
    print("recording...")
    frames = []
 
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished recording")
 

    #find function

 
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

    #reading voice
    rate, data = wav.read('file.wav')

    #my code
    # data is voice signal. its type is list(or numpy array)
    function = np.fft.fft(data)


    for j in range(int(len(function) /2) ,len(function)):
        function[j]=0    #change half of it to zero

    function_to_list=[]
    for i in function:
        function_to_list.append(abs(i))
   
    max1 = max(function_to_list)
    index_max1=function_to_list.index(max1)  #find first max
   
    for k in range(index_max1 - 20, index_max1+20):
        function_to_list[k] = 0   #change neighbors of max to zero

    max2 = max(function_to_list)
    index_max2 = function_to_list.index(max2)  #find second max
    

    first = index_max2
    second = index_max1

    #finding numbers
    if (first > 1205 and first < 1211):
        if (second >695 and second < 702):
            print ("number 1")
        if (second >766 and second < 774):
            print ("number 4")
        if (second >848 and second < 856):
            print ("number 7")
        if (second >937 and second < 945):
            print ("number *")
    elif (first > 1332 and first < 1340):
        if (second >695 and second < 700):
            print ("number 2")
        if (second >764 and second < 774):
            print ("number 5")
        if (second >848 and second < 856):
            print ("number 8")
        if (second >937 and second < 945):
            print ("number 0")
    elif (first > 1473 and first < 1481):
        if (second >695 and second < 700):
            print ("number 3")
        if (second >766 and second < 774):
            print ("number 6")
        if (second >848 and second < 856):
            print ("number 9")
        if (second >937 and second < 945):
            print ("number #")
    elif (first > 1631 and first < 1639):
        if (second >695 and second < 700):
            print ("A")
        if (second >766 and second < 774):
            print ("B")
        if (second >846 and second < 856):
            print ("C")
        if (second >937 and second < 945):
            print ("D")
    else:
        print("nothing found")
    

    
