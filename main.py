from moviepy.editor import * 

#Apro il file video di mio interesse 
video = VideoFileClip("C:/Users/marco.chianese/repo/Python/mp3converter/prova.mp4")


#Specifico estraggo l'audio con il mentodo .audio e con il metodo .write_audiofile specifico dove deve essere salvato 
video.audio.write_audiofile("tuo_audio.mp3")
