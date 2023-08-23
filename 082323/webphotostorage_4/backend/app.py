from flask import Flask, jsonify, send_from_directory
import os
import glob

app = Flask(__name__)

@app.route('/get_data')
def get_data():
    # Use glob to get the list of all .png images in the stored_photos directory
    images = glob.glob('./stored_photos/*.png')
    # Return only the filenames, not the whole path
    image_names = [os.path.basename(image) for image in images]
    return jsonify({'list': image_names})

@app.route('/stored_photos/<filename>', methods=['GET'])
def serve_image(filename):
    #Endpoint to serve the images.
    return send_from_directory('stored_photos', filename)

if __name__ == '__main__':
    app.run(debug=True)