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
    "githubtoken" : "SOMETOKEN",
    "defaultColours": "true",
    "altColours": {
        "0": {
            "r": 0,
            "g": 0,
            "b": 0,
        },
        "1-2": {
            "r": 255,
            "g": 0,
            "b": 0,
        },
        "3-5": {
            "r": 127,
            "g": 0,
            "b": 128,
        },
        "6-10": {
            "r": 0,
            "g": 0,
            "b": 255,
        },
        "11-15": {
            "r": 0,
            "g": 127,
            "b": 128,
        },
        "more": {
            "r": 0,
            "g": 255,
            "b": 0,
        }
    }
}
```
# Custom colours
If you want to use your own custom colours for the bandings, specify them in the `altColours` property, and set `defaultColours` to `"false"`

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