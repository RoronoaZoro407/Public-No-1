import os
import re
from pytube import YouTube

# YouTube video URL
video_url = input("Enter the YouTube video URL: ")

try:
    # Creating YouTube object
    yt = YouTube(video_url)

    # Get the highest resolution video stream
    stream = yt.streams.get_highest_resolution()

    # Set the output directory
    output_directory = "D:/youtube download"

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Clean the video title to remove invalid characters
    cleaned_title = re.sub(r'[<>:"/\\|?*]', '', yt.title)

    # Set the output file path and name
    output_file = cleaned_title + ".mp4"

    # Download the video to the specified output directory
    stream.download(output_directory, output_file)
    print("Download completed successfully!")
except Exception as e:
    print(f"An error occurred while downloading the video: {str(e)}")
