## Guide to download files from *SITE* using selenium on linux(ubuntu) and make the task automated by running the script at a certain time everyday.

1. Open terminal and download and install Python 3.7 or higher. You can use following commands to do that.
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.7
```

2. Install pip by writing following command.
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.7 get-pip.py
```
If you get an error like ```No module named 'distutils.util'``` when you run ```python3.7 get-pip.py```, run ```sudo apt install python3.7-distutils```.

3. Install selenium 4.
```python3.7 -m pip install selenium==4.7.2```

4. Install Webdriver Manager.
```python3.7 -m pip install webdriver_manager```

5. Download Google Chrome.
```
sudo apt install wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

6. Install git.
```sudo apt-get install git```

7. Download this program repository.
```git clone https://github.com/SudoRohit/SITEdownloader```

8. Open "SITEdownloader" and make the script "filedownloader.sh" executable by following command.
```
cd SITEdownloader
chmod +x filedownloader.sh
```

9. Open "config.ini" and make the required changes.

10. Now set the cron job for the script "filedownloader.sh" so that it runs automatically at 10am daily. Open terminal and type ```crontab -e```. Now add line ```0 10 * * * <path of filedownloader.sh>```.

You are all done. Now the script will run automatically at 10am daily and download the files from *SITE*.