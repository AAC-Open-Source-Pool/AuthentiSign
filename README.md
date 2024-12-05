# Team - 24AACL04
<b>Project name:</b>
<p> AuthentiSign</p>
<h2>Team Details</h2>
<b>Senior Mentor:</b><p> Manav</p>
<b>Junior Mentor:</b><p> Meghana Tallapalli</p>
<b>Members:</b>
<p> Hasini Banka</p>
<p> Jythraa Tota</p>
<p> Gundeboina Sameeksha</p>
<p> Gidugu Shanmukha Pavani Manishri</p>

<div align="center">
  <img src="[logo url](https://imgur.com/a/GZeJsc6)">

</div>
<p align="center">Abstract</p>
## Table of Contents

- [Introduction](#introduction) <br>
- [Requirements](#requirements) <br>
- [How to use](#installation-and-usage) <br>
- [Preview](#previews)
- [Contribution](#contribution)
## Requirements
|||
|--|--|
|[language version](url of the website)|<img src=" https://imgur.com/a/GZeJsc6 " width="130px" height="25px"></a><br>|

## Installation and usage
Step by step process of cloning the project, installments needed and how to use it







To run this project, you need the following tools and Python libraries installed:

Python Version:
- Python 3.8 or above
Required Libraries:
- OpenCV for image processing: opencv-python-headless
- Streamlit for UI: streamlit
- Scikit-Image for HOG feature extraction: scikit-image
- Scikit-Learn for similarity calculations: scikit-learn
- SciPy for correlation coefficients: scipy
- NumPy for numerical operations: numpy

Optional Tools:
- A virtual environment tool like venv or conda to manage dependencies.

Steps To Use the Signature Verification System
Follow these steps to use the application:

1. Start the Application
- Open your terminal or command prompt.
- Navigate to the project directory where the Python script is located.
- Run the Streamlit application:
 streamlit run <script_name>.py
- Replace <script_name> with the name of the Python file.

3. Enter Account Number
- Once the app is running, a user interface will appear in your browser.
- In the input field labeled "Enter Account Number", type the account number associated with the signature.

4. Capture an Image
- Click the "Capture Image" button to start the video stream from your configured IP camera.
- A live feed will appear in a separate window.
- Press the spacebar to capture an image of the signature.
- The captured image will be displayed on the Streamlit interface.

5. Verify the Signature
The application will:
- Check if the account number exists in the CSV file.
- If it’s a new account, the signature’s HOG features are saved.
- If it’s an existing account, the signature is compared against the stored HOG features using:
 -> Cosine Similarity
 -> Pearson Correlation
- The application displays results:
 -> "Signature is Original": If the similarity and correlation exceed the thresholds.
 -> "Signature is Forged": If thresholds are not met.

6. Logs and Feedback
- For new users, the app saves the HOG features and notifies that they are stored.
- For existing users, similarity scores and verification results are displayed on the interface.

7. Repeat as Needed
- You can verify multiple signatures by entering different account numbers and capturing their corresponding images.




