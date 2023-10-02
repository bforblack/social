import schedule
import time
import threading
import json
from datetime import datetime
from database.mongo_connector import Mongo
from logs.studio_logger import Logger
from post_scheduler.time_compare import is_valid_time_format
from postmanagementservice.post_service import PostManagementService


class TaskScheduler:
    def __init__(self):
        self.logger = Logger("oculus_service")
        self.mongo_connector = Mongo()
        self.schedule_thread = threading.Thread(target=self.run_scheduler)
        self.midnight_thread = threading.Thread(target=self.midnight_scheduler)
        self.schedule_thread.start()
        self.midnight_thread.start()

    def task_scheduler(self, job_data, scheduled_time, function, parent_id=None, mongo_job_id='Paused task started'):
        mongo_job_id = job_data["_id"]
        try:

            # print('job_data', job_data)
            # scheduled_time = job_data['scheduleTime']

            is_valid, datetime_obj, current_datetime = is_valid_time_format(scheduled_time)
            execution_time = datetime_obj.time()

            if is_valid and datetime_obj.date() == current_datetime.date() and datetime_obj.time() >= execution_time:
                # print('scheduler',function,job_data, True,parent_id)
                schedule.every().day.at(str(execution_time)).do(
                    lambda: function(job_data, scheduled=True, parent_id=parent_id)).tag(
                    mongo_job_id)

                self.logger.info(f'Task has been scheduled at {scheduled_time} with the Jobid: {mongo_job_id}')
                return mongo_job_id

        except Exception as Ex:
            self.mongo_connector.update('scheduler', mongo_job_id, 'Failed')
            self.logger.error(f'Error: {Ex}')

    def fetch_and_schedule_tasks(self, function):
        try:
            # Find all tasks in the collection
            all_tasks = self.mongo_connector.find_all('scheduler')

            # Schedule each task based on its 'schedule_time'
            for task in all_tasks:
                if task is not None:
                    # print('task', task)
                    object_data = json.loads(task['Object'])
                    schedule_time = object_data['schedule_time']
                    self.task_scheduler(task, schedule_time, function)

        except Exception as Ex:
            self.logger.error(f'Error: {Ex}')

    def store_job(self, request, scheduleTime):
        try:
            # updating request time in request
            request["request_time"] = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

            return self.compare_datetime_with_current(scheduleTime, request)

        except Exception as Ex:
            self.logger.error(f'Error: {Ex}')

    def load_jobs(self, mongo_job_id, scheduleTime, function, parent_id=None):
        try:
            job_data = self.mongo_connector.find_data(collectionName='scheduler', document=mongo_job_id)
            if job_data is not None:
                self.task_scheduler(job_data, scheduleTime, function, mongo_job_id=mongo_job_id, parent_id=parent_id)

        except Exception as ex:
            self.logger.error(f'Error : {ex}')

    def run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

    def compare_datetime_with_current(self, target_datetime_str, request):
        try:
            is_valid, datetime_obj, current_datetime = is_valid_time_format(target_datetime_str)

            if is_valid and datetime_obj.date() == current_datetime.date():
                if datetime_obj.time() >= current_datetime.time():
                    request['status'] = 'pending'
                    mongo_job_id = self.mongo_connector.save_data(collectionName='scheduler', document=request)
                    self.logger.info(
                        f'Task has been scheduled with id {mongo_job_id} in social database at scheduler table')
                    return mongo_job_id

                else:
                    print('Today time passed, select next time.')
                    return 'Today time passed, select next time.'

            elif datetime_obj.date() < current_datetime.date():
                print("Please don't add passed date.")
                return "Please don't add passed date."
            else:
                request['status'] = 'pending'
                mongo_job_id = self.mongo_connector.save_data(collectionName='scheduler', document=request)
                self.logger.info(
                    f'Task has been scheduled with id {mongo_job_id} in social database at scheduler table')
                return "Update the task in the database."

        except:
            return 'please provide valid time'

    def midnight_scheduler(self):
        while True:
            now = datetime.now()
            target_time = now.strftime('%H:%M:%S')
            #
            if target_time == "00:00:00":
                # Execute the function here
                #
                schedule.clear()
                task_scheduler = TaskScheduler()
                thread2 = threading.Thread(target=task_scheduler.fetch_and_schedule_tasks,
                                           args=(PostManagementService().create_post,))
                # Start the thread
                thread2.start()
