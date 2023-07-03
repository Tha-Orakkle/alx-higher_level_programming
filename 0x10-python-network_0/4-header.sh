#!/bin/bash
# sends a GET request with a header variable to the URL
curl -s -H "X-School-User-Id: 98" "$1"
