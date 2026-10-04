from picamera2 import Picamera2
import cv2
import time

picam2 = Picamera2()

config = picam2.create_preview_configuration(
    main={"size": (640, 480)}
)

picam2.configure(config)

picam2.start()

time.sleep(2)

for i in range(20):
    frame = picam2.capture_array()

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGRA2GRAY
    )

    print(
        f"Frame {i}: "
        f"{gray.shape}"
    )

    time.sleep(0.1)

picam2.stop()
