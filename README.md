```bash
python3 -m venv venv
source .venv/bin/activate # on linux
.\.venv\Scripts\activate # on windows
pip freeze > requirements.txt
```

To start the app automatically on launch, edit the file `/etc/rc.local` and add the lines:

```bash
cd /home/pi/app
/bin/bash /home/pi/app/init.sh &
```

To add a cron job to restart the system daily, edit the cron jobs by using:

```bash
sudo crontab -e
```

and add the following line:

```bash
0 0 * * * /sbin/shutdown -r now
```
