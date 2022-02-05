import os
import subprocess
data = os.environ.get('TEST')
fp = open('testfile.txt', 'w')
fp.write("THIS IS TEST INPUT FROM SCRIPT")
fp.close()
print("\n======================= Push changes to remote =======================")
print("Set git config...")
subprocess.Popen(["git", "config", "--global", "user.name", "github-actions[bot]"])
subprocess.Popen(["git", "config", "--global", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])

print("Push to remote...")
subprocess.Popen(["git", "add", "-A"])
subprocess.Popen(["git", "commit", "-m", "comment message"])
subprocess.Popen(["git", "push"])
print(data)
print("hello world")
