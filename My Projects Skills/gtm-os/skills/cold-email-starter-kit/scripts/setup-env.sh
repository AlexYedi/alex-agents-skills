#!/usr/bin/env bash
# Interactive .env bootstrap.
# Usage: bash scripts/setup-env.sh

set -e
cd "$(dirname "$0")/.."

ENV_FILE=".env"
if [ -f "$ENV_FILE" ]; then
  echo ".env already exists. Edit it directly or delete it first."
  exit 1
fi

if [ -f ".env.example" ]; then
  cp .env.example "$ENV_FILE"
  echo "Created .env from .env.example"
  echo ""
  echo "Now open .env in your editor and fill in your API keys."
  echo "Instructions for each service:"
  echo "  Dynadot:    https://www.dynadot.com/account → Tools → API → copy key + whitelist IP"
  echo "  Zapmail:    https://zapmail.ai → Settings → API → copy token"
  echo "  Prospeo:    https://prospeo.io → Dashboard → Integrations → API → copy key"
  echo "  Smartlead:  https://app.smartlead.ai → Settings → API Keys → Create"
  echo "  Instantly:  https://app.instantly.ai → Settings → Integrations → API Keys"
  echo ""
  echo "After editing, run:  npx tsx scripts/verify-credentials.ts"
else
  echo "No .env.example found. You're missing skill files."
  exit 1
fi
