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

<p align="center"><b>Abstact</b> </p> <br>
<p> AuthentiSign is a project designed to detect signature forgery. The system captures the handwritten signature, extracts its Histogram of Oriented Gradients (HOG) features, and securely stores these features in a CSV file for reference. When verifying authenticity, the system compares the HOG features of a test signature against the stored features of the original signature, and uses cosine similarity and Correlation Factor to calculate the similarity score providing a reliable method for detecting forgery. AuthentiSign can be implemented in sectors like banking, and legal documentation, where handwritten signatures are commonly used for authentication. </p>

## Table of Contents

- [Introduction](#introduction) <br>
- [Requirements](#requirements) <br>
- [How to use](#installation-and-usage) <br>
- [Preview](#previews)
- [Contribution](#contribution)
## Requirements
|||
|--|--|
|[3.11.9](https://www.python.org/downloads/release/python-3119/)|<img src="https://imgur.com/a/P8BUUyb" width="131px" height="25px"></a><br>|


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
<img src="https://i.imexampleImage.jpggur.com/" alt="Screenshot of the project">



## Contribution 
**This section provides instructions and details on how to submit a contribution via a pull request. It is important to follow these guidelines to make sure your pull request is accepted.**
1. Before choosing to propose changes to this project, it is advisable to go through the readme.md file of the project to get the philosophy and the motive that went behind this project. The pull request should align with the philosophy and the motive of the original poster of this project.
2. To add your changes, make sure that the programming language in which you are proposing the changes should be the same as the programming language that has been used in the project. The versions of the programming language and the libraries(if any) used should also match with the original code.
3. Write a documentation on the changes that you are proposing. The documentation should include the problems you have noticed in the code(if any), the changes you would like to propose, the reason for these changes, and sample test cases. Remember that the topics in the documentation are strictly not limited to the topics aforementioned, but are just an inclusion.
4. Submit a pull request via [Git etiquettes](https://gist.github.com/mikepea/863f63d6e37281e329f8) 









