# Create venv if missing, install deps using venv python, then run main.py
$repo = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $repo
$venvPy = Join-Path $repo 'venv\Scripts\python.exe'
if (-Not (Test-Path $venvPy)) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
}
$venvPy = Join-Path $repo 'venv\Scripts\python.exe'
Write-Host "Installing requirements using $venvPy..."
& $venvPy -m pip install --upgrade pip
& $venvPy -m pip install -r requirements.txt
Write-Host "Running main.py using $venvPy..."
& $venvPy main.py
