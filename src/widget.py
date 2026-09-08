from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(line: str) -> str:
    """Базовая функция для маскировки номеров карт"""
    line = line.strip()
    if not line:
        return "Ошибка: Введена пустая строка"
    parts = line.split(" ")
    if len(parts) < 2:
        return "Ошибка: Некорректный формат (должно быть название и номер через пробел)"
    digits = parts[-1]
    letters = " ".join(parts[:-1])
    if "счет" in letters.lower():
        masked_digits = get_mask_account(digits)
    else:
        masked_digits = get_mask_card_number(digits)
    return f"{letters} {masked_digits}"


def get_date(iso: str) -> str:
    """
    принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    target_date = datetime.fromisoformat(iso)
    return target_date.strftime("%d.%m.%Y")


if __name__ == "__main__":
    print(mask_account_card(""))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:13"))
