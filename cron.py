from crontab import CronTab

cron = CronTab(user='pi')  
job = cron.new(command='python3 monitorAndNotify.py')  
job.minute.every(3)

cron.write()  