# MCP AutoFix Agent

## Overview

This project is an AI-powered AutoFix Agent built using MCP (Model Context Protocol), Python, and Git.

The system monitors application logs, detects errors, generates a fix using AI, and automatically creates a Git commit in a separate branch.

## Features

* Monitor application logs
* Detect runtime errors
* Read logs using MCP Server
* Generate code fixes using AI
* Save corrected code automatically
* Create Git branch and commit automatically

## Project Files

* `app.py` - Sample application with an error
* `monitor.py` - Monitors the application and logs errors
* `mcp_server.py` - MCP server for reading logs
* `fix_code.py` - Generates code fixes using AI
* `git_automation.py` - Creates branch and commit
* `fixed_app.py` - AI-generated fixed code

## Installation

```bash
pip install -r requirements.txt
```

## Run MCP Server

```bash
python mcp_server.py
```

## Run Project

```bash
python monitor.py
```

## Example

Error Detected:

```python
print(10 / 0)
```

AI Generated Fix:

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

## Technologies Used

* Python
* MCP
* OpenRouter API
* LangChain
* Git & GitHub

## Author

Kajal Shekhawat
