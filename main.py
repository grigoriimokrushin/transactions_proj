from utils.transactions import read_json_file, get_last_five_executed, get_right_format
import datetime

FILE_NAME = "operations.json"

information_about_all_operations = read_json_file(FILE_NAME)

last_five_operations = get_last_five_executed(information_about_all_operations)

last_five_for_print = get_right_format(last_five_operations)

format_ = '%Y-%m-%dT%H:%M:%S.%f'
new_format = '%d.%m.%Y'

for transaction in last_five_for_print:
    date = datetime.datetime.strptime(transaction['date'], format_)
    transaction['date'] = date.strftime(new_format)
    print(f"{transaction['date']} {transaction['description']}\n"
          f"{transaction['from']} -> {transaction['to']}\n"
          f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}\n")


################################
