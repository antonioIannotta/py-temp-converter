def converter(source: str, source_val: float, dest: str) -> float:
    """
    This method takes the temperature to be converted, the input unit measure and the desired unit measure
    :param source: the input unit measure
    :param source_val: the value to be converted
    :param dest: the desired unit input
    :return: the value converted from the source unit measure to the output unit measure
    :raises ValueError: If an invalid unit is provided
    """

    if source not in {"c", "k", "f"} or dest not in {"c", "k", "f"}:
        raise ValueError("Invalid temperature unit. Use 'c', 'k', or 'f'.")

    if not isinstance(source_val, (int, float)):
        raise TypeError("source_val must be a numeric value.")

    conversions = {
        ("c", "k"): from_c_to_k(source_val),
        ("c", "f"): from_c_to_f(source_val),
        ("k", "c"): from_k_to_c(source_val),
        ("k", "f"): from_k_to_f(source_val),
        ("f", "c"): from_f_to_c(source_val),
        ("f", "k"): from_f_to_k(source_val)
    }

    if source == dest:
        return  source_val

    return conversions[(source, dest)]


def from_c_to_k(source_val: float) -> float:
    """
    This method converts the value provided in input from the Celsius to the Kelvin unit measure
    :param source_val: the temperature value
    :return: the converted temperature value
    """
    return 273.15 + source_val

def from_c_to_f(source_val: float) -> float:
    """
    This method converts the value provided in input from the Celsius to the Fahrenheit unit measure
    :param source_val: the temperature value
    :return: the converted temperature value
    """
    return 1.8 * source_val + 32

def from_k_to_c(source_val: float) -> float:
    """
    This method converts the value provided in input from the Kelvin to the Celsius unit measure
    :param source_val: the temperature value
    :return: the converted temperature value
    """
    return source_val - 273.15

def from_k_to_f(source_val: float) -> float:
    """
    This method converts the value provided in input from the Kelvin to the Fahrenheit unit measure
    :param source_val: the temperature value
    :return: the converted temperature value
    """
    return from_c_to_f(from_k_to_c(source_val))

def from_f_to_c(source_val: float) -> float:
    """
    This method converts the value provided in input from the Fahrenheit to the Celsius unit measure
    :param source_val: the temperature value
    :return: the converted temperature value
    """
    return 5/9 * (source_val - 32)

def from_f_to_k(source_val: float) -> float:
    """
    This method converts the value provided in input from the Fahrenheit to the Kelvin unit measure
    :param source_val: the temperature value
    :return: the converted temperature value
    """
    return from_c_to_k(from_f_to_c(source_val))