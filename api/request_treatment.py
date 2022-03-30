from fastapi import APIRouter, Form, UploadFile, Request
import os
from pydantic import BaseModel
from typing import Optional
import json
import shutil
VOLUME =  '/static_storage/'
router = APIRouter()

class Tmp(BaseModel):
    id:str

@router.get("/app")
async def pong():
    return {'ping':'pong'}

@router.post("/app")
async def create_file(rq : Tmp):

    return {'ping':'pong', 'rq':rq.id}

@router.delete("/app")
async def delete():
    return {'ping':'pong'}

