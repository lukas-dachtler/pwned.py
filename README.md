# pwned.py
#### pwned.py is a small script to check if your password has been pwned by checking the API from [haveibeenpwned.com](https://haveibeenpwned.com/API/v2)
## ■ Install
Install [Requests](http://docs.python-requests.org/en/v2.7.0/user/install/)
## ■ Use (single password)
```
python pwned.py <your password>
```
## ■ Use (file)
```
python pwned.py <path\filename.txt>
```
> **Format:** Each password has to be in a single line

> **Result:** Results will be written next to each password in the same file