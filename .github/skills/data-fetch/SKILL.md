---
name: data-fetch
description: Guide for fetching cryptocurrency market data from CoinGecko API using curl. Use this when asked to retrieve live crypto prices or market data.
---

# Data Fetch Skill: CoinGecko API with curl

## Overview
This skill covers fetching live cryptocurrency market data using the CoinGecko public API and the `curl` command-line tool.

## API Endpoint

**Base URL:** `https://api.coingecko.com/api/v3`

**Market Data Endpoint:**
```
GET /coins/markets
```

## Required Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `vs_currency` | `usd` | Quote currency for prices |
| `order` | `market_cap_desc` | Sort by market cap descending |
| `per_page` | `50` | Number of coins to fetch |
| `sparkline` | `false` | Disable sparkline data (smaller response) |

## curl Command

### Basic Fetch
```bash
curl -s "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&sparkline=false" -o crypto_raw.json
```

### With Headers (recommended for reliability)
```bash
curl -s \
  -H "Accept: application/json" \
  -H "User-Agent: CryptoWatchtower/1.0" \
  "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&sparkline=false" \
  -o crypto_raw.json
```

## curl Flags Explained

| Flag | Purpose |
|------|---------|
| `-s` | Silent mode (no progress bar) |
| `-o <file>` | Write output to file |
| `-H` | Add HTTP header |
| `-w "%{http_code}"` | Print HTTP status code |
| `--retry 3` | Retry failed requests |

## Response Structure

Each coin object contains:
```json
{
  "id": "bitcoin",
  "symbol": "btc",
  "name": "Bitcoin",
  "current_price": 45000.00,
  "market_cap": 850000000000,
  "price_change_percentage_24h": 2.5,
  "total_volume": 25000000000,
  "high_24h": 46000.00,
  "low_24h": 44000.00
}
```

## Error Handling

### Rate Limiting
CoinGecko limits requests. If rate limited (HTTP 429):
```bash
# Check status and retry
STATUS=$(curl -s -w "%{http_code}" -o crypto_raw.json "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50")
if [ "$STATUS" = "429" ]; then
  echo "Rate limited. Waiting 60 seconds..."
  sleep 60
  curl -s "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50" -o crypto_raw.json
fi
```

### Validate Response
```bash
# Check if valid JSON array
jq 'type' crypto_raw.json  # Should output: "array"
jq 'length' crypto_raw.json  # Should output: 50
```

## Common Issues

1. **Empty response**: Check internet connection
2. **Rate limited (429)**: Wait 60 seconds, or use API key
3. **Invalid JSON**: API might be down, check status page
4. **Timeout**: Add `--max-time 30` flag
