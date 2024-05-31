#!/bin/bash

source ./myvenv/bin/activate
bash -c 'python camping.py --start-date 2024-06-07 --end-date 2024-06-09 --parks 232769 | python telegram_notifier.py 2>&1 > /tmp/mylog'