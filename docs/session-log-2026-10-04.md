# Predator Detection Project Session Log
Date: 2026-10-04

## Summary

Successful migration from a simple motion camera toward an AI-ready predator detection platform.

The core capture pipeline is now functioning end-to-end.

## Accomplishments

### Environment

- Created Python virtual environment
- Recreated virtual environment using system packages
- Verified:
  - Picamera2
  - OpenCV
  - NumPy
  - Camera hardware

### AI Project Structure

Created:

- ai/classifier.py
- dataset/bird
- dataset/cat
- dataset/person
- dataset/possum
- dataset/unknown

### Motion Detection

Located existing detector:

/home/hans/predator/motion_detector.py

Copied into project repository:

scripts/motion_detector.py

### Camera Testing

Verified:

- OV5647 operational
- Picamera2 operational
- Frame capture working
- Repeated frame capture working

Test result:

(480, 640, 4)

This confirms camera frames are BGRA format.

### AI Integration

Created placeholder classifier:

{
  "species": "unknown",
  "confidence": 0.0
}

Motion detector now:

Motion
↓
Capture Image
↓
Classify
↓
Save Metadata
↓
Save Event

### Event Metadata

JSON files successfully generated.

Example:

20261004_xxxxxx.jpg
20261004_xxxxxx.json

### Browser Access

Started web server:

python3 -m http.server 8080

Confirmed images can be viewed via:

http://192.168.1.22:8080

### Test Image Review

Confirmed:

- Image capture working
- IR illumination working
- Motion detection triggering correctly

Observed issue:

- Camera currently aimed toward enclosure/IR reflections
- Needs physical positioning adjustment

## Outstanding Tasks

### High Priority

1. Improve camera positioning
2. Build temporary test rig
3. Confirm camera field of view
4. Capture useful outdoor images

### Medium Priority

1. Generate gallery page
2. Display metadata in browser
3. Improve event review workflow

### Future AI

Investigated YOLO installation.

Result:

- Ultralytics installed
- Torch installation attempted
- Torch attempted to download CUDA packages
- Installation abandoned

Decision:

Investigate:
- TensorFlow Lite
or
- ONNX Runtime

for Raspberry Pi deployment.

## Recommended Next Session

1. Build physical camera stand
2. Improve camera aiming
3. Collect real-world dataset
4. Add gallery page
5. Evaluate lightweight inference options
6. Begin species classification

## Current Status

Project state:

AI-ready event pipeline operational.

Motion Detection: Working
Camera Capture: Working
Image Storage: Working
Metadata Storage: Working
Browser Access: Working

Species Classification:
Placeholder implementation only.
