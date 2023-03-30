#!/bin/bash
# Send a POST request to a given URL with a header variable.
curl -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST "$1"
