import spotipy
from spotipy.oauth2 import SpotifyOAuth
import keras
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import os

# Spotify API credentials
client_id = 'bc14696682fb46d3a891e4dd724b9b59'
client_secret = '44f96128d98e49648a6d383befc042ff'
redirect_uri = 'http://localhost:3000'

# Function to transform an image for processing with a CNN model
def transform_image_for_cnn(image_path):
    """Transforms an image to a format suitable for CNN input.

    Opens the image, converts it to grayscale, resizes it to 48x48,
    and adds a channel dimension.

    Args:
        image_path (str): The path to the image file.

    Returns:
        numpy.ndarray: The transformed image as a numpy array.
    """
    with Image.open(image_path) as img:
        grayscale_img = img.convert("L")
        resized_img = grayscale_img.resize((48, 48))
        img_array = np.array(resized_img)
        img_array = np.expand_dims(img_array, axis=(0, -1))
    return img_array

# Load the trained CNN model
model = load_model('model.keras')

def predict_image(model, image_path):
    """Predicts the class of an image using the CNN model.

    Args:
        model: The loaded CNN model.
        image_path (str): The path to the image file.

    Returns:
        int: The predicted class index.
    """
    img_array = transform_image_for_cnn(image_path)
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=-1)
    return predicted_class

# Emotion class names
class_names = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']

# Define the scope for Spotify API
scope = 'user-library-read user-top-read playlist-modify-public user-follow-read user-modify-playback-state user-read-playback-state'

# Spotify username
username = "mepstick"

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope,
                                               cache_path='.spotify_cache'))

# Flask application setup
app = Flask(__name__)
CORS(app)

# Dictionary to store user's playlists for different moods
user_playlists = {}
emotion = "happy"

@app.route('/playlists', methods=['POST'])
def save_playlists():
    """Route to save user's playlists for different moods.

    Receives a JSON payload with playlist IDs and updates the user_playlists dictionary.

    Returns:
        json: A success message.
    """
    data = request.json
    user_playlists.update(data)
    print("Playlists updated:", user_playlists)
    return jsonify({'message': 'Playlists saved successfully!'})

@app.route('/capture', methods=['POST'])
def capture():
    """Route to capture and process an image.

    Receives an image, saves it, and processes it to predict the current emotion.

    Returns:
        json: A success message.
    """
    data = request.json['image']
    header, encoded = data.split(",", 1)
    data = base64.b64decode(encoded)
    
    if not os.path.exists('captures'):
        os.makedirs('captures')
    
    filename = "testcapture.jpg"
    filepath = os.path.join('captures', filename)

    with open(filepath, 'wb') as file:
        file.write(data)
    emotion = class_names[predict_image(model, filepath)[0]]
    return jsonify({'message': 'Image captured successfully!'})

@app.route('/play_playlist', methods=['GET'])
def trigger_play_playlist():
    """Route to play a Spotify playlist based on the current emotion.

    Returns:
        json: A message indicating which playlist is being played.
    """
    current_emotion = emotion
    play_playlist(current_emotion)
    return jsonify({'message': f'Playlist for {current_emotion} is now playing'})

def play_playlist(emotion):
    """Starts playing a Spotify playlist based on the provided emotion.

    Args:
        emotion (str): The current emotion.
    """
    playlist_id = user_playlists.get(emotion)
    if playlist_id:
        sp.start_playback(context_uri=f'spotify:playlist:{playlist_id}')
    else:
        print(f"No playlist for emotion: {emotion}")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)