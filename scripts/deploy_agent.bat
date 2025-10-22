@echo off
echo Deploying ZeroPoint Agent...
set SERVER_IP=127.0.0.1
set SERVER_PORT=4444
cd /d "%~dp0\.."
python core/agent.py %SERVER_IP% %SERVER_PORT%
pause