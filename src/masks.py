def get_mask_card_number(card_number: int | str) -> str:
    """Возвращает номер карты в формате XXXX XX** **** XXXX."""
    card_number_str = str(card_number)
    if not card_number_str.isdigit():
        msg = "Номер карты должен содержать только цифры."
        raise ValueError(msg)

    if len(card_number_str) != 16:
        msg = "Номер карты должен содержать 16 цифр."
        raise ValueError(msg)

    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account_number: int | str) -> str:
    """Возвращает номер счета в формате **XXXX."""
    account_number_str = str(account_number)
    if not account_number_str.isdigit():
        msg = "Номер счета должен содержать только цифры."
        raise ValueError(msg)

    if len(account_number_str) != 20:
        msg = "Номер счета должен содержать 20 цифр."
        raise ValueError(msg)

    return f"**{account_number_str[-4:]}"
