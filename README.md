# VibeVisionAI (Facial Expression Recognition and Automatic Song Player)

**Overview**:
This project is an innovative blend of machine learning, web development, and music streaming. It employs a Convolutional Neural Network (CNN) to detect facial expressions through a webcam interface and interacts with the Spotify API to play music playlists corresponding to the detected emotion in real time. The project is structured into two main components: a frontend web application for user interaction and a backend server for processing and API interactions.

**Features**:
Facial Expression Recognition: Utilizes a trained CNN model to detect and classify facial expressions into categories such as angry, happy, sad, etc.

Dynamic Playlist Selection: Based on the detected emotion, the application selects a Spotify playlist that resonates with the user's current mood.

Webcam Integration: The frontend web application captures real-time video from the user’s webcam for emotion detection.

Spotify API Integration: Controls music playback by communicating with the Spotify API, offering a personalized music experience.

User Customization: Users can input their preferred Spotify playlists for each emotion, enhancing the personalization of the experience.


**Frontend**:
The frontend is a web-based interface designed for user interaction and capturing facial expressions via webcam. It's built with HTML, CSS, and JavaScript, offering a clean and user-friendly layout. Users can input their Spotify playlist IDs for different emotions, and the interface displays the webcam feed for real-time emotion detection.

**Backend**:
The backend server, built with Flask, serves as the bridge between the frontend, CNN model, and Spotify API. It processes images captured from the frontend, uses the CNN model to detect emotions, and communicates with Spotify to control music playback based on the detected emotion.

**CNN Model**:
The core of emotion detection is a CNN model trained to classify facial expressions. This model processes images from the webcam, identifies facial features, and classifies the expression into predefined categories.

**Spotify Integration**:
By leveraging the Spotify API, the project controls music playback, including selecting and playing playlists. The integration is designed to respond to the emotional cues detected by the CNN model, creating a responsive and immersive musical experience.

**Getting Started**:
To run this project, you will need:
Python 3.x
Flask and its dependencies
Spotify API credentials (Client ID, Client Secret)
A trained CNN model file (model.keras)

**Installation**:
Clone the repository.
Install the required Python packages: pip install flask keras tensorflow pillow spotipy.
Place your trained CNN model file in the project directory.
Set up your Spotify Developer account and obtain your Client ID and Client Secret.

**Running the Application**:
Start the Flask server by running the Python script.
Open the frontend HTML file in a web browser.
Input your Spotify playlist IDs in the web interface.
Allow webcam access and interact with the application.

**Future Enhancements**:
Improve the CNN model's accuracy and efficiency.
Expand the range of detectable emotions for a more comprehensive music selection.
Implement user accounts for personalized settings and history tracking.
Integrate additional streaming services beyond Spotify.

**Contributing**:
Contributions to this project are welcome. Please ensure to follow best coding practices and maintain the existing coding style.

**License**:
This project is licensed under the MIT License.
