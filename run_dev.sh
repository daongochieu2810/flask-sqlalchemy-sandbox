#!/bin/bash
export DATABASE_URL='postgresql://hieu:hieu@localhost:5432/bt5110'
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