# ZeroPoint Agent Deployment Script
param(
    [string]$ServerIP = "127.0.0.1",
    [int]$ServerPort = 4444
)

Write-Host "Deploying ZeroPoint Agent..." -ForegroundColor Yellow
Write-Host "Target: ${ServerIP}:${ServerPort}" -ForegroundColor Cyan

Set-Location (Split-Path $PSScriptRoot -Parent)
python core/agent.py $ServerIP $ServerPort