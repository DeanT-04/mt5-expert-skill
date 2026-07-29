import re

def parse_metaeditor_log(log_content):
    """Parse MetaEditor output log to extract error and warning messages."""
    errors = re.findall(r'.*?:\s+error\s+\d+:.*', log_content, re.IGNORECASE)
    warnings = re.findall(r'.*?:\s+warning\s+\d+:.*', log_content, re.IGNORECASE)
    return errors, warnings
