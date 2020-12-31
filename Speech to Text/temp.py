import argparse
import io
from google.oauth2 import service_account
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types  

credentials = service_account.Credentials.from_service_account_file('video-dialogue-22aac9d80bde.json')

def transcribe_file_with_word_time_offsets(speech_file,language):
    """Transcribe the given audio file synchronously and output the word time
    offsets."""
    print("Start")
    print("checking credentials")
      
    client = speech.SpeechClient(credentials=credentials)
    
    print("Checked")
    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()
              
    print("audio file read")    
    
    audio = types.RecognitionAudio(content=content)
    
    print("config start")
    config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
            language_code=language,
            enable_word_time_offsets=True)
    
    print("Recognizing:")
    response = client.recognize(config, audio) 
    print("Recognized")

    for result in response.results:
        alternative = result.alternatives[0]
        print('Transcript: {}'.format(alternative.transcript))

        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time
            print('Word: {}, start_time: {}, end_time: {}'.format(
                word,
                start_time.seconds + start_time.nanos * 1e-9,
                end_time.seconds + end_time.nanos * 1e-9))



transcribe_file_with_word_time_offsets("abc.flac","en-US")