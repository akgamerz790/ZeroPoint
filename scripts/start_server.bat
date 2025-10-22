@echo off
echo Starting ZeroPoint Server...
cd /d "%~dp0\.."
python core/server.py
pause