import streamlit as st
import speech_recognition as sr

def main():
    st.title("Speech to Text Converter")

    # File uploader
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav')

        # Convert speech to text
        recognizer = sr.Recognizer()
        audio_data = None

        try:
            with sr.AudioFile(uploaded_file) as source:
                audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            st.write("Transcription:")
            st.write(text)
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
