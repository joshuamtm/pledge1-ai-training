import re

# Read the file
with open('index.html', 'r') as f:
    content = f.read()

# Find all slide definitions
slide_pattern = r'<!-- Slide (\d+):(.*?)-->'
slide_matches = list(re.finditer(slide_pattern, content))

print(f"Found {len(slide_matches)} slide comments")

# Create a mapping of old numbers to new sequential numbers
slide_mapping = {}
for i, match in enumerate(slide_matches, start=1):
    old_num = int(match.group(1))
    if old_num not in slide_mapping or i < slide_mapping[old_num]:
        slide_mapping[old_num] = i
    print(f"Slide {old_num} '{match.group(2).strip()}' -> Slide {i}")

# Now we need to renumber everything sequentially
# First, temporarily rename to avoid conflicts
temp_content = content
for match in reversed(slide_matches):
    old_num = match.group(1)
    temp_num = f"TEMP_{old_num}_{match.start()}"
    # Replace both in comments and IDs
    temp_content = temp_content[:match.start()] + f"<!-- Slide {temp_num}:{match.group(2)}-->" + temp_content[match.end():]

# Also temporarily rename the slide IDs
temp_content = re.sub(r'id="slide-(\d+)"', lambda m: f'id="slide-TEMP_{m.group(1)}"', temp_content)

# Now assign proper sequential numbers
slide_pattern_temp = r'<!-- Slide (TEMP_\d+_\d+):(.*?)-->'
slide_matches_temp = list(re.finditer(slide_pattern_temp, content))

final_content = temp_content
for i, match in enumerate(re.finditer(slide_pattern_temp, temp_content), start=1):
    temp_id = match.group(1)
    title = match.group(2)
    
    # Replace in comment
    final_content = re.sub(f"<!-- Slide {re.escape(temp_id)}:{re.escape(title)}-->", 
                           f"<!-- Slide {i}:{title}-->", 
                           final_content)
    
    # Replace in ID - need to extract the original number
    orig_num = temp_id.split('_')[1]
    final_content = re.sub(f'id="slide-TEMP_{orig_num}"', f'id="slide-{i}"', final_content, count=1)

# Update total slides
total_slides = len(slide_matches)
final_content = re.sub(r'const totalSlides = \d+;', f'const totalSlides = {total_slides};', final_content)
final_content = re.sub(r'(\d+) / \d+', f'1 / {total_slides}', final_content)

# Write the result
with open('index.html', 'w') as f:
    f.write(final_content)

print(f"\nFixed! Total slides: {total_slides}")