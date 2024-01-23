#!/bin/bash
# Script that displays all HTTP methods accepted by a server
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
