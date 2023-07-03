#!/bin/bash
# Displays all the HTTP methods the server will accept
curl -sI "$1" | grep -E "Allow" | cut -c 8-
