# Basic Linux Commands (for Robotics)

Here are some essential Linux commands I’m learning.  

## Navigation
- `pwd` → print working directory (where am I now?)
- `ls` → list files in current folder
- `cd foldername/` → change directory
- `cd ..` → go up one level

## File and Folder Management
- `mkdir myfolder` → make a new folder
- `touch myfile.txt` → create a new empty file
- `cp file1 file2` → copy file1 to file2
- `mv file1 file2` → move/rename file1 to file2
- `rm file.txt` → delete a file
- `rm -r foldername` → delete a folder (careful!)

## Viewing and Editing
- `cat file.txt` → show the file contents
- `less file.txt` → scroll through file contents
- `nano file.txt` → edit file with nano editor
- `vi file.txt` → edit file with vi editor

## Permissions
- `chmod +x script.sh` → make script executable
- `ls -l` → show file permissions

## Processes
- `ps` → show running processes
- `top` → real-time processes and CPU usage
- `kill <PID>` → stop a process

---

✍️ Notes:
- Linux is case-sensitive (`File.txt` ≠ `file.txt`).
- `rm -r` is dangerous — always double-check before deleting!
