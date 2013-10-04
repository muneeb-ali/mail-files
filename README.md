Mass Email
==========

Send personalized emails to people with unique attachments.

## How to Use

With this package you can blast personalized attachments to people in list.csv. Currently, it only supports sending emails to people on the same domain e.g., @princeton.edu (easy to change this behavior though)


1. Set attachment file name as userid.txt (or pdf or anything else) e.g. muneeb.txt
 
2. Put your files in a folder 'files' inside the current directory. You can change the folder name in config.py

3. Edit the config.py and set your details (Note: we don't save the password but ask it at run time)

4. Make sure list.csv file has all names and user ids in the format (first_name, user_id)

5. Execute send_mail (better to send some test email to yourself, before sending the real message)

> ./send_mail.py 
