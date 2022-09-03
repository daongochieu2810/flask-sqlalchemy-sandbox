#!/bin/bash
export DATABASE_URL='postgres://efhcrdoezlcoqj:e5fab140e8f6aa9fff97786f021003219d0f10f6abdef01f9ce6a6024595d0e5@ec2-44-207-126-176.compute-1.amazonaws.com:5432/d90qs881urf4m9'
if [ -d ".venv" ]
then
    source .venv/bin/activate
    python app.py
else
    python -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    python app.py
fi