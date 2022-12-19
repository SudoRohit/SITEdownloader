## Guide to download files from *SITE* using selenium on linux and make the task automated by running the script at a certain time everyday.

1. Download and install Python 3.9 or higher.
https://www.python.org/downloads/
2. Open terminal and install pip by writing following command.
```sudo apt install python3-pip```.
3. Install selenium 4
```pip install selenium```.
4. Install git
```sudo apt-get install git```.
5. Download this program repository.
```git clone https://github.com/SudoRohit/SITEdownloader```.
6. Open "SITEdownloader" make the script "filedownloader.sh" executable by command ```chmod +x filedownloader.sh```.
7. Open "config.ini" and make the required changes.
8. Now set the cron job for the script "filedownloader.sh" so that it runs automatically at 10am daily. Open terminal and type ```crontab -e```. Now add line ```0 10 * * * <path of filedownloader.sh>```.

You are all done. Now the script will run automatically at 10am daily and download the files from *SITE*.