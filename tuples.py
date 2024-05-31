"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[-1]


def convert_coordinate(coordinate):
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    coordinate = get_coordinate(azara_record)
    convert = convert_coordinate(coordinate)
    if convert == rui_record[1]:
        return True
    return False

def create_record(azara_record, rui_record):
    if compare_records(azara_record, rui_record) is True:
        return azara_record + rui_record
    return 'not a match'


def clean_up(combined_record_group):
    report = []
    for record in combined_record_group:
        item, _, location, coordinate, color = record
        cleaned_record = (item, location, coordinate, color)
        report.append(cleaned_record)
    
    format_report = "".join(f"{record}\n" for record in report)
    return format_report