# Setup

Update pip

```python
python3.10 -m pip install --upgrade pip
```

install dependencies 

```python 
pip3 install requests
pip3 install pandas
pip3 install unicornhatmini
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