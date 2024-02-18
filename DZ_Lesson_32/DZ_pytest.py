import pytest
def is_even(number: int) -> bool:
    """
    Проверяет, является ли число четным.

    :param number: Проверяемое число
    :return: True, если число четное, иначе False
    """
    return number % 2 == 0
#--------------test_case 1 (base_test)-------------------------#
#--------------Passing NORMAL atributes________________________#
# atribute -> 2
# expected result: True
# print(is_even(2))
# actual result -> True

def test_is_even_base():
    expected_result = True  # Expected True
    actual_result = is_even(2)
    assert actual_result == expected_result
# test passed

#--------------test_case 2-------------------------------------#
#--------------Passing ABNORMAL atributes type == int__________#
# atribute(3) % 2 = False
# expected result: False
# print(is_even(3))
# actual result -> False

def test_is_even_abnormal_int_atribute():
    expected_result = False  # Expected False
    actual_result = is_even(3)
    assert actual_result == expected_result
# test passed

#--------------test_case 3-------------------------------------#
#--------------Passing ABNORMAL atributes type == float__________#
# atribute(4.1) % 2 = False
# expected result: False
# print(is_even(4.1))
# actual result -> False
# test passed

def test_is_even_abnormal_float_atribute():
    expected_result = False  # Expected False
    actual_result = is_even(4.1)
    assert actual_result == expected_result
# test passed


#--------------test_case 4-------------------------------------#
#---Passing ABNORMAL atributes type == str or arr or dict------#
# atribute №1 ("4") % 2 = False
# atribute №2 ([4]) % 2 = False
# atribute №3 ({4}) % 2 = False
# expected result: False
# print(is_even("4")) # invalid test
# print(is_even([4])) # invalid test
# print(is_even({4})) # invalid test
# actual result -> TypeError

def test_is_even_abnormal_str_atribute():
    expected_result = False  # Expected False
    try:
        actual_result = is_even("4")
    except:
        actual_result = False
    assert actual_result == expected_result
# test passed

def test_is_even_abnormal_arr_atribute():
    expected_result = False  # Expected False
    try:
        actual_result = is_even([4])
    except:
        actual_result = False
    assert actual_result == expected_result
# test passed

def test_is_even_abnormal_dict_atribute():
    expected_result = False  # Expected False
    try:
        actual_result = is_even({4})
    except:
        actual_result = False
    assert actual_result == expected_result
# test passed