import subprocess

from fix_code import fix_code
from git_automation import create_fix_branch
try:

    subprocess.run(
        ["python", "app.py"],
        check=True
    )

except Exception as e:

    with open(
        "logs/app.log",
        "a"
    ) as file:

        file.write(str(e) + "\n")

    with open(
        "logs/app.log",
        "r"
    ) as file:

        logs = file.read()

    with open(
        "app.py",
        "r"
    ) as file:

        code = file.read()

    fixed_code = fix_code(
        logs,
        code
    )

    with open(
        "fixed_app.py",
        "w"
    ) as file:

        file.write(fixed_code)

    print("Fixed code generated")
    create_fix_branch()

print("Monitoring Completed")