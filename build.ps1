Write-Host "Cleaning up old build..."
if (Test-Path package) { Remove-Item -Recurse -Force package }
if (Test-Path deployment.zip) { Remove-Item -Force deployment.zip }

Write-Host "Creating package folder..."
New-Item -ItemType Directory -Name package | Out-Null

Write-Host "Installing plotly (Linux)..."
pip install plotly `
    --platform manylinux2014_x86_64 `
    --only-binary=:all: `
    --python-version 3.12 `
    --implementation cp `
    --target ./package `
    --upgrade

Write-Host "Copying function code..."
Copy-Item lambda_function.py package/

Write-Host "Zipping..."
Compress-Archive -Path .\package\* -DestinationPath .\deployment.zip

Write-Host "Done! Upload deployment.zip to Lambda."