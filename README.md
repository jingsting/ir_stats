# ir_stats
Tool to scrape driver stats from iRacing.com

## Reqired 
- Python 3
- selenium
Install with ```pip install selenium```
- Chrome webdriver
On mac, install with brew ```brew cask install chromedriver```

## Usage

### Login Information 
Create a file with the name ```config.py```.
In the file, fill out your user name(email address) and password. 
```
USERNAME = '__username_here__'
PASSWORD = '__password_here__'
```
### List of Drivers
In the file ```list.txt```, list driver names following the format of the examples
### Executing
In the terminal, run ```python stats.py```.
This will generate the result file ```stats.txt``` in the same directory
