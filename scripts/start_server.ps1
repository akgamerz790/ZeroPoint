# ZeroPoint Server Startup Script
# This script starts the ZeroPoint server application.
# eeeewejt4uit8h957y4t3r2e1wqazxcvbnm,./';lkjhgfdsaQWERTYUIOP{}|:"<>?~`!@#$%^&*()_+-
Write-Host "Starting ZeroPoint Server..." -ForegroundColor Green
Set-Location (Split-Path $PSScriptRoot -Parent)
python core/server.py
Read-Host "Press Enter to continue..."