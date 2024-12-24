def converter(source: str, source_val: float, dest: str) -> float:
    """
    This method takes the temperature to be converted, the input unit measure and the desired unit measure
    :param source: the input unit measure
    :param source_val: the value to be converted
    :param dest: the desired unit input
    :return: the value converted from the source unit measure to the output unit measure
    """
    match source:
        case "c":
            match dest:
                case "k":
                    return from_c_to_k(source_val)
                case "f":
                    return from_c_to_f(source_val)
        case "k":
            match dest:
                case "c":
                    return from_k_to_c(source_val)
                case "f":
                    return from_k_to_f(source_val)
        case "f":
            match dest:
                case "c":
                    return from_f_to_c(source_val)
                case "k":
                    return from_f_to_k(source_val)


def from_c_to_k(source_val: float) -> float:
    """
    This method converts the value provided in input from the Celsius to the Kelvin unit measure
    :param source_val: the temperature value
    :return: the converted temperature value
    """
    pass

def from_c_to_f(source_val: float) -> float:
    """
    This method converts the value provided in input from the Celsius to the Fahrenheit unit measure
    :param source_val: the temperature value
    :return: the converted temperature value
    """
    pass

def from_k_to_c(source_val: float) -> float:
    """
    This method converts the value provided in input from the Kelvin to the Celsius unit measure
    :param source_val: the temperature value
    :return: the converted temperature value
    """
    pass

def from_k_to_f(source_val: float) -> float:
    """
    This method converts the value provided in input from the Kelvin to the Fahrenheit unit measure
    :param source_val: the temperature value
    :return: the converted temperature value
    """
    pass

def from_f_to_c(source_val: float) -> float:
    """
    This method converts the value provided in input from the Fahrenheit to the Celsius unit measure
    :param source_val: the temperature value
    :return: the converted temperature value
    """
    pass

def from_f_to_k(source_val: float) -> float:
    """
    This method converts the value provided in input from the Fahrenheit to the Kelvin unit measure
    :param source_val: the temperature value
    :return: the converted temperature value
    """
    pass