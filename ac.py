import cv2
import streamlit as st
import numpy as np
from skimage.feature import hog
from sklearn.metrics.pairwise import cosine_similarity
import os
from scipy.stats import pearsonr

# Set the IP address of your camera stream (replace with your actual IP address)
ip_address = "http://192.168.43.1:8080/mjpeg"  # Change if needed

# Set the path to the original image folder containing signatures (replace with your path)
original_image_folder = r"C:\Users\HOME\Desktop\python\signs"  # Change if needed

def capture_image():
    """
    Captures image from the pre-defined IP address.

    Returns:
        A boolean indicating success (True) or failure (False).
    """
    print(f"Attempting to open video stream from {ip_address}")

    try:
        cap = cv2.VideoCapture(ip_address)
        if not cap.isOpened():
            print("Error: Cannot open video stream.")
            return None
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error reading video stream.")
                return None

            cv2.imshow('Video', frame)


            if cv2.waitKey(1) & 0xFF == ord(' '):
                cap.release()
                cv2.destroyAllWindows()
                return frame
    except Exception as e:
        print(f"Error capturing image: {e}")
        return None
    finally:
        cap.release()
        cv2.destroyAllWindows()


def compute_hog(image, pixels_per_cell, cells_per_block):
    """
    Computes HOG features for the given image.

    Args:
        image: The input image.
        pixels_per_cell: The pixels per cell for HOG.
        cells_per_block: The cells per block for HOG.

    Returns:
        The computed HOG features.
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray_image, (200, 100))
    hog_features = hog(resized_image, pixels_per_cell=pixels_per_cell,
                       cells_per_block=cells_per_block, visualize=False, channel_axis=None)
    return hog_features


def compare_signatures(account_number, temp_image):
    """
    Compares the captured image with the corresponding signature in the original folder.

    Args:
        account_number: The account number entered by the user.
        temp_image: The captured image.

    Returns:
        A tuple containing the similarity score (float) or None if no match found.
    """
    pixels_per_cell = (30, 30)
    cells_per_block = (2, 2)

    temp_image_hog = compute_hog(temp_image, pixels_per_cell, cells_per_block)

    filename = f"{account_number}.jpg"
    signature_path = os.path.join(original_image_folder, filename)

    if os.path.exists(signature_path):
        # Existing user, signature found
        original_image = cv2.imread(signature_path)
        original_image_hog = compute_hog(original_image, pixels_per_cell, cells_per_block)
        score = cosine_similarity([temp_image_hog], [original_image_hog])[0][0]
        correlation_coefficient, _ = pearsonr(temp_image_hog, original_image_hog)
        return score, correlation_coefficient
        
    else:
        # New user, signature not found
        cv2.imwrite(os.path.join(original_image_folder, filename), temp_image)
        print(f"New user with account number {account_number}. Signature captured and saved.")
        return None, None


def verify_signature(account_number, temp_image):
    """
    Checks for the corresponding signature file, compares if it exists, and displays a message.

    Args:
        account_number: The account number entered by the user.
        temp_image: The captured image.
    """
    similarity_score, correlation_coefficient = compare_signatures(account_number, temp_image)

    if similarity_score is None:
        # New user, signature not found
        st.write(f"New user with account number {account_number}. Signature captured and saved.")
    else:
        print(f"Similarity Score: {similarity_score:.2f}")
        print(f"Correlation Coefficient: {correlation_coefficient:.2f}")
        if correlation_coefficient > 0.7 or similarity_score > 0.85:
            st.write("SIGNATURE IS ORIGINAL")
        else:
            st.write("SIGNATURE IS FORGED")


# Streamlit UI
st.title("Signature Verification")

account_number = st.text_input("Enter Account Number")

if st.button("Capture Image"):
    if not account_number:
        st.write("Please enter an account number.")
    else:
        temp_image = capture_image()
        if temp_image is not None:
            st.image(temp_image, caption="Captured Image", channels="BGR")
            verify_signature(account_number, temp_image)
        else:
            st.write("Failed to capture image. Please try again.")
