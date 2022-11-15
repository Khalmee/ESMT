#import ffmpy
import os

#https://r2northstar.readthedocs.io/en/latest/guides/soundmodding.html

def handleAudioFileMP3(filePath, outputPath): #convert and create
    os.system("ffmpeg -i "+filePath+" -vn -c:a pcm_s16le  -ar 48000 "+outputPath+".temp.wav") #konwersja
    os.system("ffmpeg -i "+ outputPath+".temp.wav" +" -map 0 -map_metadata -1 -c:v copy -c:a copy "+ outputPath)#dodać f na początku?
    os.remove(outputPath+".temp.wav")

    #ff = ffmpy.FFmpeg(
    #    executable='C:\\ffmpeg\\ffmpeg\\bin\\ffmpeg.exe',
    #    inputs = {filePath:None},#'-f s16le'
    #    outputs = {outputPath:'-ar 48000'}#-c copy -fflags +bitexact -flags:v +bitexact -flags:a +bitexact
    #)
    #ff.run()

def handleAudioFileWAV(filePath, outputPath): #convert and create
    os.system("ffmpeg -i " + filePath + " -acodec pcm_s16le -ar 48000 " + outputPath+".temp.wav")
    os.system("ffmpeg -i "+ outputPath+".temp.wav" +" -map 0 -map_metadata -1 -c:v copy -c:a copy "+ outputPath)
    os.remove(outputPath+".temp.wav")


#script_ui EmitUISound("sound_name")

#spaces break file paths