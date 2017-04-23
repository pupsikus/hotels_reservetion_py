from datetime import datetime
import re


def check_dates_range(start_date, end_date):
    """
    :type start_date: datetime
    :type type end_date: datetime
    :return: list of errors
    :type return: list
    """
    err_list = []
    if not start_date:
        err_list.append(ValueError('"start date" has an empty value. '))

    if not end_date:
        err_list.append(ValueError('"end date" has an empty value. '))

    if type(start_date) is not datetime:
        _msg = ('"start date" has a wrong type(not a datetime). '
                '"start date" type = "%s", value = "%s"') \
               % (type(start_date), start_date)
        err_list.append(TypeError(_msg))

    if type(end_date) is not datetime:
        _msg = ('"end date" has a wrong type(not a datetime). '
                '"end date" type = "%s", value = "%s"') \
               % (type(end_date), end_date)
        err_list.append(TypeError(_msg))

    if err_list:
        return err_list, start_date, end_date

    today = datetime.now().date()
    start_date = start_date.date()
    end_date = end_date.date()
    if start_date < today:
        err_list.append(ValueError('"start date" is earlier than today '
                                   'date'))
    if end_date < start_date:
        err_list.append(ValueError('"end date" is earlier than start '
                                   'date'))
    # TODO: check maximum number of reservations dates and other handlers
    return err_list, start_date, end_date


def check_int(in_value, name):
    err_list = []
    if not in_value:
        err_list.append(
            ValueError('Empty value. Arg name = "%s"' % name))
        return err_list

    if type(in_value) is not int:
        _msg = ('Wrong argument type(not an interger). Arg name = "%s", '
                'value = "%s", type = "%s"') % (name, in_value,
                                                type(in_value))
        err_list.append(TypeError(_msg))
    # TODO: check maximum int number
    return err_list


def check_string(in_value, name):
    err_list = []
    if not in_value:
        err_list.append(ValueError('Empty value. Arg name = "%s"' % name))
        return err_list

    if type(in_value) is not str:
        _msg = ('Wrong argument type(not a string). Arg name = "%s", '
                'value = "%s", type = "%s"') % (name, in_value,
                                                type(in_value))
        err_list.append(TypeError(_msg))
    _failed = re.match(r'[^a-z^A-Z]', in_value)
    if _failed:
        err_list.append(
            ValueError('Wrong argument value. Arg name = "%s", '
                       'value = "%s"' % (name, in_value))
        )
    # TODO: check maximum string length
    return err_list