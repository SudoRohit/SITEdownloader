## Guide to download files from *SITE* using selenium on linux(ubuntu) and make the task automated by running the script at a certain time everyday.

1. Open terminal and download and install Python 3.9 or higher. You can use following commands to do that.
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.9
```
2. Install pip by writing following command.
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py
```
If you get an error like ```No module named 'distutils.util'``` when you run ```python3.9 get-pip.py```, run ```sudo apt install python3.9-distutils```.
3. Install selenium.
```python3.9 -m pip install selenium```
4. Install Webdriver Manager.
```python3.9 -m pip install webdriver_manager```
5. Install git.
```sudo apt-get install git```
6. Download this program repository.
```git clone https://github.com/SudoRohit/SITEdownloader```
7. Open "SITEdownloader" and make the script "filedownloader.sh" executable by following command.
```
cd SITEdownloader
chmod +x filedownloader.sh
```
8. Open "config.ini" and make the required changes.
9. Now set the cron job for the script "filedownloader.sh" so that it runs automatically at 10am daily. Open terminal and type ```crontab -e```. Now add line ```0 10 * * * <path of filedownloader.sh>```.

You are all done. Now the script will run automatically at 10am daily and download the files from *SITE*.