import cv2
import streamlit as st
import numpy as np
from skimage.feature import hog
from sklearn.metrics.pairwise import cosine_similarity
import csv
import os
from scipy.stats import pearsonr

# Path to the CSV file to store HOG features
hog_features_file = "hog_features.csv"

def capture_image():
    """
    Captures image from the pre-defined IP address.
    Returns:
        The captured frame.
    """
    ip_address = "http://192.168.1.2:8080/mjpeg"  # Change if needed
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


def compute_hog(image, pixels_per_cell=(30, 30), cells_per_block=(2, 2)):
    """
    Computes HOG features for the given image.
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray_image, (200, 100))
    hog_features = hog(resized_image, pixels_per_cell=pixels_per_cell,
                       cells_per_block=cells_per_block, visualize=False, channel_axis=None)
    return hog_features


def save_hog_features(account_number, hog_features):
    """
    Saves the HOG features to a CSV file.
    """
    with open(hog_features_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([account_number] + hog_features.tolist())


def load_hog_features(account_number):
    """
    Loads the HOG features for a given account number from the CSV file.
    """
    if not os.path.exists(hog_features_file):
        return None
    
    with open(hog_features_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == account_number:
                return np.array(row[1:], dtype=np.float64)
    return None


def compare_signatures(account_number, temp_image):
    """
    Compares the captured image's HOG features with the stored HOG features.
    """
    temp_image_hog = compute_hog(temp_image)

    original_image_hog = load_hog_features(account_number)

    if original_image_hog is not None:
        # Existing user
        score = cosine_similarity([temp_image_hog], [original_image_hog])[0][0]
        correlation_coefficient, _ = pearsonr(temp_image_hog, original_image_hog)
        return score, correlation_coefficient
    else:
        # New user
        save_hog_features(account_number, temp_image_hog)
        print(f"New user with account number {account_number}. HOG features saved.")
        return None, None


def verify_signature(account_number, temp_image):
    """
    Verifies the captured image against stored HOG features.
    """
    similarity_score, correlation_coefficient = compare_signatures(account_number, temp_image)

    if similarity_score is None:
        st.write(f"New user with account number {account_number}. HOG features saved.")
    else:
        print(f"Similarity Score: {similarity_score:.2f}")
        print(f"Correlation Coefficient: {correlation_coefficient:.2f}")
        if correlation_coefficient > 0.7 or similarity_score > 0.86:
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