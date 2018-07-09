#!/bin/bash -e

host=http://yz-gpu007.hogpu.cc:8000/graphql
query='{"query": "{ allMessages {message, creationDate}}"}'

curl \
 -X POST \
 -H "Content-Type: application/json" \
 --data "$query" \
 "$host" 
