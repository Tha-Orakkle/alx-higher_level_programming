#!/bin/bash
# takes in a URL as an argument, sends a POST request to the URL, and displays the body of the response
curl -sL -X PUT -d "You got me!" http://0.0.0.0:5000/catch_me | grep "You got me!" | cut -d "'" -f 2 | cut -c -11 | tr -d '\n'
