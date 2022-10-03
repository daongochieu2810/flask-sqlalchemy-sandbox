#!/bin/bash
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