#!/usr/bin/env bash
# sends a POST request wth variables, and displays the body of the response
curl -s -X POST -d "email: test@gmail.com" -d "subject: I will always be here for PLD" "$1"
