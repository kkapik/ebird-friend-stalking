# eBird friend stalking

Small Python code to check if my friends have seen some nice birds today.


## How can you make it work?

First you need to have a API key for eBird. It can be easily requested [here](https://ebird.org/api/keygen) by filling out the form.

Once your have your key you need to place it in the python code. At this step you also add the name on eBird of your friends.
The fields to modify are on line 6 and 7:

```python
api_key = 'XXXXXXXXXXXX' #Paste your eBirdApiToken here
myfriends = ["NAME HERE"] #Put the name of your friends in here.
```

Once you have done this you can run it in your terminal on Linux with the command:
```bash
python3 friendobservation.py
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


After waiting few seconds you will get your result !!! :)


## What's next?

* Add some the count for species
* Add locations of observation
