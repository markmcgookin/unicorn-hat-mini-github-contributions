# Setup

Update pip

```python
python3.10 -m pip install --upgrade pip
```

install dependencies (-H will install them in the Pi's home directory not the pi users one)

```python 
sudo -H pip3 install requests
sudo -H pip3 install pandas
sudo -H pip3 install unicornhatmini
```

# Github Token
Go to https://github.com/settings/tokens and generate a CLASSIC token. It needs user > read permissions only

# Secrets
Create a file called usersecrets with this content and place your token in it

```python
# Add your secrets here.
usersecrets = {
    "githubusername" : "SOMEUSERNAME",
    "githubtoken" : "SOMETOKEN"
}
```

# If you get an error with numpy install the dependencies another way 

```bash 
sudo apt-get install libatlas-base-dev
```

# Setup to run automatically

Make script executable

```bash
chmod 755 launcher.sh
```

create a logs directory in your home folder

```bash
cd
mkdir logs
```

edit the crontab

```bash
sudo crontab -e
```

and add this line

```bash
@reboot sh /home/pi/unicorn-hat-mini-github-contributions/launcher.sh >/home/pi/logs/cronlog 2>&1
```

then just reboot the pi