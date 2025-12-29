@echo off
setlocal

echo ========================================
echo Building Roblox Multi Client (GUI)
echo Using Nuitka to pack main.py
echo ========================================
echo.

REM Check if Nuitka is installed
python -m nuitka --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Nuitka is not installed!
    echo Install it with: pip install nuitka
    pause
    exit /b 1
)

echo [1/4] Cleaning previous build...
if exist "main.dist" rmdir /s /q "main.dist"
if exist "main.build" rmdir /s /q "main.build"
if exist "main.onefile-build" rmdir /s /q "main.onefile-build"
if exist "dist\RobloxMultiClient.exe" del /q "dist\RobloxMultiClient.exe"
echo Done.
echo.

echo [2/4] Building with Nuitka...
python -m nuitka ^
    --standalone ^
    --onefile ^
    --windows-disable-console ^
    --include-package=customtkinter ^
    --include-package=psutil ^
    --include-package=win32event ^
    --include-package=win32api ^
    --include-package=win32timezone ^
    --assume-yes-for-downloads ^
    --enable-plugin=tk-inter ^
    --output-dir=dist ^
    --output-filename=RobloxMultiClient.exe ^
    --remove-output ^
    main.py

if errorlevel 1 (
    echo [ERROR] Build failed!
    pause
    exit /b 1
)

echo.
echo [3/4] Build completed successfully!
echo.

echo [4/4] Finalizing...
if exist "dist\RobloxMultiClient.exe" (
    echo.
    echo ========================================
    echo Build Successful!
    echo ========================================
    echo Executable: dist\RobloxMultiClient.exe
    echo.
    echo Roblox Multi Client is ready.
    echo No console will appear, GUI only.
    echo ========================================
) else (
    echo [ERROR] Executable not found in dist folder!
    pause
    exit /b 1
)

echo.
pause
