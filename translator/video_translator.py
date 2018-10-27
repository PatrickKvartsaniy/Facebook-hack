from .processing_file import video_to_audio, replace_audio
from .processing_audio import synthesize_text, create_audio
from .translate import translate, translate_transcript
from .transcript import voice_to_text

def translate_video(video):
	src = 'en'
	trg = 'ru'
	sup_voice =  'ru'
	sup_lang = 'en-US'
	audio_file_name = 'output.wav'
	in_name = "videoplayback.mp4"
	out_name = "translated_video.mp4"
	video_to_audio(video,audio_file_name)
	# Instantiates a client
	result = voice_to_text(audio_file_name, sup_lang)
	# print(result)
	speech = translate_transcript(result, src, trg)
	# print(speech)
	for i,_speech in enumerate(speech):
		synthesize_text(_speech['alternative'], sup_voice ,'output' + str(i) + '.mp3')

	create_audio(speech, 'whole_audio.wav')

	replace_audio(in_name, "whole_audio.wav", out_name)

	return out_name
# print(speech)