# Zapier Filter Setup for Status = "Ready"

## Option 1: Built-in Notion Trigger Filter (Recommended)

If your Notion database has a "Status" property:

1. In the **Notion trigger** step, look for **"Set up trigger"** or **"Customize trigger"**
2. Add a filter condition:
   - **Property**: Status
   - **Condition**: "is"
   - **Value**: Ready
3. Save the trigger

**Note**: Not all Zapier integrations support built-in filters. If you don't see this option, use Option 2.

---

## Option 2: Separate Filter Step

Add a **Filter by Zapier** step between Notion trigger and Webhook:

### Step Configuration:

1. **App**: Filter by Zapier
2. **Event**: Only continue if...

### Filter Conditions:

**Option A: Simple Text Match**
- **Field**: `{{1.Status}}`
- **Condition**: "Text is exactly"
- **Value**: `Ready`

**Option B: Case-Insensitive**
- **Field**: `{{1.Status}}`
- **Condition**: "Text contains" (case-insensitive)
- **Value**: `ready`

**Option C: Multiple Status Values**
- Use "OR" conditions:
  - `{{1.Status}}` is exactly "Ready"
  - OR `{{1.Status}}` is exactly "Process"
  - OR `{{1.Status}}` is exactly "Active"

### Complete Filter Setup:

```
┌─────────────────┐
│  Notion Trigger │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Filter Step     │  Only if Status = "Ready"
│  (Skip if not)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Webhook Action │
└─────────────────┘
```

---

## Option 3: Code Step (Advanced)

If you need more complex logic:

1. **App**: Code by Zapier
2. **Event**: Run Python
3. **Code**:
```python
status = input_data.get('Status', '')

if status == 'Ready':
    return {'continue': True}
else:
    return {'continue': False}
```

4. Add a **Filter** step after:
   - Only continue if `{{2.continue}}` is `True`

---

## Testing the Filter

1. Create test entries in Notion:
   - Entry 1: Status = "Ready" → Should trigger
   - Entry 2: Status = "Draft" → Should NOT trigger
   - Entry 3: Status = "Pending" → Should NOT trigger

2. Run test in Zapier
3. Verify only "Ready" entries trigger the webhook

---

## Recommended: Use Option 1 or 2

- **Option 1** is simplest if available
- **Option 2** works universally and is easy to understand
- **Option 3** only if you need complex logic

---

**Quick Answer**: Add a **Filter by Zapier** step with condition: `{{1.Status}}` is exactly `"Ready"`

