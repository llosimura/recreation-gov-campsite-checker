# -*- coding: utf-8 -*-
import json
import sys
import requests
from datetime import datetime

from enums.emoji import Emoji

CREDENTIALS_FILE = "./slack_config.json"

def _send_slack_message(message):
    with open(CREDENTIALS_FILE) as f:
        sc = json.load(f)

        url = sc["url"]
        payload = {
            "text": message,
        }
        headers = {
            'Content-Type': 'application/json',
        }
        requests.post(url, data=json.dumps(payload), headers=headers)

        # api.CreateFavorite(resp)
        print("The following was sent: ")
        print()
        print(message)


def main(args, stdin):
    first_line = next(stdin)

    if "Something went wrong" in first_line:
        _send_slack_message("{}, I'm broken! Please help")
        sys.exit()

    available_site_strings = generate_availability_strings(stdin)
    if available_site_strings:
        message = generate_msg_str(available_site_strings, first_line, )
        _send_slack_message(message)
        with open("logs.txt", "a") as log:
            log.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} - Campsite found\n")
        sys.exit(0)
    else:
        with open("logs.txt", "a") as log:
            log.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} - No found\n")
        print("No campsites available, not sending message 😞")
        sys.exit(1)


def generate_msg_str(available_site_strings, first_line):
    message = first_line.rstrip()
    message += " 🏕🏕🏕\n"
    message += "\n".join(available_site_strings)
    message += "\n"
    return message


def generate_availability_strings(stdin):
    available_site_strings = []
    for line in stdin:
        line = line.strip()
        if Emoji.SUCCESS.value in line:
            park_name_and_id = " ".join(line.split(":")[0].split(" ")[1:])
            num_available = line.split(":")[1][1].split(" ")[0]
            s = "{} site(s) available in {}".format(
                num_available, park_name_and_id
            )
            available_site_strings.append(s)
    return available_site_strings


if __name__ == "__main__":
    main(sys.argv, sys.stdin)
