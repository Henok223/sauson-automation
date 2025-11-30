# GitLab Setup - Authentication Required

## Git Push Failed - Need Authentication

GitLab requires authentication to push. Here are your options:

## Option 1: Use Personal Access Token (Recommended)

### Step 1: Create Personal Access Token

1. Go to: https://gitlab.com/-/user_settings/personal_access_tokens
2. Click **"Add new token"**
3. **Token name:** `slauson-automation`
4. **Scopes:** Check `write_repository`
5. **Expiration:** Set as needed
6. Click **"Create personal access token"**
7. **Copy the token** (you'll only see it once!)

### Step 2: Use Token in Git URL

```bash
cd ~/slauson-automation
git remote set-url origin https://oauth2:YOUR_TOKEN@gitlab.com/hmikaeltewolde-group/hmikaeltewolde-project.git
git push -uf origin main
```

Replace `YOUR_TOKEN` with the token you copied.

---

## Option 2: Use SSH (More Secure)

### Step 1: Generate SSH Key (if you don't have one)

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# Press Enter to accept defaults
```

### Step 2: Add SSH Key to GitLab

1. Copy your public key:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

2. Go to: https://gitlab.com/-/user_settings/ssh_keys
3. Paste your public key
4. Click **"Add key"**

### Step 3: Change Remote to SSH

```bash
cd ~/slauson-automation
git remote set-url origin git@gitlab.com:hmikaeltewolde-group/hmikaeltewolde-project.git
git push -uf origin main
```

---

## Option 3: Use Git Credential Helper

```bash
git config --global credential.helper store
git push -uf origin main
# Enter your GitLab username and password/token when prompted
```

---

## Quick Push (After Authentication)

Once authenticated, push:

```bash
cd ~/slauson-automation
git push -uf origin main
```

---

## Verify Push

After pushing, check GitLab:
- Go to: https://gitlab.com/hmikaeltewolde-group/hmikaeltewolde-project
- You should see all your files

---

**I recommend Option 1 (Personal Access Token) - it's the easiest!**

