from flask import Flask, request, jsonify, render_template, send_file
import os
import re
from pytube import YouTube

app = Flask(__name__)

app.debug = True
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.json.get('url')

    try:
        # Validate the input URL
        if not video_url:
            return jsonify({'error': 'Invalid URL'}), 400

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

        # Set the output file path and name using f-strings
        output_file = f"{cleaned_title}.mp4"

        # Specify the complete output file path
        output_path = os.path.join(output_directory, output_file)

        # Download the video to the specified output path
        stream.download(output_directory, filename=output_file)

        # Send the file to the client
        return send_file(output_path, as_attachment=True, attachment_filename=output_file)

    except KeyError:
        return jsonify({'error': 'Invalid URL'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()

