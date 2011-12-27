from django.conf import settings
from retweeter import app_settings

def check_db_settings():
	engines = ['mysql', 'postgresql', 'oracle', 'sqlite3']

	engine_flag = 0
	for engine in engines:
		if settings.DATABASES['default']['ENGINE'] == 'django.db.backends.' + engine:
			engine_flag = 1

	if engine_flag == 0:
		return False

	if settings.DATABASES['default']['NAME'] == '':
		return False

	if settings.DATABASES['default']['USER'] == '':
		return False

	return True


def check_app_settings():
	if app_settings.TWITTER_ACCOUNT == '':
		return False

	if app_settings.TWITTER_CONSUMER_KEY == '':
		return False

	if app_settings.TWITTER_CONSUMER_SECRET == '':
		return False

	return True

