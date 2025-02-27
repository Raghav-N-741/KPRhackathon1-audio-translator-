import gradio as gr
from backend import download_youtube_audio, speech_to_text, translate_text, text_to_speech

def process_youtube_audio(video_url, target_lang):
    try:
        audio_file = download_youtube_audio(video_url)
        extracted_text = speech_to_text(audio_file)

        translated_text = translate_text(extracted_text, target_lang)
        translated_audio_file = text_to_speech(translated_text, target_lang)

        return extracted_text, translated_text, translated_audio_file
    except Exception as e:
        return f"Error: {str(e)}", "", ""

# Define Gradio Interface
iface = gr.Interface(
    fn=process_youtube_audio,
    inputs=[
        "text",
        gr.Dropdown(["Tamil", "English", "Hindi"], label="Select Language")
    ],
    outputs=["text", "text", "audio"],
    title="YouTube Audio Translator",
    description="Enter a YouTube video URL, select Tamil, English, or Hindi, and get translated audio."
)

# Launch Gradio App
iface.launch(share=True)
