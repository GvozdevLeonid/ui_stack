# ui_stack

ui_stack is a python frontend build pipeline.
Tailwind CSS, DaisyUI, AlpineJS integration for python ( Django, FastAPI, Flask, ... )

## GOAL
This project provides a convenient way to integrate the Tailwind CSS/DaisyUI/AlpineJS framework into Python projects. It creates a folder (named theme by default) that includes all the necessary files and configurations to get started quickly.

## Requirements
* Python 3.11 or newer.
* Node.js

## Getting Started
1. Install ui_stack:
```
pip install git+https://github.com/GvozdevLeonid/ui_stack.git
```
2. Set the environment variable to the project's base folder:
```
LINUX/MACOS:
export UI_STACK_PROJECT_ROOT=base project folder path
WINDOWS:
set UI_STACK_PROJECT_ROOT=base project folder path
```
3. Create ui_stack folder:
```
ui_stack -f theme init
```
4. Install dependencies:
```
ui_stack -f theme install
```
5. Start monitoring files for development
```
ui_stack -f theme start
```
6. Build production files
```
ui_stack -f theme build
```
7. Add CSS and JS files to your template
```
<link href="/static/css/styles.css" rel="stylesheet" type="text/css" />
<script "/static/js/script.js"></script>
```
