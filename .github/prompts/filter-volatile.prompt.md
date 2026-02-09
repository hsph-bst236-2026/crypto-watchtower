---
mode: 'agent'
description: 'Filter crypto_raw.json to find coins with >5% price change and save to volatile_movers.json'
tools: ['terminalLastCommand']
---

# Filter Volatile Coins

Use `jq` to filter the raw crypto data and identify volatile market movers.

## Task

Run this command to filter coins with more than ±5% price change in 24 hours:

```bash
jq '[.[] | select(.price_change_percentage_24h > 5 or .price_change_percentage_24h < -5) | {name, symbol, current_price, price_change_percentage_24h, market_cap}]' crypto_raw.json > volatile_movers.json
```

## Prerequisites
- `crypto_raw.json` must exist (run fetch-crypto prompt first)

## Validation

After filtering:
1. Count results with `jq 'length' volatile_movers.json`
2. Show the top gainer and top loser
3. If no volatile coins found, report "Market is calm today"

## Output
- File: `volatile_movers.json`
- Content: Array of volatile coins with selected fields only
