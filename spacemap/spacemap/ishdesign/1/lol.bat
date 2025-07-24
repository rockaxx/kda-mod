@echo off
for %%f in (*.png) do (
    ffmpeg -y -i "%%f" "%%~nf.webp"
)
pause
