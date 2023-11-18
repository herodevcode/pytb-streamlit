import os
import pytube
import streamlit as st

def download_video(url, output_path):
    yt = pytube.YouTube(url)
    video = yt.streams.get_highest_resolution()
    output_file = os.path.join(output_path, video.default_filename)
    video.download(output_path=output_path) 
    return output_file

if __name__ == '__main__':
    st.title("YouTube Video Downloader")
    url = st.text_input('YouTube URL')

    if url:
        # Button to start the download
        if st.button('Download Video'):
            output_path = 'videos'
            os.makedirs(output_path, exist_ok=True)
            filepath = download_video(url, output_path)

            with open(filepath, 'rb') as f:
                st.download_button(
                    label='Download video',
                    data=f,
                    file_name=os.path.basename(filepath),
                    mime='video/mp4')