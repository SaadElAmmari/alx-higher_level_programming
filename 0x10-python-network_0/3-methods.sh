#!/bin/bash
# display all http methods the server will accept using curl.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
