# Status Field - How to Trigger Automation

## Quick Answer

**It depends on your Zapier setup!** Here are the options:

---

## Option 1: Trigger on New Entry (Recommended for Testing)

**Zapier Trigger**: "New Database Item"

**Status Value**: `pending` (or any value - status doesn't matter)

**How it works**:
- Zapier triggers **automatically** when you create a new entry
- Status value doesn't matter - it will process regardless
- Set status to `pending` initially
- Automation will update it to `completed` when done

**Best for**: Testing and simple workflows

---

## Option 2: Trigger When Status = "Ready" (Recommended for Production)

**Zapier Trigger**: "New Database Item" + Filter

**Status Value**: `Ready` (exact match required)

**How it works**:
1. Create entry with status = `pending` (or leave empty)
2. Fill in all required fields
3. Upload images (headshot_url, logo_url)
4. **Change status to `Ready`**
5. Zapier detects the change and triggers automation

**Zapier Filter Setup**:
- Add a **Filter by Zapier** step
- Condition: `{{1.Status}}` is exactly `Ready`
- Only continue if condition matches

**Best for**: Production - gives you control over when to process

---

## Option 3: Trigger on Status Update

**Zapier Trigger**: "Updated Database Item"

**Status Value**: `Ready` (when you want to trigger)

**How it works**:
- Zapier triggers when **any** field is updated
- Add filter: Only if Status = `Ready`
- Change status from `pending` → `Ready` to trigger

**Best for**: Re-processing entries or manual control

---

## Recommended Setup for You

### For Testing (Right Now):
1. **Zapier Trigger**: "New Database Item" (no filter)
2. **Set Status to**: `pending`
3. **Create a new entry** with all fields filled
4. **Zapier will trigger automatically**

### For Production (Later):
1. **Zapier Trigger**: "New Database Item" + Filter
2. **Filter**: Status = `Ready`
3. **Workflow**:
   - Create entry with status = `pending`
   - Fill in all fields
   - Upload images
   - **Change status to `Ready`** ← This triggers automation
   - Automation updates status to `completed`

---

## Status Values Reference

| Status Value | When to Use | What Happens |
|--------------|-------------|--------------|
| `pending` | Initial state | Entry created, waiting to process |
| `Ready` | Ready to process | Triggers automation (if filter set) |
| `processing` | During automation | (Optional - you can add this) |
| `completed` | After automation | Set automatically by code |
| `error` | If something fails | (Optional - you can add this) |

---

## Quick Decision Tree

```
Do you want automation to run automatically when you create a new entry?
├─ YES → Use "New Database Item" trigger (no filter)
│         Set Status = `pending` (or any value)
│
└─ NO → Use "New Database Item" + Filter (Status = "Ready")
        Set Status = `pending` initially
        Change to `Ready` when ready to process
```

---

## For Your Current Test

**Set Status to**: `pending`

**Zapier Setup**: 
- Trigger: "New Database Item"
- No filter needed for testing

**Then**:
1. Create new entry in Notion
2. Fill in all fields
3. Upload images
4. Set Status = `pending`
5. Zapier will trigger automatically
6. Status will be updated to `completed` when done

---

## Summary

- **For testing**: Set Status = `pending`, use "New Database Item" trigger (no filter)
- **For production**: Set Status = `Ready` when ready, use filter in Zapier
- **Status doesn't affect webhook processing** - it's just for Zapier filtering

**Right now, just set it to `pending` and create a new entry!** 🚀


