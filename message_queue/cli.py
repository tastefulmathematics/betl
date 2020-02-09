import argparse

import core

from message_queue import commands
logger = core.get_logger(__name__)
DESCRIPTION = "Message Queue"


def parse_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    help_text = "\n".join([f"{command['key']}: {command['description']}" for command in command_list])
    parser.add_argument("command", help=help_text)

    help_text = "The topic of the message"
    parser.add_argument("--topic", dest="topic", help=help_text)

    help_text = "The target service"
    parser.add_argument("--service", dest="service", help=help_text)

    help_text = "The unique identifier of a resource or queue"
    parser.add_argument("--identifier", dest="identifier", help=help_text)

    return parser.parse_args()


def main():
    args = parse_args()
    command = args.command
    method = command_map.get(command)
    if method:
        method(args)
    else:
        logger.warning(f"[{command}] not registered")


command_list = [
    {
        "key": "process-topic",
        "description": "Process a specified topic",
        "method": commands.process_topic,
    },
    {
        "key": "process-queue",
        "description": "Run a message queue worker",
        "method": commands.process_queue,
    },
    {
        "key": "process-forever",
        "description": "Run a message queue worker",
        "method": commands.process_forever,
    },
    {
        "key": "list-queue",
        "description": "List running queues",
        "method": commands.list_queues,
    },
    {
        "key": "list-resource",
        "description": "List running resources",
        "method": commands.list_resources,
    },
    {
        "key": "kill-queue",
        "description": "Kill a running queue",
        "method": commands.kill_queue,
    },
    {
        "key": "kill-resource",
        "description": "Kill a resource worker",
        "method": commands.kill_resource,
    },

]
command_map = {v["key"]: v["method"] for v in command_list}
main()
