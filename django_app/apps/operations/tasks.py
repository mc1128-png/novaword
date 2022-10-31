from celery.schedules import crontab
from celery.task import periodic_task, task
from celery.utils.log import get_task_logger

from utils.user_plan import UserPlan
from utils.email_send import send_feedback_email

logger = get_task_logger(__name__)


@periodic_task(run_every=(crontab(minute='0', hour='*/2')), name="deploy_today_group_plans", ignore_result=True)
def deploy_today_group_plans():
    logger.info("Deploying today's learning plans")
    user_plan = UserPlan()
    user_plan.deploy_all_group_plans()


@periodic_task(run_every=(crontab(minute='0', hour='*/4')), name="populate_today_tasks", ignore_result=True)
def populate_today_tasks():
    logger.info("Populating today's tasks")
    user_plan = UserPlan()
    user_plan.populate_today_tasks()


@task(name="send_user_feedback")
def send_user_feedback(email, title, message):
    send_feedback_email(email, title, message)
