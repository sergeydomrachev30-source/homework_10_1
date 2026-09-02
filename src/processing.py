from typing import List


def filter_by_state(data: List, state: str = "EXECUTED") -> List:
    """
    принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED') и возвращает новый список словарей, содержащий
    только те словари, у которых ключ state  соответствует указанному значению
    """
    target_list = []
    for item in data:
        if item["state"] == state:
            target_list.append(item)
    return target_list


def sort_by_date(data: List, ascending: bool = True) -> List:
    """Сортирует список словарей по ключу 'date'."""
    return sorted(data, key=lambda x: x["date"], reverse=ascending)
