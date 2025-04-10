# NVIDIA AI Workbench Tutorial
An interactive web application that guides you through the features of NVIDIA AI Workbench. 
It's self-paced with hands-on exercises and step-by-step guidance for both basic and advanced workflows.

*Navigating the README*: [Prerequisites](#prerequisites) | [Description](#description) | [Features](#features) | [Tutorial Structure](#tutorial-structure) | [Get Started](#get-started) | [Development](#development) | [License](#license)

*Other Resources*: [:arrow_down: Download AI Workbench](https://www.nvidia.com/en-us/deep-learning-ai/solutions/data-science/workbench/) | [:books: User Guide](https://docs.nvidia.com/ai-workbench/user-guide/latest/overview/introduction.html) |[:open_file_folder: Other Projects](https://docs.nvidia.com/ai-workbench/user-guide/latest/quickstart/example-projects.html) | [:rotating_light: User Forum](https://forums.developer.nvidia.com/t/support-workbench-example-project-onboarding-project/329786)

## Prerequisites
 - NVIDIA AI Workbench installed on your system
 - 15 to 30 minutes of time

## Description
This tutorial application is built using Streamlit and provides an interactive learning experience for NVIDIA AI Workbench. It covers everything from basic project setup to advanced features like environment customization and container management. The tutorial is designed to be self-paced and includes validation checks to ensure proper understanding of each concept.

## Features
- Interactive step-by-step tutorials
- Real-time validation of completed tasks
- Progress tracking across sessions
- Multi-language support
- Comprehensive coverage from basics to advanced topics

## Tutorial Structure
The tutorial is organized into progressive sections:

### Basic Tutorials
1. Getting Started with AI Workbench
   - Creating your first project
   - Using JupyterLab
   - Basic Git operations
   
2. Environment Customization
   - Adding packages
   - Rebuilding environments
   - Testing new dependencies

3. Project Structure and Management
   - Understanding project components
   - Data persistence
   - Environment configuration

### Advanced Tutorials
1. Advanced Environment Configuration
2. Custom Container Usage
3. Advanced RAG Applications

## Get Started

1. Clone this project into the AI Workbench desktop app
2. From the project view, click the green **Open Tutorial** button in the top right
3. The browser will open the tutorial, follow along:
   - Start with the basic exercises
   - Complete each task in sequence
   - Verify your progress with built-in validation
   - Move to advanced topics when ready

## Development
This tutorial app uses a template-based system for content management:
- Python files (`*.py`) handle logic and interaction
- YAML files (`*.en_US.yaml`) contain tutorial content
- Test files ensure proper task completion

### Adding New Tutorials
1. Copy the template files:
   - `template.py` → `your_tutorial.py`
   - `template.en_US.yaml` → `your_tutorial.en_US.yaml`
2. Update the content in the YAML file
3. Implement necessary test functions
4. Update navigation links

## License
This project is licensed under the Apache License, Version 2.0. See the LICENSE file for details.

This project may utilize additional third-party open source software projects. Review the license terms of these open source projects before use. Third party components used as part of this project are subject to their separate legal notices or terms that accompany the components. You are responsible for confirming compliance with third-party component license terms and requirements.
