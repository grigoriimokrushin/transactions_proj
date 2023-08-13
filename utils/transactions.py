import json, os


def read_json_file(file: json) -> list:
    """Возвращает из фаила JSON список словарей Python с помощью json"""
    with open(os.path.abspath(file), 'r', encoding='utf-8') as f:
        transactions = json.load(f)
        return transactions


def get_last_five_executed(transactions: list) -> list:
    """Возвращает из списка словарей ВСЕХ операций список из
    ПЯТИ ПОСЛЕДНИХ УСПЕШНЫХ операций
    начиная с самой последней с помощью функции sorted"""
    transactions = [trans for trans in transactions if trans]
    sorted_transactions = sorted(transactions[:50], key=lambda x: x['date'], reverse=True)
    executed_transactions = sorted(sorted_transactions[:50], key=lambda x: x['state'], reverse=True)
    return executed_transactions[0:5]


def get_right_format(last_five_operations: list):
    """Приводим информацию из списка словарей последних пяти операций
     в нужный нам формат для последующего вывода на экран"""
    for transaction in last_five_operations:
        from_ = transaction.get('from')
        to_ = transaction.get('to')
        transaction['to'] = (to_[:5] + '**' + to_[-4:])
        if from_ is None:
            transaction['from'] = 'Неизвестно'
        elif 'Счет' in from_:
            transaction['from'] = (from_[:9] + ' ' + from_[-16:-12] + ' ' + from_[-12:-10] + '** **** ' + from_[-4:])
        else:
            transaction['from'] = (from_[:-12] + ' ' + from_[-12:-10] + '** **** ' + from_[-4:])
    return last_five_operations


