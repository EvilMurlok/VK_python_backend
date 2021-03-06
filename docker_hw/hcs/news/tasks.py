from celery.schedules import crontab
from django.core.mail import send_mail
from django.conf import settings
from application.celery import app


@app.task(autoretry_for=(Exception, ), max_retries=3)
def send_mail_to_admin(subject, message):
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, settings.ADMIN_EMAILS)


@app.task(autoretry_for=(Exception,))
def moderate_news_titles():
    from news.models import News

    with open(settings.BANNED_WORDS_PATH, 'r') as file:
        words = file.read().strip()
        banned_words = set(words.split('\n'))

    for news in News.objects.all():
        for banned_word in banned_words:
            if banned_word in news.title:
                news.title = news.title.replace(banned_word, '*' * len(banned_word))
            if banned_word in news.content.lower():
                news.content = news.content.replace(banned_word, '*' * len(banned_word))
        news.save()


app.conf.beat_schedule.update(
    {
        'moderate-news-titles': {
            'task': 'news.tasks.moderate_news_titles',
            'schedule': crontab(minute='*', hour='*', day_of_month='*', month_of_year='*', day_of_week='*')
        }
    }
)