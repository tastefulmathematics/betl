import multiprocessing
import time

mapping = {

}

def process_message(message_key, message_body):
    method = mapping.get(message_key)
    if not method:
        return

    method(message_body)

def process_primary_queue():
    process_list = []
    for is_primary, message_key, message_body in primary_work_queue():
        if is_primary:
            kwargs = {
              "args": (mesasge_key, message_body),
              "target": process_message,
            }
        else:
            kwargs = {
              "args": 600,
              "target": process_secondary_queue,
            }
            process_list.append(multiprocessing.Process(**kwargs))


def process_secondary_queue(duration):
    start_time = time.time()
    while True:
        current_time = time.time()
        if duration and current_time - start_Time:
            return

        message_key, message_body = next(secondary_work_queue())
        process_message(message_key, message_body)
