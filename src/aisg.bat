@echo off
rem script for running AISG CLI Tool - https://www.aisingapore.org

rem show help message if no input is provided
if "%~1"=="" (
echo AISG CLI Tool v0.1 - USAGE - aisg module function parameter^(s^)
exit /b 1
)

rem concatenate inputs and pass to execution engine
set params=%1 %2 %3 %4 %5 %6 %7 %8 %9
python -u aisg.py %params%
