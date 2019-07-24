from crontab import CronTab
 
my_cron = CronTab(user='xuzifan')
job = my_cron.new(command='python3 data_cleaning.py')
job.minute.every(1)


 
my_cron.write()
