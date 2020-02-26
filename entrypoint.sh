#!/bin/bash

error() {
  echo "You need to define DEFAULT_BOT_TOKEN, DEFAULT_CHAT_ID or Create 'config.yaml'" >&2;
  exit 1;
}

if [ -z "$DEFAULT_BOT_TOKEN" ] || [ -z "$DEFAULT_CHAT_ID" ]; then
  error
fi

exec "$@"
