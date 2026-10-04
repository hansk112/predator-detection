import json
from pathlib import Path


def classify(image_path):
    """
    Placeholder classifier.

    Future versions:
    - YOLO
    - TensorFlow Lite
    - ONNX
    """

    return {
        "species": "unknown",
        "confidence": 0.0
    }


def save_result(image_path, result):

    image = Path(image_path)

    metadata = {
        "image": image.name,
        "species": result["species"],
        "confidence": result["confidence"]
    }

    metadata_file = image.with_suffix(".json")

    with open(metadata_file, "w") as f:
        json.dump(metadata, f, indent=2)


if __name__ == "__main__":

    test_file = "test.jpg"

    result = classify(test_file)

    print(result)
