---
name: github-deploy
description: Guide for deploying projects to GitHub and GitHub Pages for the hsph-bst236-2026 organization. Use this when asked to deploy, publish, or push to GitHub.
---

# GitHub Deployment Skill: hsph-bst236-2026 Organization

## Overview
This skill covers deploying projects to GitHub repositories within the `hsph-bst236-2026` organization and enabling GitHub Pages for static site hosting.

## Organization Details

| Property | Value |
|----------|-------|
| Organization | `hsph-bst236-2026` |
| GitHub URL | `https://github.com/hsph-bst236-2026` |
| Pages URL Pattern | `https://hsph-bst236-2026.github.io/<repo>/` |

## GitHub CLI Setup

### Check Authentication
```bash
# Verify gh CLI is installed and authenticated
gh auth status

# Login if needed (will open browser)
gh auth login
```

### Authenticate with Organization Access
```bash
# Ensure you have org access
gh auth refresh -s admin:org
```

## Repository Creation

### Create New Repo in Organization
```bash
# Create public repo with current directory as source
gh repo create hsph-bst236-2026/crypto-watchtower \
  --public \
  --source=. \
  --remote=origin \
  --push \
  --description "24/7 Crypto Market Watchtower Dashboard"
```

### Clone Existing Repo
```bash
git clone https://github.com/hsph-bst236-2026/crypto-watchtower.git
cd crypto-watchtower
```

### Add Remote to Existing Local Repo
```bash
# Initialize git if needed
git init

# Add organization remote
git remote add origin https://github.com/hsph-bst236-2026/crypto-watchtower.git

# Verify remote
git remote -v
```

## Commit & Push Workflow

### Standard Update
```bash
# Stage all changes
git add -A

# Commit with descriptive message
git commit -m "📊 Market update: $(date '+%Y-%m-%d %H:%M %Z')"

# Push to main branch
git push -u origin main
```

### Force Push (use carefully)
```bash
git push -f origin main
```

## GitHub Pages Configuration

### Enable via GitHub CLI
```bash
# Enable Pages on main branch, root folder
gh api repos/hsph-bst236-2026/crypto-watchtower/pages \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -f build_type=legacy \
  -f source='{"branch":"main","path":"/"}'
```

### Check Pages Status
```bash
gh api repos/hsph-bst236-2026/crypto-watchtower/pages
```

### Manual Setup (via Web)
1. Navigate to: `https://github.com/hsph-bst236-2026/crypto-watchtower/settings/pages`
2. Under **Build and deployment**:
   - Source: "Deploy from a branch"
   - Branch: `main`
   - Folder: `/ (root)`
3. Click **Save**
4. Wait 1-2 minutes for initial deployment

## Deployment URLs

After enabling Pages, the site will be available at:
```
https://hsph-bst236-2026.github.io/crypto-watchtower/
```

## Required Files for Pages

Ensure these exist in the repository root:
- `index.html` — Main entry point (required)
- `market_chart.png` — Chart image
- `volatile_movers.json` — Data file (if using fetch)

## Common Issues

| Issue | Solution |
|-------|----------|
| "Permission denied" | Check org membership and repo permissions |
| "Repository not found" | Verify org name and repo exists |
| "Pages not building" | Check Actions tab for build errors |
| "404 on site" | Ensure `index.html` exists in root |
| "Authentication failed" | Run `gh auth login` or use SSH key |

## SSH vs HTTPS

### HTTPS (recommended for classroom)
```bash
git remote set-url origin https://github.com/hsph-bst236-2026/crypto-watchtower.git
```

### SSH (if configured)
```bash
git remote set-url origin git@github.com:hsph-bst236-2026/crypto-watchtower.git
```

## Automation with GitHub Actions

For automated updates, create `.github/workflows/update.yml`:
```yaml
name: Update Dashboard
on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours
  workflow_dispatch:  # Manual trigger

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Fetch and update data
        run: |
          curl -s "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50" -o crypto_raw.json
          # Add more pipeline steps...
      - name: Commit and push
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add -A
          git commit -m "🤖 Auto-update: $(date -u '+%Y-%m-%d %H:%M UTC')" || exit 0
          git push
```
