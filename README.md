# Smart Content Assistant: AI-Driven Content Creation and Analysis

## Overview
Smart Content Assistant is an intelligent platform for generating, analyzing, and optimizing content. The platform features user authentication, SEO content analysis, and tailored suggestions for improving the quality and effectiveness of your content.

---

## Features
- **User Authentication and Profiles**:
  - Secure user registration and login.
  - Persistent user profiles with saved preferences.
  - Personalized dashboard for accessing previously generated content.
  
- **SEO-Enhanced Content Analysis**:
  - Analyze content for keyword density, readability, and overall SEO performance.
  - Actionable suggestions for improving keyword usage and readability.
  - Detailed reports to optimize content for search engines.

---

## Installation

### Prerequisites
Ensure the following are installed on your system:
- Python 3.9 or higher
- pip (Python package installer)
- SQLite (for local database storage)

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SmartContentAssistant.git
   cd SmartContentAssistant

2. Create a virtual environment and activate it
   ```bash
  python3 -m venv env
  source env/bin/activate  
  # On Windows, use 
  `env\Scripts\activate`

3. Install the dependencies
   ```bash
   pip install -r requirements.txt

4. setup the database
   
5. run the application
   ``bash
   python app/main.py
   
6. open your browser and navigate to:
   ```bash
   http://127.0.0.1:5000


## Usage

### User Authentication
- **Register**: Create an account by navigating to `/register` and filling out the form.
- **Login**: Log in using your username and password.
- **Dashboard**: View your profile and past activity.

### SEO Analysis
- Navigate to `/seo` to access the SEO analysis tool.
- **Input**:
  - **Content**: The text to analyze.
  - **Keyword**: The primary keyword for SEO optimization.
  - **Ideal Keyword Count**: Desired frequency of the keyword in the content.
- **Output Includes**:
  - Word count.
  - Keyword frequency and density.
  - Readability score.
  - Suggestions for SEO improvement.

---

## Example Outputs

### SEO Analysis Example
- **Input**:
  - **Content**: "AI is transforming the future of healthcare and technology."
  - **Target Keyword**: "AI"
  - **Ideal Keyword Count**: 3
- **Output**:
  - **Word Count**: 8
  - **Keyword Count**: 1
  - **Keyword Density**: 12.5%
  - **Readability Score**: 72.5
  - **Suggestions**:
    - "Consider using the keyword 'AI' at least 2 more times."
    - "Break down longer sentences to improve readability."

### User Dashboard
- Displays user-generated content and associated metadata for easy reference and editing.

---

## Testing

### SEO Analysis Testing
- Verify the system handles cases with:
  - Zero instances of the target keyword.
  - Excessive keyword repetition.
  - Both short and long content to ensure accurate word count and readability scoring.

### User Authentication Testing
- Check registration fails when usernames already exist.
- Validate login fails with incorrect credentials.
- Confirm successful logout clears session data.

