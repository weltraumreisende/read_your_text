# read_your_text
This Python webapp using streamlit reads your text files in your preferred laguage.

The prerequisites 

To run this web app, you need to install streamlit and texttospeech google.cloud

to install streamlit
pip install streamlit 

to install Google Cloud text-to-speech
pip install google-cloud-texttospeech

To obtain Google Application Credentials:
Please refer to Google's document
https://cloud.google.com/docs/authentication/production#windows

Once you get the key and saved to your computer, set the path on your python program.
[line 4 of read_text.py]
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="gcloud/secret.json"

replace path "gcloud/secret.json" to your own file path and file name with your service account key.
 
The languages supported by Text-to-Speech are listed here:
https://cloud.google.com/text-to-speech/docs/voices

Please add your preferred languages to:
(1) lang_code  [line 17 of read_text.py]
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
     Left side is the list of languages. Right side is the language codes used by text-to-speech.
     For exasmple, if you would like to add Spanish (Spain), ad:
              'Spanish-ES':'es-ES'
     Note that you need to add ' ' to each languages, and add "," if not the last one in the list.

(2) lang [line 72 of read_text.py]
      lang = st.sidebar.selectbox(
        "Select speaker's language",
        ('Japanese', 'English-GB', 'English-US', 'Mandarin-CN','Mandarin-TW', 'Korean','Indonesian','Malay')            
    )
    Add the language name defined in the left side of the lang_code. For example, if you added Spanish-US to the list:  'Spanish-US':'es-US'
    Then add 'Spanish-US', NOT 'es-US'
    
(3) The Voice Names defined in the Supported voices and languages list are not used with this app. Therefore what you look for to define the language codes are the third column of the "Supported Voices and Languages list https://cloud.google.com/text-to-speech/docs/voices

