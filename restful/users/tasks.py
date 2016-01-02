from djcelery import celery
import logging
logger = logging.getLogger(__name__)

@celery.task
def add(x,y):
	logger.debug("Adding the addition of %s,%s to the que")
	return x + y

@celery.task
def sleeptask(i):
	from time import sleep
	sleep(i)
	return i