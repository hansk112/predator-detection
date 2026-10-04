from picamera2 import Picamera2
import cv2
import time
import os
import sys
from datetime import datetime

sys.path.append("/home/hans/predator-detection")

from ai.classifier import classify, save_result

print("Starting predator detector...")

picam2 = Picamera2()

config = picam2.create_preview_configuration(
    main={"size": (640, 480)}
)

picam2.configure(config)
picam2.start()

print("Camera started")

time.sleep(2)

previous = None

save_dir = os.path.expanduser("~/predator/events")
os.makedirs(save_dir, exist_ok=True)

print(f"Saving events to: {save_dir}")

while True:

    frame = picam2.capture_array()

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGRA2GRAY
    )

    gray = cv2.GaussianBlur(
        gray,
        (21, 21),
        0
    )

    if previous is None:
        previous = gray
        print("Baseline frame established")
        continue

    delta = cv2.absdiff(
        previous,
        gray
    )

    threshold = cv2.threshold(
        delta,
        25,
        255,
        cv2.THRESH_BINARY
    )[1]

    motion_pixels = cv2.countNonZero(
        threshold
    )

    print(
        f"Motion pixels: {motion_pixels}",
        end="\r",
        flush=True
    )

    if motion_pixels > 5000:

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filename = (
            f"{save_dir}/{timestamp}.jpg"
        )

        cv2.imwrite(
            filename,
            frame
        )

        result = classify(
            filename
        )

        save_result(
            filename,
            result
        )

        print()
        print(
            f"Motion detected: {filename}"
        )

        print(
            f"Species: {result['species']} "
            f"Confidence: {result['confidence']}"
        )

        time.sleep(3)

    previous = gray
