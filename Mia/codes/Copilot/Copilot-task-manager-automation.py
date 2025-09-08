## Phase 3: Task Manager Automation (Windows Example)
# 1 To automate this on device startup:

# 2 Save the script as copilot_memory.py

Create a .bat file to run it:
@echo off
pythonw.exe "C:\path\to\copilot_memory.py"

# 3 Add the .bat file to Task Scheduler: Trigger: At logon Action: Start a program Conditions: Uncheck “Start only if connected to power”
