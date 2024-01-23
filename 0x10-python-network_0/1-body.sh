#!/bin/bash
# Script that takes in a URL, sends a GET request to that URL, and displays the body of the response if the status code is 200
response=$(curl -s -o /dev/null -w "%{http_code}" "$1"); [ "$response" -eq 200 ] && curl -sL "$1"
