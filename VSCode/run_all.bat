@echo off
start C:\Windows\py.exe C:\Users\student\Desktop\VSCode\sam_serial_to_file.py
start C:\Windows\py.exe C:\Users\student\Desktop\VSCode\sam_client_ser_RnW.py

:: Note - this extra call is to avoid a bug with %~f0 when the script
::        is executed with quotes around the script name.
call :getLock
exit /b

:getLock
:: The CALL will fail if another process already has a write lock on the script
call :main 9>>"%~f0"
exit /b

:main
:: Body of your script goes here. Only one process can ever get here
:: at a time. The lock will be released upon return from this routine,
:: or when the script terminates for any reason


start cmd.exe /k "node-red"
:start
ping 127.0.0.1
if %errorlevel% == 1 (
goto :fail
) else (
enter command to run when connected here
start "" http://127.0.0.1:1880/ui
exit /b
)
:fail
echo Not connected to network, retrying...
goto :start