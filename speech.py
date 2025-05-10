import streamlit as st
from gtts import gTTS
import os
import tempfile
import base64

# Streamlit page setup
st.set_page_config(page_title="🗣️ Text-to-Speech App", page_icon="🗣️")
st.title("🗣️ Text-to-Speech Generator")
st.markdown("Convert your text into spoken audio using gTTS (Google Text-to-Speech).")

# Input for the text to be spoken
text_input = st.text_area("Enter the text to convert to speech", height=200)

# Language selection
language = st.selectbox("Select language", ["en", "es", "fr", "de", "hi", "ta", "te"])

# Generate speech on button click
if st.button("🔊 Generate Speech"):
    if text_input.strip():
        try:
            # Create TTS object
            tts = gTTS(text=text_input, lang=language)
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(temp_file.name)

            # Read audio file for playback and download
            audio_bytes = open(temp_file.name, 'rb').read()
            b64_audio = base64.b64encode(audio_bytes).decode()

            st.audio(audio_bytes, format="audio/mp3")
            href = f'<a href="data:audio/mp3;base64,{b64_audio}" download="speech.mp3">📥 Download MP3</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.success("✅ Speech generated successfully!")
        except Exception as e:
            st.error(f"❌ Error generating speech: {str(e)}")
    else:
        st.warning("⚠️ Please enter some text before generating speech.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit and gTTS")
