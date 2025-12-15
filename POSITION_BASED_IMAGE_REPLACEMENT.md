# Position-Based Image Replacement

## How It Works

Instead of using named placeholders, the code now identifies image placeholders by their **position** in the template and replaces them automatically.

## Image Placement

The code identifies images based on their position in a 1920x1080 design:

1. **Top Right** → Logo
   - Right 40% of design, top third (y ≤ 360px)

2. **Middle Right** → Map (optional)
   - Right 40% of design, middle third (360px < y ≤ 720px)

3. **Bottom Right** → Headshot
   - Right 40% of design, bottom third (y > 720px)

## What You Need to Do

### In Your Canva Template:

1. **Create image placeholders** (any placeholder images) in these positions:
   - **Top right corner** → Place a placeholder image here (will be replaced with logo)
   - **Middle right area** → Place a placeholder image here (will be replaced with map, optional)
   - **Bottom right corner** → Place a placeholder image here (will be replaced with headshot)

2. **You don't need to name them** - Just position them correctly!

3. **For text fields**, you still need to use Data Autofill with these field names:
   - `company_name`
   - `description`
   - `location`
   - `investment_date`
   - `investment_round`
   - `quarter`
   - `year`
   - `founders`
   - `co_investors`
   - `background`

## How the Code Works

1. **Uploads images** to Canva (headshot, logo, map)
2. **Gets all image elements** from the design
3. **Identifies their positions** (x, y coordinates)
4. **Replaces images by position**:
   - Top right image → Logo
   - Middle right image → Map (if provided)
   - Bottom right image → Headshot

## Fallback Behavior

- **If Autofill works**: Uses Autofill for both text and images (if you have named placeholders)
- **If Autofill fails**: Falls back to position-based replacement for images
- **Text always uses Autofill**: Text fields still need Data Autofill setup

## Template Setup Summary

✅ **Images**: Just place placeholder images in the right positions (no naming needed!)
✅ **Text**: Use Data Autofill with the field names listed above

## Position Zones (for reference)

For a 1920x1080 design:
- **Right zone**: x ≥ 1152px (right 40%)
- **Top zone**: y ≤ 360px (top third)
- **Middle zone**: 360px < y ≤ 720px (middle third)
- **Bottom zone**: y > 720px (bottom third)

## Troubleshooting

**Images not replacing?**
- Make sure placeholder images are in the right positions
- Check that images are in the right 40% of the design
- Verify image elements are actual image elements (not grouped or masked)

**Text not updating?**
- Text still requires Data Autofill setup with correct field names
- Position-based replacement only works for images


