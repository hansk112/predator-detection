from picamera2 import Picamera2
import cv2
import time
import os
from datetime import datetime

picam2 = Picamera2()

config = picam2.create_preview_configuration(
    main={"size": (640, 480)}
)

picam2.configure(config)
picam2.start()

time.sleep(2)

previous = None

save_dir = os.path.expanduser("~/predator/events")
os.makedirs(save_dir, exist_ok=True)

while True:

    frame = picam2.capture_array()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if previous is None:
        previous = gray
        continue

    delta = cv2.absdiff(previous, gray)

    threshold = cv2.threshold(
        delta,
        25,
        255,
        cv2.THRESH_BINARY
    )[1]

    motion_pixels = cv2.countNonZero(threshold)

    if motion_pixels > 5000:

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filename = f"{save_dir}/{timestamp}.jpg"

        cv2.imwrite(filename, frame)

        print(f"Motion detected: {filename}")

        time.sleep(3)

    previous = gray
