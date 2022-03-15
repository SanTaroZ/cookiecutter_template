import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Installing libraries...")
#print(f"Initializing a git repository...{RESET_ALL}")

#subprocess.call(['git', 'init'])
#subprocess.call(['git', 'add', '*'])
#subprocess.call(['git', 'commit', '-m', 'Initial commit'])

#print(f"{MESSAGE_COLOR} git init, git add * & git commit -m Initial has been executed{RESET_ALL}")
#subprocess.call(['dir'])
#subprocess.call(['pip', 'install','-r','requirements.txt'])

paths = []
for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
        paths.append(dirpath)

print(os.getcwd())   
os.chdir(paths[0])
print(os.getcwd())
subprocess.call(['pip', 'install','-r','requirements.txt'])

print(f"{MESSAGE_COLOR}Done!!")