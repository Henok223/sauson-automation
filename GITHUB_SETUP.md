# GitHub Setup Instructions

## Step 1: Create GitHub Repository

1. Go to: https://github.com/new
2. **Repository name:** `slauson-automation` (or any name you prefer)
3. **Description:** "Portfolio onboarding automation for Slauson & Co."
4. **Visibility:** Private (recommended) or Public
5. **DO NOT** initialize with README, .gitignore, or license (we already have files)
6. Click **"Create repository"**

## Step 2: Get Your Repository URL

After creating, GitHub will show you the repository URL. It will look like:
```
https://github.com/YOUR_USERNAME/slauson-automation.git
```

Or SSH:
```
git@github.com:YOUR_USERNAME/slauson-automation.git
```

## Step 3: Add GitHub Remote and Push

Once you have your repository URL, run:

```bash
cd ~/slauson-automation
git remote add origin https://github.com/YOUR_USERNAME/slauson-automation.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your GitHub username!**

## Authentication

GitHub may ask for authentication. Options:

### Option 1: Personal Access Token (Recommended)

1. Go to: https://github.com/settings/tokens
2. Click **"Generate new token"** → **"Generate new token (classic)"**
3. **Note:** `slauson-automation`
4. **Expiration:** Choose duration
5. **Scopes:** Check `repo` (full control of private repositories)
6. Click **"Generate token"**
7. **Copy the token** (you'll only see it once!)

When pushing, use the token as your password:
```bash
git push -u origin main
# Username: your_github_username
# Password: paste_your_token_here
```

### Option 2: Use SSH

1. Generate SSH key (if needed):
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

2. Add to GitHub:
   - Copy: `cat ~/.ssh/id_ed25519.pub`
   - Go to: https://github.com/settings/ssh/new
   - Paste and add

3. Use SSH URL:
   ```bash
   git remote set-url origin git@github.com:YOUR_USERNAME/slauson-automation.git
   git push -u origin main
   ```

## After Pushing

Your code will be on GitHub and you can:
- Deploy to Render using GitHub
- Share with team
- Version control
- Backup your code

---

**Create the GitHub repo first, then share the URL and I'll help you push!**

