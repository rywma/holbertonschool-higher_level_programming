#!/usr/bin/python3
"""Generate personalized invitation files from a template."""
import logging

logging.basicConfig(level=logging.INFO)


def generate_invitations(template, attendees):
    """Generate output_X.txt files by filling a template per attendee."""
    if not isinstance(template, str):
        logging.error("Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(
        isinstance(a, dict) for a in attendees
    ):
        logging.error("Attendees must be a list of dictionaries.")
        return
    if template == "":
        logging.error("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        logging.error("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = f"output_{index}.txt"
        with open(filename, "w") as f:
            f.write(content)