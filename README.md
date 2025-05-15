# Train-Detection-API


This is a FastAPI-based backend system for receiving and logging train detections from smart sensors and AI-powered cameras. Designed to support real-time monitoring and rerouting for road traffic impacted by trains, this API is part of the larger "RoundAbout" project.

## Features

- Accepts POST requests from train detection devices (e.g., Raspberry Pi, Arduino, AI cameras)
- Validates and logs data such as location, timestamp, detection method, and confidence score
- Exposes endpoints to retrieve all detections or individual records by ID
- Can be extended to support rerouting apps or traffic management systems

## Tech Stack

- Backend Framework: FastAPI (Python 3.8+)
- Data Model: Pydantic
- Storage: In-memory (temporary; upgrade to database recommended)
- API Docs: Auto-generated at `/docs` and `/redoc`

## Getting Started

### 1. Clone the Repository

git clone https://github.com/xangelusmortis/train-detection-api.git
cd train-detection-api
2. Install Dependencies
Make sure you’re using Python 3.8 or newer.

bash
Copy
Edit
pip install fastapi uvicorn
3. Run the API Server
bash
Copy
Edit
uvicorn main:app --reload
Visit the following URLs in your browser:

Swagger UI: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

API Usage
POST /api/train-detection
Submit a new train detection.

Example request body:

json
Copy
Edit
{
  "crossing_id": "X001",
  "latitude": 40.7132,
  "longitude": -74.0060,
  "timestamp": "2025-05-14T08:20:00Z",
  "detected_by": ["laser", "camera_ai"],
  "confidence_score": 0.97,
  "train_direction": "northbound"
}
Example response:

json
Copy
Edit
{
  "status": "success",
  "message": "Train detection recorded",
  "detection_id": "uuid-generated-id"
}
GET /api/train-detection
Returns all recorded detections.

GET /api/train-detection/{detection_id}
Returns a specific detection by its unique ID.

Future Plans
Replace in-memory storage with persistent database (e.g., SQLite or Firebase)

Add API key authentication

Create dashboard frontend to view and manage detections

Integrate with real-time rerouting application logic

Contributing
Contributions are welcome. Fork the repository, make your changes, and submit a pull request.

Legal Notice
This project is intended for research, development, and demonstration purposes. Use in the field should follow all applicable laws and obtain any required permissions from property owners or rail authorities.

Contact
Developed by Mort as part of the RoundAbout project.
For inquiries or collaboration opportunities, please reach out via GitHub or your preferred contact method.
