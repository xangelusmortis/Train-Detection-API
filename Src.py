from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid
"""Fast API: Is the web framework used to build my API
   HTTPException: To throw errors
   BaseModel, Field: Used to define data structures and validate inputs
   List, Optional: Used type check
   uuid: Generation of unique detection IDs"""

app = FastAPI(title="Train Detection API")
detection_log = []                          #stores detections during server run time << database neccessary?


#Define the data model for detection model
class Detection(BaseModel):
    crossing_id: str                       #Which sensor it came from
    latitude: float                        #Geograpic location
    longitude: float
    timestamp: datetime                    #When the detection happened
    detected_by : List[str] = Field(..., example=["laser", "camera_ai"])   #List of the provided detection methods
    confidence_score: float = Field(..., ge=0.0, le=1.0)                   #How sure the program is that it is a train
    train_direction: Optional[str] = Field(None, example="northbound")     #Optional

#Define the response model
class DetectionResponse(BaseModel):
        status: str
        message: str
        detection_id: str

# POST endpoint to receive detection
@app.post("/api/train-detection", response_model=DetectionResponse)  #This tell FastAPI to handle POST requests here
async def receive_detection(detection: Detection):                   #Validating incoming JSON against Detection model
    detection_id = str(uuid.uuid4())                                 #Creates a random unique ID for this detection

    # Store detection with an ID
    detection_entry = detection.dict()                               #Converts the object to the dictionary
    detection_entry["detection_id"] = detection_id
    detection_log.append(detection_entry)                            #Adds the detection to memory

    return DetectionResponse(
        status="success",
        message="Train detection recorded",
        detection_id=detection_id

    )
# GET endpoint to fetch all detections (for viewing/debugging)
@app.get("/api/train-detection")
async def get_all_detections():
    return detection_log

# GET endpoint to fetch a single detection by ID
@app.get("/api/train-detection/{detection_id}")  #this is a URL parameter
async def get_detection_by_id(detection_id: str):
    #this loops through stored detections to find one witha  matching ID
    for d in detection_log:
        if d["detection_id"] == detection_id:
            return d
    raise HTTPException(status_code=404, detail="Detection not found")



