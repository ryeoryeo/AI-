from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr

'''
from gtts import gTTS
from playsound import playsound
import tempfile
'''

r = sr.Recognizer()

# 1.메뉴를 말씀해주세요.
# 음성 파일 경로
audio_file = "./menu.wav"

# 음성 파일 로드
sound = AudioSegment.from_wav(audio_file)

# 음성 파일 재생
play(sound)

# 2.선택된 메뉴 결정, 음성인식
# 마이크로폰으로부터 음성 입력 받기
with sr.Microphone() as source:
    print("메뉴를 말씀해주세요...")
    audio = r.listen(source)

# 음성을 텍스트로 변환하기
try:
    text = r.recognize_google(audio, language='ko-KR')
    print("인식된 텍스트:", text)
except sr.UnknownValueError:
    print("음성을 인식할 수 없습니다.")
except sr.RequestError:
    print("음성 인식 서비스에 접근할 수 없습니다.")

'''
#텍스트를 음성으로 재생 (파일 권한문제로 삭제)
#TTS 엔진을 사용하여 텍스트를 음성으로 변환
tts = gTTS(text, lang='ko')

#임시 파일에 음성을 저장
with tempfile.NamedTemporaryFile(dir='.', delete=True) as fp:
   tts.save(fp.name)
   fp.flush()

    음성 파일 재생
    playsound(fp.name)
'''

# 3.메뉴결정
# 음성 파일 경로
audio_file2 = "./menu2.wav"

# 음성 파일 로드
sound = AudioSegment.from_wav(audio_file2)

# 음성 파일 재생
play(sound)
