# scoring/audit_log.py

from datetime import datetime

audit_logs = []


def save_log(action, data):

    log = {

        "timestamp":
        datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        ),

        "action":
        action,

        "details":
        data

    }

    audit_logs.append(log)



def get_logs():

    return audit_logs