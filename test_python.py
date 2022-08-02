import os
import subprocess
import datetime
data = os.environ.get('TEST')
fp = open('testfile.txt', 'a')
fp.write("\n=================================================================================\n")
fp.write("Task Date: "+ str(datetime.datetime.now()) + "\n")
fp.write("THIS IS TEST INPUT FROM SCRIPT value of Secret: " + data)
fp.close()
print("\n======================= Push changes to remote =======================")
print("Set git config...")
subprocess.Popen(["git", "config", "--global", "user.name", "Devang-Tomar"])
subprocess.Popen(["git", "config", "--global", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])

print("Push to remote...")
subprocess.Popen(["git", "add", "-A"])
subprocess.Popen(["git", "commit", "-m", "comment message"])
subprocess.Popen(["git", "push"])
print(data)
print("hello world")
