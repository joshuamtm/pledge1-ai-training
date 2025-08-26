import re

# Read the file
with open('index.html', 'r') as f:
    content = f.read()

# Define the sample prompts for each COMPAS section
compas_samples = [
    {
        'after_slide': 7,  # After Context Part 2
        'title': 'Context: Sample Discovery Prompt',
        'content': '''        <div class="prompt-example">
            <p><strong>Use this prompt to uncover your organization's AI landscape:</strong></p>
            <p style="font-style: italic; margin-top: 10px; font-size: 0.85em;">
            "I'm the [your role] at [organization type]. Help me conduct an AI readiness assessment. Our team of [size] currently struggles with [top 3 pain points]. We have [tech stack/tools], and our data privacy requirements include [compliance needs]. What questions should I ask my team to understand: 1) Current unofficial AI use, 2) Biggest time-wasters that AI could address, 3) Security/compliance gaps we need to fill? Please provide a 5-minute team survey template and a simple scoring rubric to assess our AI readiness level."
            </p>
        </div>
        <div class="demo-box">
            <div class="demo-title">Why This Works</div>
            <p>• Provides organizational context upfront</p>
            <p>• Asks for specific deliverables (survey + rubric)</p>
            <p>• Focuses on discovery, not solutions</p>
        </div>'''
    },
    {
        'after_slide': 9,  # After Objective
        'title': 'Objective: Sample Problem Definition Prompt',
        'content': '''        <div class="prompt-example">
            <p><strong>Use this prompt to clarify your true objective:</strong></p>
            <p style="font-style: italic; margin-top: 10px; font-size: 0.85em;">
            "I run a [organization type] and we're drowning in [specific task]. Currently, this takes [hours] per [frequency] and involves [current process]. But I suspect the real problem might be deeper. Can you help me use the '5 Whys' technique to identify the root cause? Then suggest 3 possible objectives: 1) A quick fix (this week), 2) A systemic improvement (this quarter), 3) A transformational change (this year). For each, estimate time savings and implementation effort on a scale of 1-5."
            </p>
        </div>
        <div class="demo-box">
            <div class="demo-title">Why This Works</div>
            <p>• Distinguishes symptoms from root causes</p>
            <p>• Offers multiple solution levels</p>
            <p>• Includes measurable criteria</p>
        </div>'''
    },
    {
        'after_slide': 11,  # After Method in Action
        'title': 'Method: Sample Implementation Prompt',
        'content': '''        <div class="prompt-example">
            <p><strong>Use this prompt to design your AI implementation method:</strong></p>
            <p style="font-style: italic; margin-top: 10px; font-size: 0.85em;">
            "Our [department] needs to implement AI for [specific workflow]. We have [budget] and [timeline]. Our team includes [roles and skill levels]. Design a phased rollout plan that includes: Phase 1 - Pilot with [early adopters], Phase 2 - Expand to [broader group], Phase 3 - Full implementation. For each phase, specify: required tools, training needed, success metrics, potential risks, and rollback plan. Format as a simple Gantt chart I can share with leadership."
            </p>
        </div>
        <div class="demo-box">
            <div class="demo-title">Why This Works</div>
            <p>• Acknowledges constraints (budget, timeline, skills)</p>
            <p>• Requests phased approach with clear milestones</p>
            <p>• Includes risk mitigation</p>
        </div>'''
    },
    {
        'after_slide': 21,  # After Performance & Assessment slide
        'title': 'Performance & Assessment: Sample Tracking Prompts',
        'content': '''        <div class="prompt-example">
            <p><strong>Use this prompt to track and optimize performance:</strong></p>
            <p style="font-style: italic; margin-top: 10px; font-size: 0.85em;">
            "I've implemented [AI tool/workflow] for [specific task] over the past [timeframe]. Initial metrics show [current results]. Help me create a performance dashboard that tracks: 1) Time saved (hours/week), 2) Quality metrics (error rates, satisfaction scores), 3) Adoption rate (% of team using it), 4) ROI (cost savings vs. tool cost). Then analyze my data to identify: What's working well? What needs adjustment? What unexpected benefits or challenges emerged? Provide specific recommendations to improve performance by 25% next month."
            </p>
        </div>
        <div class="demo-box">
            <div class="demo-title">Why This Works</div>
            <p>• Focuses on measurable outcomes</p>
            <p>• Requests both analysis and action items</p>
            <p>• Sets specific improvement target</p>
        </div>'''
    },
    {
        'after_slide': 22,  # After Super You slide 
        'title': 'Super You: Sample Transformation Prompt',
        'content': '''        <div class="prompt-example">
            <p><strong>Use this prompt to envision your transformed organization:</strong></p>
            <p style="font-style: italic; margin-top: 10px; font-size: 0.85em;">
            "Our organization has successfully implemented AI across [departments/workflows]. We've freed up [hours] per week and improved [key metrics]. Now help me envision 'Super Us': 1) What strategic initiatives can we tackle with our freed capacity? 2) How can we use AI to better serve [our beneficiaries]? 3) What new partnerships or funding opportunities does this unlock? 4) What's our story for funders about our AI transformation? 5) Create a one-page 'AI Success Story' template highlighting our journey, impact metrics, and vision for scaling. Make it compelling for grant applications."
            </p>
        </div>
        <div class="demo-box">
            <div class="demo-title">Why This Works</div>
            <p>• Shifts focus from efficiency to impact</p>
            <p>• Connects AI to mission advancement</p>
            <p>• Provides fundraising narrative</p>
        </div>'''
    }
]

