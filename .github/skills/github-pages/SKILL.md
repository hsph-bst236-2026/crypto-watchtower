---
name: github-pages
description: Guide for deploying static websites to GitHub Pages. Use this when asked to publish HTML dashboards, commit changes, or deploy to the web.
---

# GitHub Pages Skill: Static Site Deployment

## Overview
This skill covers generating HTML dashboards, Git version control, and deploying to GitHub Pages for the Crypto Watchtower project.

## HTML Dashboard Template

### Complete Dark-Mode Dashboard
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔥 Crypto Watchtower</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #1a1a2e;
            color: #eeeeee;
            line-height: 1.6;
            padding: 20px;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        header {
            text-align: center;
            padding: 40px 0;
            border-bottom: 1px solid #333;
        }
        h1 { font-size: 2.5rem; margin-bottom: 10px; }
        .timestamp { color: #888; font-size: 0.9rem; }
        .chart-container {
            margin: 40px 0;
            text-align: center;
        }
        .chart-container img {
            max-width: 100%;
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #333;
        }
        th { background: #16213e; color: #4cc9f0; }
        tr:hover { background: #16213e; }
        .gain { color: #00ff88; }
        .loss { color: #ff4444; }
        footer {
            text-align: center;
            padding: 40px 0;
            color: #666;
            font-size: 0.8rem;
        }
        @media (max-width: 768px) {
            h1 { font-size: 1.8rem; }
            th, td { padding: 8px; font-size: 0.9rem; }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🔥 Crypto Watchtower</h1>
            <p class="timestamp">Last updated: <span id="timestamp"></span></p>
        </header>
        
        <section class="chart-container">
            <h2>📊 Market Movers (24h)</h2>
            <img src="market_chart.png" alt="Market Movers Chart">
        </section>
        
        <section class="data-table">
            <h2>📋 Volatile Coins</h2>
            <table id="coins-table">
                <thead>
                    <tr>
                        <th>Coin</th>
                        <th>Symbol</th>
                        <th>Price (USD)</th>
                        <th>24h Change</th>
                    </tr>
                </thead>
                <tbody></tbody>
            </table>
        </section>
        
        <footer>
            <p>Data from CoinGecko API • Built with AI Agents</p>
        </footer>
    </div>
    
    <script>
        // Set timestamp
        document.getElementById('timestamp').textContent = new Date().toLocaleString();
        
        // Load and display coin data
        fetch('volatile_movers.json')
            .then(r => r.json())
            .then(coins => {
                const tbody = document.querySelector('#coins-table tbody');
                coins.sort((a, b) => b.price_change_percentage_24h - a.price_change_percentage_24h);
                coins.forEach(coin => {
                    const change = coin.price_change_percentage_24h;
                    const changeClass = change > 0 ? 'gain' : 'loss';
                    const changeSign = change > 0 ? '+' : '';
                    tbody.innerHTML += `
                        <tr>
                            <td>${coin.name}</td>
                            <td>${coin.symbol.toUpperCase()}</td>
                            <td>$${coin.current_price.toLocaleString()}</td>
                            <td class="${changeClass}">${changeSign}${change.toFixed(2)}%</td>
                        </tr>
                    `;
                });
            })
            .catch(err => console.error('Failed to load data:', err));
    </script>
</body>
</html>
```

## Git Workflow

### Initial Setup
```bash
# Initialize if needed
git init

# Configure GitHub Pages in repository settings:
# Settings → Pages → Source: Deploy from branch → main → / (root)
```

### Commit & Deploy
```bash
# Stage all generated files
git add crypto_raw.json volatile_movers.json volatility_report.json
git add market_chart.png index.html daily_brief.txt

# Commit with timestamp message
git commit -m "📊 Market update: $(date '+%Y-%m-%d %H:%M %Z')"

# Push to trigger GitHub Pages deployment
git push origin main
```

### Automated Update Script
```bash
#!/bin/bash
# update_and_deploy.sh

set -e  # Exit on error

echo "🔄 Fetching latest data..."
curl -s "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50" -o crypto_raw.json

echo "🔍 Filtering volatile coins..."
jq '[.[] | select(.price_change_percentage_24h > 5 or .price_change_percentage_24h < -5) | {name, symbol, current_price, price_change_percentage_24h, market_cap}]' crypto_raw.json > volatile_movers.json

echo "📊 Generating chart..."
python generate_chart.py

echo "📤 Deploying to GitHub Pages..."
git add -A
git commit -m "📊 Auto-update: $(date '+%Y-%m-%d %H:%M %Z')" || echo "No changes to commit"
git push origin main

echo "✅ Done! Site will update in ~1 minute."
```

## GitHub Pages Configuration

### Via Repository Settings
1. Go to repository **Settings**
2. Navigate to **Pages** section
3. Set **Source**: Deploy from a branch
4. Select **Branch**: `main` (or `gh-pages`)
5. Select **Folder**: `/ (root)`
6. Click **Save**

### Custom Domain (Optional)
```bash
# Create CNAME file
echo "crypto.yourdomain.com" > CNAME
git add CNAME && git commit -m "Add custom domain"
```

## Deployment Checklist

- [ ] All files committed (JSON, PNG, HTML)
- [ ] No large files (>100MB limit)
- [ ] `index.html` exists in root
- [ ] Image paths are relative (not absolute)
- [ ] GitHub Pages enabled in settings
- [ ] Branch is correct (main or gh-pages)

## Common Issues

| Issue | Solution |
|-------|----------|
| 404 on site | Check index.html exists in root |
| Images not loading | Use relative paths: `src="market_chart.png"` |
| Old content shown | Hard refresh (Ctrl+Shift+R) or wait 5 min |
| Build failed | Check Actions tab for error details |
| CORS error on JSON | Host JSON on same domain or use JSONP |

## Site URL
After deployment, your site will be available at:
```
https://<username>.github.io/<repository>/
```
