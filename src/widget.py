from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(line: str) -> str:
    """Базовая функция для маскировки номеров карт (база из прошлого задания)"""
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


if __name__ == "__main__":
    print(mask_account_card(""))
    print(mask_account_card("Счет 73654108430135874305"))