# Function to insert a new slide after a given slide number
def insert_slide_after(content, after_slide_num, new_slide_num, slide_html):
    # Find the end of the specified slide
    pattern = rf'(<!-- Slide {after_slide_num}:.*?</div>\n    </div>)'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        end_pos = match.end()
        # Create the new slide with proper numbering
        new_slide = f'\n\n    <!-- Slide {new_slide_num}: {slide_html.split("<h1>")[1].split("</h1>")[0]} -->\n    <div class="slide" id="slide-{new_slide_num}">\n        <div class="logo-pledge">\n            <div class="pledge-icon">1%</div>\n            <span>Pledge 1%</span>\n        </div>\n        <div class="logo-mtm">\n            MEET the M<span class="moment">O</span>MENT\n            <div class="tagline">RESILIENCE FOR NONPROFITS</div>\n        </div>\n        <h1>{slide_html.split("<h1>")[1].split("</h1>")[0]}</h1>\n{slide_html.split("</h1>")[1]}\n    </div>'
        
        # Insert the new slide
        content = content[:end_pos] + new_slide + content[end_pos:]
    
    return content

# First, let's find out how many slides we currently have
total_slides_match = re.search(r'const totalSlides = (\d+);', content)
if total_slides_match:
    current_total = int(total_slides_match.group(1))
else:
    current_total = 27  # fallback based on previous work

# Sort samples by their position (reverse order to avoid numbering conflicts)
compas_samples.sort(key=lambda x: x['after_slide'], reverse=True)

# Track how many slides we're adding
slides_added = 0

# Insert each sample slide
for sample in compas_samples:
    after_slide = sample['after_slide'] + slides_added  # Adjust for previously added slides
    new_slide_num = after_slide + 1
    
    # Build the slide HTML
    slide_html = f"<h1>{sample['title']}</h1>\n{sample['content']}"
    
    # Insert the slide
    content = insert_slide_after(content, after_slide, new_slide_num, slide_html)
    
    # Update all subsequent slide numbers
    for i in range(current_total + slides_added, new_slide_num, -1):
        # Update slide IDs
        content = re.sub(f'id="slide-{i}"', f'id="slide-{i+1}"', content)
        # Update slide comments
        content = re.sub(f'<!-- Slide {i}:', f'<!-- Slide {i+1}:', content)
    
    slides_added += 1
    current_total += 1

# Update the total slides count
content = re.sub(r'const totalSlides = \d+;', f'const totalSlides = {current_total};', content)
content = re.sub(r'1 / \d+', f'1 / {current_total}', content)

# Write the modified content back
with open('index.html', 'w') as f:
    f.write(content)

print(f"Successfully added {len(compas_samples)} sample prompt slides!")
print(f"Total slides now: {current_total}")