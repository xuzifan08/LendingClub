from crontab import CronTab
 
my_cron = CronTab(user='xuzifan')
job = my_cron.new(command='python3 automatic_ETL.py')
job.minute.every(1)
 
my_cron.write()
