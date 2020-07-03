# website-blocker
This is a simple python code to block the unwanted websites from your browser. You can customise the website list to be blocked by changing "website_list" python list in the code.
Following are instructions to execute code:
1. You must change the host path according to your pc.
   For windows users host path is C:\Windows\System32\drivers\etc\hosts
   For mac/linux users its etc\hosts
2. You also need to replace host file of your os to given host file.
3. You need to set a scheduler at startup-
   For windows:
   1. Now open task scheduler.
   2. Click on “create task”. Fill the name of your choice and flag “Run with highest privilege”.
   3. Now go to triggers, select “At startup” for begin the task.
   4. Go to Action bar and create a new action and give path of your script.
   5. Go to conditions bar and unflag the power section.
   6. Press ok and you can see the script scheduled. Restart your pc and try to load blocked websites - they won't load.
   For Mac:
   1. Write following command in terminal:
      sudo crontab -e
   2. Now press “i” to go into insert/editing mode and write @reboot python_script_path .
   3. Save the tab by pressing first esc to quit write mode and fall back to command mode and now write “:wq” and finally press enter to validate.
   4. Restart your system and see the magic.
