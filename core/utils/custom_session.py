from django.core.cache import cache
import uuid


def cache_user_session_key(user_id: str):
    cache_obj = cache.get('user_session', {})
    session_id = str(uuid.uuid4().hex)
    cache_obj[user_id] = session_id
    cache.set('user_session', cache_obj, 86400)
    return session_id


def get_or_create_user_session_key(user_id: str):
    cache_obj = cache.get('user_session', {})
    cache_obj = cache_obj.get(str(user_id), None)
    cache_obj = cache_user_session_key(user_id) if not cache_obj else cache_obj
    return cache_obj


def get_user_session_key(user_id: str):
    cache_obj = cache.get('user_session', {})
    cache_obj = cache_obj.get(str(user_id), None)
    return cache_obj


def delete_user_session(user_id: str):
    cache_obj = cache.get('user_session', {})
    cache_obj.pop(str(user_id), None)
    cache.set('user_session', cache_obj, 86400)
    return cache_obj