#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept
curl -sI -X OPTIONS "$1" | grep Allow | cut -d' ' -f1 --complement
