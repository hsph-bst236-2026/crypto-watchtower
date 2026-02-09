---
mode: 'agent'
description: 'Commit all generated files and push to GitHub to deploy via GitHub Pages'
tools: ['terminalLastCommand']
---

# Deploy to GitHub Pages

Commit all generated files and push to GitHub to trigger a Pages deployment.

## Task

Run these commands:

```bash
# Stage all generated files
git add crypto_raw.json volatile_movers.json volatility_report.json market_chart.png index.html daily_brief.txt generate_chart.py 2>/dev/null || true
git add -A

# Commit with timestamp
git commit -m "📊 Market update: $(date '+%Y-%m-%d %H:%M %Z')"

# Push to origin
git push origin main
```

## Prerequisites
- Git repository initialized
- Remote origin configured
- GitHub Pages enabled in repository settings (Settings → Pages → Source: main branch)

## Validation

After pushing:
1. Confirm push was successful
2. Report the GitHub Pages URL: `https://<username>.github.io/<repo>/`
3. Note that it may take 1-2 minutes for changes to appear

## Notes
- If no changes to commit, that's okay - report "No new changes"
- If push fails, check authentication and remote configuration
