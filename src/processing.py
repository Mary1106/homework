def filter_by_state(list_of_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Принимает список словарей и значение для ключа state (по умолчанию 'EXECUTED'); возвращает новый список
    словарей, у которых ключ sate соответствует указанному значению."""
    filtered_list = []
    for i in list_of_dict:
        if i.get("state") == state:
            filtered_list.append(i)
        else:
            continue
    return filtered_list


def sort_by_date(list_of_dict: list[dict], reverse: bool = True) -> list[dict]:
    """Принимает список словарей и параметр, задающий порядок сортировки (по умолчанию — убывание); возвращает
    новый список, отсортированный по дате (date)."""
    sorted_list = sorted(list_of_dict, key=lambda dict_in_list: dict_in_list["date"], reverse=reverse)
    return sorted_list
