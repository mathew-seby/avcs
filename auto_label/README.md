# Automated Dataset Annotation Script (AVCS)

**Description:**
This Jupyter Notebook automates the data labeling process for the AI-driven Traffic Control System (AVCS) dataset, handling the training, testing, and validation sets. 

Instead of manually drawing bounding boxes, this script uses a pre-trained YOLOv8 nano model (`yolov8n.pt`) to scan over 12,000 unlabelled traffic images. It detects vehicles (cars, motorcycles, buses, and trucks) and calculates if their center points fall within a predefined Region of Interest (ROI) designed to monitor lane starvation. 

**How it works:**
* **Active Lanes:** If a vehicle is detected inside the ROI, it automatically generates a YOLO-formatted `.txt` label file marking it as an active lane (class `0`). 
* **Empty Lanes:** If the ROI is empty, it generates a standard empty label file so the model learns to recognize when a light should be skipped.
* **Export:** Finally, the script zips and exports the fully annotated dataset, ready for the main model training pipeline.
