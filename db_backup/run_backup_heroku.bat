set YYYYMMDD=%DATE:~10,4%%DATE:~4,2%%DATE:~7,2%
echo %YYYYMMDD%

heroku pg:backups:download -a influenserul-py-rest -o bkps\%YYYYMMDD%.dump