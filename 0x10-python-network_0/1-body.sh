#!/bin/bash
# Script that takes in a URL, sends a GET request to that URL, and displays the body of the response if the status code is 200
curl -s "$1"
