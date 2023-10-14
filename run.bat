@echo off

if exist .\venv\ (
    echo "Activating Virtual Environment..."
) else (
    echo Creating virtual environment...
    python -m venv venv
    echo Installing dependencies...
    pip install -r requirements.txt
)

CALL venv\Scripts\activate
echo Starting application...
py .\main.py
