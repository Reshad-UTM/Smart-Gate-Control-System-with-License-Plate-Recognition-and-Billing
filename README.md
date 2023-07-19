# Smart-Gate-Control-System-with-License-Plate-Recognition-and-Billing
This project demonstrates a Smart Gate Control System integrated with License Plate Recognition (LPR) and Billing to manage entry and exit of vehicles in a secure and efficient manner. The system uses a webcam to capture video frames, OpenCV for license plate detection, and Tesseract OCR for license plate recognition. It also employs an Arduino-based servo motor and IR sensor to control the gate's opening and closing based on detected vehicles.
Features

    Real-time license plate detection and recognition.
    Automatic gate control based on vehicle presence.
    Capture and store license plate data for billing and management.
    Calculate payment bills for vehicles with the same license plate number.
    Customizable billing rates for different time durations.

Requirements

    Python 3.x
    OpenCV (cv2)
    pytesseract
    Tesseract OCR (Make sure to install and set the path in the Python code)
    Arduino IDE and an Arduino board with a servo motor and an IR sensor.

Setup

    Install the required Python libraries using pip:

bash

pip install opencv-python pytesseract

    Install Tesseract OCR: Tesseract OCR Installation Guide

    Upload the provided Arduino code to your Arduino board, connecting a servo motor and an IR sensor to the appropriate pins.

    Connect your webcam to your computer.

Usage

    Run the Python script license_plate_recognition.py:

bash

python license_plate_recognition.py

    The webcam feed will open, and the system will detect and recognize license plates in real-time.

    When a car is detected, the gate will automatically open. After the car passes, the gate will close after a delay.

    If the same vehicle's license plate is detected within 30 seconds, a 10% discount will be applied to the bill calculation.

    The billing system will calculate the payment bills based on the elapsed time and the customized billing rates.

License

This project is licensed under the MIT License.
Note

    This project is designed for educational and demonstration purposes only. Ensure proper legal compliance and privacy considerations before deploying it in a real-world setting.
    The accuracy of license plate recognition may vary depending on lighting conditions, camera placement, and image quality.

Contributions

Contributions, bug reports, and feedback are welcome! Feel free to open an issue or submit a pull request.
Acknowledgments

This project was inspired by OpenCV and Tesseract OCR for their invaluable contributions to computer vision and OCR technology.
Authors

    Reshad-UTM - GitHub Profile

Contact

For any inquiries or questions, please email us at reshadrayhan2016@gmail.com.com.
