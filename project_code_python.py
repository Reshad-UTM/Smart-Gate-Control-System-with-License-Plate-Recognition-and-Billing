import cv2
import pytesseract
import time
import serial

# Set the path to the Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the pre-trained cascade classifier for license plate detection
plate_cascade = cv2.CascadeClassifier(r'C:\Users\Reshad_UTM\Desktop\fyp\haarcascade_russian_plate_number.xml')

# Open a connection to the webcam
video_capture = cv2.VideoCapture(1)

# Variables for tracking time and gate state
start_time = time.time()
recognized_plate = None
gate_open = False
stored_plate = None

# Initialize the serial connection to Arduino
ser = serial.Serial('COM3', 9600)  # Update with the correct COM port

def open_gate():
    ser.write(b'1')  # Send command to Arduino to open the gate
    time.sleep(1)  # Adjust the delay as needed

def close_gate():
    ser.write(b'2')  # Send command to Arduino to close the gate
    time.sleep(1)  # Adjust the delay as needed

while True:
    # Read a frame from the webcam
    ret, frame = video_capture.read()

    # Convert the frame to grayscale for license plate detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect license plates in the grayscale frame
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Process each detected license plate
    for (x, y, w, h) in plates:
        # Extract the license plate region
        plate_img = frame[y:y + h, x:x + w]

        # Convert the license plate region to grayscale for OCR
        plate_gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)

        # Perform OCR on the license plate region
        plate_text = pytesseract.image_to_string(plate_gray, config='--psm 7 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

        # Remove any non-alphanumeric characters from the recognized text
        plate_text = ''.join(e for e in plate_text if e.isalnum())

        # Draw a bounding box around the license plate
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the recognized text on the frame
        cv2.putText(frame, plate_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Store the recognized plate
        recognized_plate = plate_text

    # Check if 30 seconds have elapsed
    elapsed_time = time.time() - start_time
    if elapsed_time >= 30:
        # Print the stored license plate text
        print("License Plate: ", recognized_plate)

        # Calculate the bill based on the elapsed time
        bill = elapsed_time * 0.1  # Adjust the rate per second as needed

        # Print the bill
        print("Bill: $", bill)

        # Check if the gate is already open and the recognized plate is the same
        if gate_open and recognized_plate == stored_plate:
            # Calculate the payment bill for the same plate
            payment = bill * 0.9  # Apply a 10% discount for repeat plate

            # Print the payment bill
            print("Payment for repeat plate: $", payment)

        # Reset the timer and recognized plate
        start_time = time.time()
        recognized_plate = None

        # Store the recognized plate for the next iteration
        stored_plate = recognized_plate

        # Close the gate
        close_gate()
        gate_open = False

    # Check if a license plate is recognized and the gate is closed
    if recognized_plate is not None and not gate_open:
        # Open the gate
        open_gate()
        gate_open = True

    # Display the resulting frame
    cv2.imshow('License Plate Detection', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close any open windows
video_capture.release()
cv2.destroyAllWindows()
