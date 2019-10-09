@echo off


echo Commit on GitHub k4kiran

echo.

set /p comment="Enter comment:"


git add .

git commit -m "%comment%"

git push



echo.
echo Committed Successfullly

pause