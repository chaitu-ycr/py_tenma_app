@echo off

title "running py_tema_app"

set origin_dir=%CD%
set file_dir=%~dp0
cd %file_dir%
cd ..
set root_folder=%CD%
set cmd_venv_activate=%root_folder%\.venv\Scripts\activate.bat
set cmd_venv_deactivate=%root_folder%\.venv\Scripts\deactivate.bat

cd %root_folder%

:ACTIVATE_VENV
call %cmd_venv_activate%
if %ERRORLEVEL% NEQ 0 (GOTO VENV_ERROR)

:START_APP
python .\src\py_tenma_app.py
if %ERRORLEVEL% NEQ 0 (GOTO ERROR)

:END
call %cmd_venv_deactivate%
cd %origin_dir%
pause
GOTO :eof

:ERROR
title "Failed to run py_tema_app due to error %ERRORLEVEL%"
cd %origin_dir%
pause
GOTO :eof

:VENV_ERROR
title "Failed to run app due to error %ERRORLEVEL%. run install_dependencies.bat file and try again."
cd %origin_dir%
pause
GOTO :eof
