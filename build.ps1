$exclude = @("venv", "fipezap-monitor.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "fipezap-monitor.zip" -Force