---
mode: 'agent'
description: 'Set up GitHub repository, commit all files, and deploy to GitHub Pages for hsph-bst236-2026 organization'
tools: ['terminalLastCommand']
---

# Deploy to GitHub Pages

Set up the GitHub repository and deploy the Crypto Watchtower dashboard.

## Task

### Step 1: Create GitHub Repository (if not exists)
Using GitHub CLI or web interface, create a repo in the `hsph-bst236-2026` organization:
```bash
# Check if gh CLI is available and authenticated
gh auth status

# Create repo in organization (if not exists)
gh repo create hsph-bst236-2026/crypto-watchtower --public --source=. --remote=origin --push
```

### Step 2: If repo already exists, add remote and push
```bash
# Add remote (skip if already added)
git remote add origin https://github.com/hsph-bst236-2026/crypto-watchtower.git 2>/dev/null || true

# Push to main branch
git push -u origin main
```

### Step 3: Enable GitHub Pages
```bash
# Enable Pages via GitHub CLI (requires gh-pages extension or API)
gh api repos/hsph-bst236-2026/crypto-watchtower/pages -X POST -f source='{"branch":"main","path":"/"}' 2>/dev/null || echo "Pages may already be enabled or requires manual setup"
```

### Alternative: Manual GitHub Pages Setup
If CLI doesn't work, instruct user to:
1. Go to https://github.com/hsph-bst236-2026/crypto-watchtower/settings/pages
2. Under "Source", select "Deploy from a branch"
3. Select branch: `main`, folder: `/ (root)`
4. Click Save

## Validation

After deployment:
1. Confirm push was successful
2. Report the GitHub Pages URL: `https://hsph-bst236-2026.github.io/crypto-watchtower/`
3. Note: Site may take 1-2 minutes to go live

## Prerequisites
- Git repository initialized with committed files
- GitHub CLI (`gh`) authenticated with org access, OR
- Manual access to organization repository settings
