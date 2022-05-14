# eBird friend stalking - Discord version

**For normal version please check [here](..)**

This version has been created to be executed on a server in order to send Discord notifications every day as a recap of the day.

## How can you make it work?

First you need to have a API key for eBird. It can be easily requested [here](https://ebird.org/api/keygen) by filling out the form.

Once your have your key you need to place it in the python code. At this step you also add the name on eBird of your friends.
The fields to modify are at the top of [discord/main.py](./main.py):

```python
api_key = 'XXXXXXXXXXXX' #Paste your eBirdApiToken here
myfriends = ["NAME HERE"] #Put the name of your friends in here.
```

You then need to add a default zone, and a default language for the results.
This is done by modifying the bottom lines of [discord/main.py](./main.py):

```python
location = "SE" #Change your location here
locale = "en"  #Put the language you want here.
```


Finally you will need to have to get a Webhook URL for in a channel on Discord.

To get it: 'Edit Channel > Integrations > Webhooks'

Then add your Webhook at the end of [discord/main.py](./main.py):
```python
notifier = dn.Notifier('WEBHOOK URL') #Add your webhook url here.
```

You can test your modifications at this point to check if everything is working correctly.

After waiting few seconds you will receive a mesasge on the channel !!! :)


## Autorun of the script

To get a daily recap of yesterday activity of your friends you can run the script as a cron job on a server.

To add it in the cron job just run the [setup script](./setup.sh). *This may require sudo privileges*.

```bash
sudo ./setup.sh
```

The script will display the final crontab list.

The default execution time with this script is 06:00.
