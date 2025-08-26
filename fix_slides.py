import re

# Read the file
with open('index.html', 'r') as f:
    content = f.read()

# 1. Fix the Vibe Coding slide (already done in previous edit)
# This is already corrected

# 2. Update the Building Packages slide to add Gemini Gems
old_packages = '''    <!-- Slide 14: Building Packages -->
    <div class="slide" id="slide-14">
        <div class="logo-pledge">
            <div class="pledge-icon">1%</div>
            <span>Pledge 1%</span>
        </div>
        <div class="logo-mtm">
            MEET the M<span class="moment">O</span>MENT
            <div class="tagline">RESILIENCE FOR NONPROFITS</div>
        </div>
        <h1>From Prompt to Package</h1>
        <p>A Package = Your PTCF prompt + instructions + files, saved for repeated use</p>
        <h3>Platform-Specific Setup</h3>
        <div class="demo-box">
            <div class="demo-title">ChatGPT → Custom GPT</div>
            <p>• Go to "Explore GPTs" → "Create"</p>
            <p>• Name: "Grant Report Generator"</p>
            <p>• Instructions: [Your PTCF prompt]</p>
        </div>
        <div class="demo-box">
            <div class="demo-title">Claude → Project</div>
            <p>• Create new Project</p>
            <p>• Add templates to Project knowledge</p>
            <p>• Custom instructions: Your PTCF prompt</p>
        </div>
    </div>'''

new_packages = '''    <!-- Slide 14: Building Packages -->
    <div class="slide" id="slide-14">
        <div class="logo-pledge">
            <div class="pledge-icon">1%</div>
            <span>Pledge 1%</span>
        </div>
        <div class="logo-mtm">
            MEET the M<span class="moment">O</span>MENT
            <div class="tagline">RESILIENCE FOR NONPROFITS</div>
        </div>
        <h1>From Prompt to Package</h1>
        <p>A Package = Your PTCF prompt + instructions + files, saved for repeated use</p>
        <h3>Platform-Specific Setup</h3>
        <div class="demo-box">
            <div class="demo-title">ChatGPT → Custom GPT</div>
            <p>• Go to "Explore GPTs" → "Create"</p>
            <p>• Name: "Grant Report Generator"</p>
            <p>• Instructions: [Your PTCF prompt]</p>
        </div>
        <div class="demo-box">
            <div class="demo-title">Claude → Project</div>
            <p>• Create new Project</p>
            <p>• Add templates to Project knowledge</p>
            <p>• Custom instructions: Your PTCF prompt</p>
        </div>
        <div class="demo-box">
            <div class="demo-title">Gemini → Gems</div>
            <p>• Click "Create a Gem"</p>
            <p>• Name your Gem</p>
            <p>• Add instructions and context</p>
            <p>• Test and refine, then share with team</p>
        </div>
    </div>'''

content = content.replace(old_packages, new_packages)

# 3. Add a new slide after Grant Review with sample PTCF prompt
# Find the Grant Review slide and add a new one after it
grant_review_pattern = r'(    <!-- Slide 15: Use Case - Grant Review -->.*?</div>\n    </div>)'
grant_review_match = re.search(grant_review_pattern, content, re.DOTALL)

if grant_review_match:
    end_pos = grant_review_match.end()
    
    new_slide = '''

    <!-- Slide 16: Grant Review PTCF Example -->
    <div class="slide" id="slide-16">
        <div class="logo-pledge">
            <div class="pledge-icon">1%</div>
            <span>Pledge 1%</span>
        </div>
        <div class="logo-mtm">
            MEET the M<span class="moment">O</span>MENT
            <div class="tagline">RESILIENCE FOR NONPROFITS</div>
        </div>
        <h1>Grant Review GPT: Sample PTCF Prompt</h1>
        <div class="prompt-example">
            <p><strong>Instructions for your Grant Review GPT:</strong></p>
            <p style="font-style: italic; margin-top: 10px; font-size: 0.85em;">
            "You are a grant program manager with 20 years of experience evaluating nonprofit performance <strong>(P)</strong>. Your task is to compare grant proposals with final reports to assess whether objectives were met <strong>(T)</strong>. You work for a foundation focused on youth development and education equity. You understand that nonprofits face challenges and value honest communication about obstacles <strong>(C)</strong>. Provide your assessment in three sections: 1) Executive Summary (Met/Exceeded/Fell Short), 2) Key Achievements with specific metrics, 3) Recommendations for future funding. Use clear, constructive language that celebrates successes while identifying areas for growth <strong>(F)</strong>."
            </p>
        </div>
        <div class="demo-box">
            <div class="demo-title">Share with Your Grants Team</div>
            <p>• Save as Custom GPT, Project, or Gem</p>
            <p>• Set sharing permissions for team access</p>
            <p>• Train team on uploading documents</p>
            <p>• Review first few outputs together</p>
        </div>
    </div>'''
    
    content = content[:end_pos] + new_slide + content[end_pos:]
    
    # Now we need to renumber all subsequent slides
    # Update slide 16 (Vibe Coding) to 17, etc.
    for i in range(26, 15, -1):  # Go backwards to avoid conflicts
        old_slide = f'slide-{i}'
        new_slide_num = f'slide-{i+1}'
        old_comment = f'Slide {i}:'
        new_comment = f'Slide {i+1}:'
        
        content = content.replace(f'id="{old_slide}"', f'id="{new_slide_num}"')
        content = content.replace(f'<!-- {old_comment}', f'<!-- {new_comment}')
    
    # Update total slides from 26 to 27
    content = content.replace('const totalSlides = 26;', 'const totalSlides = 27;')
    content = content.replace('1 / 26', '1 / 27')

# Write the modified content back
with open('index.html', 'w') as f:
    f.write(content)

print("Slides updated successfully!")