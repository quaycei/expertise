from django.contrib.auth.models import User

from django_slack_oauth.models import SlackUser


def register_user(request, api_data):
    user = User.objects.create_user(
        username=api_data['user_id']
    )

    slacker, _ = SlackUser.objects.get_or_create(slacker=user)
    slacker.access_token = api_data.pop('access_token')
    slacker.extras = api_data
    slacker.save()

    request.created_user = user

    return request, api_data


def notify(request, api_data):
    notify_admins("New user with id {} has been created.".format(request.created_user))
    notify_user(request.created_user)

    return request, api_data
