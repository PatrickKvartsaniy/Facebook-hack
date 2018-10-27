import sys
import os
import pipes

def video_to_audio(input_video,output_audio):
	try:
		file, file_extension = os.path.splitext(input_video)
		file = pipes.quote(file)
		# video_to_wav = 'ffmpeg -i ' + file + file_extension + ' ' + file + '.mp3'	
		video_to_wav = f'ffmpeg -i {input_video} -vn -acodec pcm_s16le -ar 44100 -ac 1 {output_audio}'
		# final_audio = 'lame '+ file + '.wav' + ' ' + file + '.wav'
		os.system(video_to_wav)
		# os.system(final_audio)
		#file=pipes.quote(file)
		#os.remove(file + '.wav')
		print("sucessfully converted ", input_video, " into audio!")
	except OSError as err:
		print(err.reason)
		exit(1)

def replace_audio(video_file, audio_file, video_output):
	video_to_wav = 'ffmpeg -i ' + video_file + ' -i ' + audio_file + ' -c:v copy -map 0:v:0 -map 1:a:0 ' + video_output
	os.system(video_to_wav)