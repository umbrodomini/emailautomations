#import win32com.client as win32
from datetime import date

today = date.today()

d1 = today.strftime("%Y%m%d")
tasks = []


found_tasks = False
t_ype = []
with open('tasks.txt', 'r') as f:
    for line in f:
        if 'TASKS:' in line:
            found_tasks = True
            continue                    # This is the only change to your code.
                                        # When the header is found, immediately go to the next line
        if found_tasks:
            if 'TASKS:' in line:
               found_tasks = False
            else:
                t_line = str(line).rstrip('\n')
                tasks.append(t_line)



tasks = '\n'.join(tasks)

body = f'Hi Sir Ge, {tasks}'

print(body)
# outlook = win32.Dispatch('outlook.application')
# mail = outlook.CreateItem(0)
# mail.To = 'dennis.castaneda@infor.com'
# mail.Subject = 'Daily Report {} Den'.format(d1)
# mail.Body = f'Hi Sir Ge, \n\n\nDONE:\n\n{done} \n\n\nDOING:\n\n{doing}\n\n\nTO DO:\n\n\n {toodo}'
# #mail.HTMLBody = '<h2><b>Done:\n\nDoing:\n\nTO DO:\n\n </b></h2>' #this field is optional



# To attach a file to the email (optional):
# attachment  = "Path to the attachment"
# mail.Attachments.Add(attachment)

#mail.Send()