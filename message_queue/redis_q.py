import redis
import uuid


class RedisQ:
    enterprise_key = ""

    def __init__(self, identifier=None):
        self._identifier = identifier or uuid.uuid4().hex

        self.redis_client = redis.Redis()
        self.source_tag_mapping = {}
        self.target_topic_list = []

    def is_running():
        pass

    def stop_running():
        pass

    def create_resource():
        pass

    def reset_resources(target_topic_counter):
        pass

    def consume_resource():
        pass

    def get_next_resource_and_topic():
        pass

    def produce_message(source_key, target_topic, message):
        pass

    def consume_message(target_topic, resource):
        pass

    def produce_error_message(message):
        pass

    def produce_archive_message(message):
        pass

    def produce_dead_letter_message(message):
        pass

    def consume_enterprise_message_bulk():
        pass

    @staticmethod
    def topic_key(topic):
        pass

    @staticmethod
    def resource_key(topic):
        pass

    @staticmethod
    def active_key(resourcce):
        pass

    @staticmethod
    def kill_key(resource):
        pass
