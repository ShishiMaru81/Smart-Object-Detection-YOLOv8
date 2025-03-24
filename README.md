# Smart-Object-Detection-YOLOv8
<h3>YOLOv8 Object Detection with Webcam and Video Capture</h3>
<p>This project leverages YOLOv8 (You Only Look Once version 8[nano model]), one of the latest state-of-the-art models for real-time object detection. Using the YOLOv8 architecture, this project can detect and track multiple objects in real-time, either through a webcam or from a video file. It utilizes the power of computer vision libraries like OpenCV and cvzone for efficient processing, tracking, and visualization.</p>

<h2>Features:</h2>
<ul>
  <li><strong>Real-Time Object Detection:</strong> Detects objects in live webcam feed or video files.</li>
  <li><strong>Bounding Box Visualization:</strong> Displays bounding boxes around detected objects.</li>
  <li><strong>Confidence Scores:</strong> Shows the confidence percentage for each detected object.</li>
  <li><strong>Class Name Labeling:</strong> Labels detected objects with their class names (e.g., car, person, dog, etc.).</li>
</ul>

<h2>Technologies:</h2>
<ul>
  <li><strong>YOLOv8n.pt/YOLOv8m.pt:</strong> A state-of-the-art real-time object detection model.</li>
  <li><strong>OpenCV:</strong> Library for computer vision tasks and video capture.</li>
  <li><strong>cvzone:</strong> Simplifies OpenCV operations, particularly drawing on images.</li>
  <li><strong>Python:</strong> The project is written in Python 3.</li>
</ul>
<br/>
<h2>Key Features:</h2>

<h3>Real-Time Object Detection:</h3>
<ul>
  <li>Detects and identifies a wide range of objects (over 80 classes) in live video feeds, including vehicles (cars, buses, trucks), people, animals, and other common objects.</li>
  <li>The system can run on both webcam streams and video files, making it versatile for different use cases.</li>
</ul>

<h3>Bounding Boxes & Labels:</h3>
<ul>
  <li>For each detected object, a bounding box is drawn around it.</li>
  <li>The detected object is labeled with its class name (e.g., car, person, dog) and the confidence score of detection is displayed.</li>
</ul>

<h3>Customizable Detection:</h3>
<ul>
  <li>Easily extendable to work with custom-trained YOLOv8 models.</li>
  <li>You can modify the list of objects that the model detects by altering the class names or retraining the model with a custom dataset.</li>
</ul>

<h3>Optimized for Speed:</h3>
<ul>
  <li>The program is designed for real-time performance with optimized video processing, ensuring smooth operation on standard devices.</li>
  <li>FPS (frames per second) display to monitor performance and efficiency.</li>
</ul>

<h3>Tracking with SORT Algorithm:</h3>
<ul>
  <li>Implemented SORT (Simple Online and Realtime Tracking) to track objects over multiple frames.</li>
  <li>Each object is assigned a unique ID, allowing for continuous tracking as it moves through the scene.</li>
</ul>

<h3>Video/Live Stream Compatibility:</h3>
<ul>
  <li>The model can be run on live webcam streams or with video files, making it highly flexible for various applications.</li>
</ul>

<h2>Potential Use Cases:</h2>

<ul>
  <li><strong>Surveillance Systems:</strong> Implement object tracking and movement detection for security and monitoring.</li>
  <li><strong>Traffic Monitoring:</strong> Detect and track vehicles, pedestrians, and other objects in traffic footage for analysis.</li>
  <li><strong>Autonomous Vehicles:</strong> Real-time object detection for self-driving cars to identify road signs, pedestrians, and vehicles.</li>
  <li><strong>Smart Cities:</strong> For detecting and tracking objects in urban environments to monitor public spaces and traffic flow.</li>
  <li><strong>Sports Analytics:</strong> Tracking players, sports equipment, and other objects in sports videos.</li>
</ul>
