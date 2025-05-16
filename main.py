#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import uvicorn
import os

app = FastAPI(title="Student Performance Prediction API", version="1.0")

model_path = "model.pkl"
with open(model_path, 'rb')as f:
    model = pickle.load(f)

class StudentFeatures(BaseModel):
    hours_studied: int
    previous_scores: int
    extracurricular_activities: int
    sleep_hours: int
    sample_question_papers_practiced: int

@app.post("/predict", summary="Predict Student Performance")
async def predict(student: StudentFeatures):
    input_data = student.dict()

    columns = [
        "Hours Studied", 
        "Previous Scores", 
        "Extracurricular Activities", 
        "Sleep Hours", 
        "Sample Question Papers Practiced"
    ]
    df_data = pd.DataFrame([input_data])
    df_data.columns = columns

    pred = model.predict(df_data)[0]

    return {"pred": pred}

@app.get("/status")
async def get_status():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8005)


# In[ ]:




