# Description vs Background - Field Differences

## Based on Your Slide Design

Looking at your slide design, here's how these fields are used:

### `description` - Short Description
- **Purpose**: Brief company description (1-2 sentences)
- **Location on slide**: Usually near the company name or in a summary section
- **Length**: Short, concise overview
- **Example**: "Loamy is a vertical SaaS AgTech platform designed to help the agricultural supply chain reduce waste."

### `background` - Detailed Background Section
- **Purpose**: Longer, detailed company background/description
- **Location on slide**: In the "Background" section (the yellow-highlighted section you showed)
- **Length**: Full paragraph with more details
- **Example**: "Loamy is a vertical SaaS AgTech platform designed to help the agricultural supply chain reduce waste, improve efficiencies, and increase margins. The company is founded by Charles Julius and Jason Pesek, who have product management backgrounds and met while working at Motive (fka KeepTruckin), a fleet management software company."

## In Your Slide Design

From the slide you showed me:
- **Description**: Would be a shorter text near the company name
- **Background**: The longer paragraph in the yellow "Background" section with detailed company information

## How the Code Handles It

```python
"description": company_data.get("description", ""),  # Short description
"background": company_data.get("background", company_data.get("description", "")),  # Long background (falls back to description if not provided)
```

**Note**: If `background` is not provided in the webhook data, it will use `description` as a fallback.

## What You Need to Do

### Option 1: Use Both Fields (Recommended)
- **`description`**: Link to a shorter text element (1-2 sentences)
- **`background`**: Link to the longer "Background" section paragraph

### Option 2: Use Only One Field
- If you only have one description field in your template:
  - Use `background` for the longer text
  - Leave `description` empty or use the same field for both

## Recommendation

Based on your slide design:
- **`description`**: Use for a short tagline/summary near the company name
- **`background`**: Use for the detailed paragraph in the "Background" section

If your template only has one description field (the Background section), you can:
1. Link it to `background` field
2. Leave `description` unlinked (or link it to the same element)

## In Your Canva Data Autofill Setup

When linking fields:
- If you have **two text elements** (short + long):
  - Short description → `description`
  - Long background paragraph → `background`
  
- If you have **one text element** (just the Background section):
  - Background paragraph → `background`
  - `description` can be left unlinked or linked to the same element


