from fastapi import FastAPI
from Back_Office_Agent.controllers.main import backagent
from Document_Verification_Agent.controllers.main import documentagent
from Eligibility_Check_Agent.controllers.main import eligibilityagent
from Report_Generation_Agent.controllers.main import reportagent
from Screening_Ops_Maker_Agent.controllers.main import screeningagent
from fastapi.middleware.cors import CORSMiddleware
from Human_in_the_loop.controllers.main import hilagent
from Data_Acquistion_Agent.controllers.main import dataagent



app = FastAPI(
    title="Agents",
    description="This API routes requests to different agent.",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(backagent,tags=["Back-Office-Agent"])
app.include_router(dataagent,tags=["Data-Acquistion-Agent"])
app.include_router(documentagent,tags=["Document-Verification-Agent"])
app.include_router(eligibilityagent,tags=["Eligibility-Checker-Agent"])
app.include_router(reportagent,tags=["Report-Generation-Agent"])
app.include_router(screeningagent,tags=["Screening-OpsMaker-Agent"])
app.include_router(hilagent,tags=["Human-in-the-loop"])
