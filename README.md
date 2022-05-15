# eBird friends stalking

Python code to check if your friends have seen some nice birds.

**A version using Discord notification is available [here](./discord).**


## How can you make it work?

First install the required libraries:
```bash
pip3 install -r requirements.txt
```

Then you need to have a API key for eBird. It can be easily requested [here](https://ebird.org/api/keygen) by filling out the form.


Once your have your key you need to place it in the python code. At this step you also add the name on eBird of your friends.
The fields to modify are at the top of [main.py](./main.py):

```python
api_key = 'XXXXXXXXXXXX' #Paste your eBirdApiToken here
myfriends = ["NAME HERE"] #Put the name of your friends in here.
```

Once you have done this you can run it in your terminal on Linux with the command:
```bash
python3 main.py
```
 Or by any other way you like to run your python code.


 It will prompt you for the region you want to scan and for the date and you can choose the language in which the name of the birds will be display:
 ```
 Zone?
 SE                       #example of a zone
 Date? ((d)d/(m)m/yyyy)
 12/5/2022                #example of a date
 Language? (default = en)
 fr                       #example of a language choice
 ```
Default date is today.

Note: the available languages and code can be found [here](https://support.ebird.org/en/support/solutions/articles/48000804865-bird-names-in-ebird) (*You may need to change the language of the support page to english to access this link*)


After waiting few seconds you will get your result !!! :)


## What's next?

* Add some the count for species
* Add locations of observation
