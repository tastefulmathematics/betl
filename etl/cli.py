import argparse

import core

from etl import commands
logger = core.get_logger(__name__)
DESCRIPTION = "File Processing"


def parse_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    help_text = "\n".join([f"{command['key']}: {command['description']}" for command in command_list])
    parser.add_argument("command", help=help_text)

    help_text = "The S3 URI to locate the file"
    parser.add_argument("--s3-uri", dest="s3_uri", help=help_text)

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
        "key": "validate-configuration",
        "description": "Validate configuration of the message queue",
        "method": commands.validate_configuration,
    },
    {
        "key": "process-file",
        "description": "Process the file for a given s3 uri",
        "method": commands.process_file,
    },
    {
        "key": "file-configuration",
        "description": "Print the configuration for the file for a given s3 uri",
        "method": commands.file_configuration,
    },
]
command_map = {v["key"]: v["method"] for v in command_list}
main()
