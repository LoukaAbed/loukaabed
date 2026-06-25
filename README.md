---
title: Portfolio App Pipeline
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.51.0
app_file: testapp.py
pinned: false
---

# Live Custom Domain Data Science Portfolio Hub
Automated testing deployment infrastructure streaming from GitHub straight to Hugging Face Spaces.

## SAS ODA Integration Setup

This application uses the `saspy` Python bridge package to securely execute native SAS code blocks directly inside the Streamlit portfolio hub.

### Infrastructure Requirements

To ensure the backend SAS connectivity functions properly on Hugging Face, verify that the following files are at the root of your project:

1. **`packages.txt`** (Installs the required Java runtime)
   ```text
   default-jre
   ```

2. **`requirements.txt`**
   ```text
   streamlit>=1.51.0
   saspy
   pandas
   ```

### Space Credentials Configuration
Do not hardcode your SAS credentials. Navigate to your **Hugging Face Space Settings** -> **Variables and secrets**, and add your encrypted platform secrets:
* `SAS_USER`: Your SAS ODemand login email address.
* `SAS_PASSWORD`: Your SAS account password.
