# CLICK-Jack
It is a automatic tool to find Clickjacking Vulnerability in various Web applications.

## What is Clickjacking ?
Clickjacking, also known as a “UI redress attack”, is when an attacker uses multiple transparent or opaque layers to trick a user into clicking on a button or link on another page when they were intending to click on the top level page. Thus, the attacker is “hijacking” clicks meant for their page and routing them to another page, most likely owned by another application, domain, or both. [Reference](https://owasp.org/www-community/attacks/Clickjacking)

## Installation:
````
git clone 
cd clickjack
pip install -r requirements.txt
````

## Example:
To run on list of domains use below command:
````
python3 clickjack.py <URLs LIST>
or
python3 clickjack.py urls.txt
````

![1](https://user-images.githubusercontent.com/75206412/148673052-565d2571-11a1-4345-a581-71e6ce052ef2.jpg)

## Benifits:
- It will work for list of urls
- Output the list of the vulnerable urls in seperate text file

## Support ME:

<a href="https://www.buymeacoffee.com/princep4" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
<img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/PrincePrafull3?style=social" width="450" height="50">
