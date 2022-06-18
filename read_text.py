import os
import io
import streamlit as st
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="gcloud/secret.json"
# replace path "gcloud/secret.json" to your own file path where you saved your own file with the service account key.
from google.cloud import texttospeech

st.sidebar.title("Read your text!")

def synthesize_speech(text, lang='Japanese', gender='defalut'):
    gender_type = {
        'Unspecified': texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED,
        'male': texttospeech.SsmlVoiceGender.MALE,
        'female': texttospeech.SsmlVoiceGender.FEMALE,
        'neutral': texttospeech.SsmlVoiceGender.NEUTRAL
    }
    lang_code = {
        'Japanese':'ja-JP',
        'English-GB':'en-GB',
        'English-US':'en-US',
        'German':'de-DE',
        'Indonesian':'id-ID',
        'Mandarin-CN':'cmn-CN',
        'Mandarin-TW':'cmn-TW',
        'Korean':'ko-KR',
        'Malay':'ms-MY'
     }
# you can add more languages. Please refer to readme.md

    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=lang_code[lang], ssml_gender=gender_type[gender]
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return response
    

st.sidebar.markdown("### preparing your text data")

input_option = st.sidebar.selectbox(
    "How do you want to input your data?",
    ("Direct Input","Upload your textfile")
)

input_data = None

if input_option == "Direct Input":
    input_data = st.sidebar.text_area("Paste your text here. ","This is text sample for cloud text-to-speech")
else:
    uploaded_file = st.sidebar.file_uploader("Please upload your text file.",["txt"])
    if uploaded_file is not None:
        content = uploaded_file.read()
        input_data = content.decode()


if input_data is not None:
    st.write("===   your text   ===")
    st.write(input_data)
    st.write("===   end of text   ===")
    st.sidebar.markdown("### set your parameters")

    lang = st.sidebar.selectbox(
        "Select speaker's language",
        ('Japanese', 'English-GB', 'English-US', 'Mandarin-CN','Mandarin-TW', 'Korean','Indonesian','Malay')            
    )
    # You can add more languages but should be same as defined lang_code at line 18. 

    gender = st.sidebar.selectbox(
        "select speaker's gender",
    ("Unspecified","male","female","neutral")
    )

st.write("Once your text and prefered parameters are ready, ")
st.write("Press Start to generate the MP3 file.")
if st.button("Start"):
    comment = st.empty()
    comment.write("generating")
    response = synthesize_speech(input_data, lang=lang, gender=gender)
    st.audio(response.audio_content)
    comment.write("Voice data generated. Now you can play and download the voice data in MP3 format")





