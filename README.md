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
|[3.11.9](https://www.python.org/downloads/release/python-3119/)|<img src=" (https://imgur.com/a/rGhxETx) " width="131px" height="25px"></a><br>|

## Installation and usage
Step by step process of cloning the project, installments needed and how to use it

- Clone the repository

To run this project, you need the following tools and Python libraries installed:

Python Version:
- Python 3.8 or above
Required Libraries:
- OpenCV for image processing: opencv-python
- Streamlit for UI: streamlit
- Scikit-Image for HOG feature extraction: scikit-image
- Scikit-Learn for similarity calculations: scikit-learn
- SciPy for correlation coefficients: scipy
- NumPy for numerical operations: numpy

Steps To Use the AuthentiSign
Follow these steps to use the application:

1. Start the Application
- Open your terminal or command prompt.
- Navigate to the project directory where the Python script is located.
- Run the Streamlit application.

3.Enter Account Number and Capture Image
- In the input field labeled "Enter Account Number", type the account number associated with the signature.
- Click the "Capture Image" button to start the video stream from your configured IP camera.
- A live feed will appear in a separate window.
- Press the spacebar to capture an image of the signature.
- The captured image will be displayed on the Streamlit interface.

4. Verify the Signature
The application will:
- Check if the account number exists in the CSV file.
- If it’s a new account, the signature’s HOG features are saved.
- The application displays results:
 -> "Signature is Original": If the similarity and correlation exceed the thresholds.
 -> "Signature is Forged": If thresholds are not met.

## Preview
Screenshots of the project
<img src="url">
<img src="url">









