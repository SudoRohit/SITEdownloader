log=log_file.log
date >> $log
python3.7 main.py >> $log
python3.7 thesis.py >> $log
date >> $log