Substationfinder
==================
## Overview
The Substationfinder is a Telegrammbot that can show you the locations and routs
to German Substations. The bot knows over 300 Substations in the 380kV and 220kV Voltage level.

## Usage
- Download [Telegramm](https://telegram.org/)
- New Message
- Search Substationfinder
- write Message: **/start**
- write Message for instance: **Berlin**
- get reply with Google and Waze link

## Data source
[Umspannwerke in Deutschland](https://de.wikipedia.org/wiki/Liste_der_Schaltanlagen_im_H%C3%B6chstspannungsnetz_in_Deutschland)

## Contribution
If you have any issue with the bot feel free to send a pull request.
For datainconsistent please fix it first in the German [Wikipedia](https://de.wikipedia.org/wiki/Liste_der_Schaltanlagen_im_H%C3%B6chstspannungsnetz_in_Deutschland).

- Install [Telegramm](https://telegram.org/)
- create own bot write Message **/newbot** to BotFather and follow the instruction
- Copy the key in a new file called production.ini (find example of the format in the example.ini)
- install requirements
- start with **python main.py**

## known issues
Some Substations are not in the Database for instance Knapsack. Feel free to add them to the Wikipedia.
Some locations are not that accurate.

## Requirements
- Python 3.X
- python-telegram-bot
- ...
- Pip install -r requirements.txt

## License
- CDDL
