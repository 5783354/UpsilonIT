import uuid
import os


def upload_to_users(instance, filename):
    splitted = os.path.splitext(filename)
    if len(splitted) > 1:
        ext = splitted[1]
    else:
        ext = ''
    return os.path.join('users', str(instance.id), str(uuid.uuid4()) + ext)


def upload_to_blogs(instance, filename):
    splitted = os.path.splitext(filename)
    if len(splitted) > 1:
        ext = splitted[1]
    else:
        ext = ''
    return os.path.join('blogs', str(instance.id), str(uuid.uuid4()) + ext)


def upload_to_posts(instance, filename):
    splitted = os.path.splitext(filename)
    if len(splitted) > 1:
        ext = splitted[1]
    else:
        ext = ''
    return os.path.join('posts', str(instance.id), str(uuid.uuid4()) + ext)