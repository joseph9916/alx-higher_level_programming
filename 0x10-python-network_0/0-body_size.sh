#!/bin/bash
#Write a Bash script that takes in a URL, sends a request to that URL,
curl -w '%{size_download}' -s -o /dev/null "$1"; echo ""
