---
mode: 'agent'
description: 'Fetch top 50 cryptocurrencies from CoinGecko API and save to crypto_raw.json'
tools: ['terminalLastCommand']
---

# Fetch Crypto Data

Use `curl` to fetch the current top 50 cryptocurrencies by market cap from the CoinGecko API.

## Task

Run this command:

```bash
curl -s "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&sparkline=false" -o crypto_raw.json
```

## Validation

After fetching, verify the data:
1. Check the file exists and has content
2. Validate it's a JSON array with `jq 'length' crypto_raw.json` (should return 50)
3. Report the top 3 coins by market cap

## Output
- File: `crypto_raw.json`
- Content: Array of 50 coin objects with price data
