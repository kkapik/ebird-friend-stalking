#!/bin/bash

tmpfile=$(mktemp)
crontab -l >"$tmpfile"
printf '%s\n' "00 06  * * * python3 $PWD/main.py" >>"$tmpfile"
crontab "$tmpfile" && rm -f "$tmpfile"
crontab -l
