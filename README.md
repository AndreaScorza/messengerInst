# MessengerInst
MessengerInst is a bot that forwards Instagram messages to a Telegram chat.

##Installation
To install the requirements, run the following command:
```
pip intall -r requirements.txt
```

Next, create a `.env` file with the following variables:
```makefile
PASSWORD=xxxx <br>
USERNAME=xxxxx <br>
bot_token=xxxxx <br>
chat_id=xxxxx <br>
```
If you are using a Raspberry Pi, you will also need to install `chromium-chromedriver`:

```
sudo apt-get install chromium-chromedriver
```

In the `inst_module` file, replace the line `driver = webdriver.Chrome()` with:

```python
driver = webdriver.Chrome(‘/usr/lib/chromium-browser/chromedriver’)
```

To run the script using `Cron` you will need to install the `virtual display`:

```
pip3 install pyvirtualdisplay
```

and add it to the main file

```python
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()
```

From the `pi` open the terminal and type
```
crontab -e
```
to edit the crontab file.

add the following line to execute the script every hour
```
0 * * * * /usr/bin/python3 /path/to/your/script.py >> /path/to/log/file/log.txt
```

##### Stop receiving notification for specific contacts
To stop receiving notifications from specific contacts on your messaging platform, you can create a file called `unwanted.txt` and add the names of the senders you want to block, with each name on a separate line.

NB: Crontab might create the `data.txt` and look for the `unwanted.txt` files at the `/home/username/` level
