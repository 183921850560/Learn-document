# coding=utf-8
import re


def equals(check_value, expect_value):
    assert check_value == expect_value, "预期 %s 等于 %s" %(check_value, expect_value)

def less_than(check_value, expect_value):
    assert check_value < expect_value, "%s >= %s" %(check_value, expect_value)

def less_than_or_equals(check_value, expect_value):
    assert check_value <= expect_value, "%s > %s" %(check_value, expect_value)

def greater_than(check_value, expect_value):
    assert check_value > expect_value, "%s <= %s" %(check_value, expect_value)

def greater_than_or_equals(check_value, expect_value):
    assert check_value >= expect_value, "%s < %s" %(check_value, expect_value)

def not_equals(check_value, expect_value):
    assert check_value != expect_value, "预期不等于 %s" % expect_value

def string_equals(check_value, expect_value):
    assert str(check_value) == str(expect_value), "%s 不等于 %s" %(check_value, expect_value)

def length_equals(check_value, expect_value):
    assert isinstance(expect_value, int), "expect_value: %s 不是INT类型"% expect_value
    assert len(check_value) == expect_value , "长度 %s 不等于 %s" %(len(check_value), expect_value)

def length_greater_than(check_value, expect_value):
    assert isinstance(expect_value, int), "expect_value: %s 不是INT类型"% expect_value
    assert len(check_value) > expect_value , "长度 %s <= %s" %(len(check_value), expect_value)

def length_greater_than_or_equals(check_value, expect_value):
    assert isinstance(expect_value, int), "expect_value: %s 不是INT类型"% expect_value
    assert len(check_value) >= expect_value, "长度 %s < %s" %(len(check_value), expect_value)

def length_less_than(check_value, expect_value):
    assert isinstance(expect_value, int), "expect_value: %s 不是INT类型"% expect_value
    assert len(check_value) < expect_value, "长度 %s >= %s" %(len(check_value), expect_value)

def length_less_than_or_equals(check_value, expect_value):
    assert isinstance(expect_value, int),"expect_value: %s 不是INT类型"% expect_value
    assert len(check_value) <= expect_value, "长度 %s > %s" %(len(check_value), expect_value)

def contains(check_value, expect_value):
    assert isinstance(check_value, (list, tuple, dict, str)), "check_value: 类型错误"
    assert expect_value in check_value, " %s 不包含 %s" %(check_value, expect_value)

def contained_by(check_value, expect_value):
    assert isinstance(expect_value, (list, tuple, dict, str)), "expect_value: 类型错误"
    assert check_value in expect_value, " %s 不包含于 %s" %(check_value, expect_value)


def regex_match(check_value, expect_value):
    assert isinstance(expect_value, str),"expect_value: %s 不是String类型"% expect_value
    assert isinstance(check_value, str),"check_value: %s 不是INT类型"% check_value
    assert re.match(expect_value, check_value), " %s 正则表达式不匹配 %s" %(check_value, expect_value)

def startswith(check_value, expect_value):
    assert str(check_value).startswith(str(expect_value)), " %s 不是以 %s 字符开头" %(check_value, expect_value)

def endswith(check_value, expect_value):
    assert str(check_value).endswith(str(expect_value)), " %s 不是以 %s 字符结尾" %(check_value, expect_value)

def all_equals(check_value, expect_value):
    assert isinstance(check_value, (list, tuple, dict))
    for check in check_value:
        if isinstance(expect_value,int):
            check = float(check)
        assert check == expect_value , "列表中的 %s 不相等于 %s" %(check, expect_value)
def all_contains(check_value, expect_value):
    assert isinstance(check_value,list)
    for ck in check_value:
        assert expect_value in ck , " %s 不包含 %s" %(ck, expect_value)


def is_sort(check_value, expect_value):
    """
    检查数组是否排序
    :param check_value:
    :param expect_value
    :return:
    """
    assert isinstance(check_value,list)
    order = 'desc'
    if check_value == sorted(check_value):
        order = 'asc'
    elif check_value == sorted(check_value, reverse=True):
        order = 'desc'
    assert order.lower() == expect_value.lower(), "没有按指定字段排序"


def get_uniform_comparator(comparator):
    """ convert comparator alias to uniform name
    """
    if comparator in ["eq", "equals", "==", "is"]:
        return "equals"
    elif comparator in ["lt", "less_than","<"]:
        return "less_than"
    elif comparator in ["le", "less_than_or_equals","<="]:
        return "less_than_or_equals"
    elif comparator in ["gt", "greater_than",">"]:
        return "greater_than"
    elif comparator in ["ge", "greater_than_or_equals",">="]:
        return "greater_than_or_equals"
    elif comparator in ["ne", "not_equals","!="]:
        return "not_equals"
    elif comparator in ["str_eq", "string_equals"]:
        return "string_equals"
    elif comparator in ["len_eq", "length_equals", "count_eq"]:
        return "length_equals"
    elif comparator in ["len_gt", "count_gt", "length_greater_than", "count_greater_than"]:
        return "length_greater_than"
    elif comparator in ["len_ge", "count_ge", "length_greater_than_or_equals", "count_greater_than_or_equals"]:
        return "length_greater_than_or_equals"
    elif comparator in ["len_lt", "count_lt", "length_less_than", "count_less_than"]:
        return "length_less_than"
    elif comparator in ["len_le", "count_le", "length_less_than_or_equals","count_less_than_or_equals"]:
        return "length_less_than_or_equals"
    else:
        return comparator
try:
    equals(1,1)
except AssertionError as e:
    print(e)
