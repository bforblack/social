from datetime import datetime


def is_valid_time_format(time_str):
    current_datetime = datetime.now()
    current_date = datetime.today().date()
    try:
        datetime_obj_s = datetime.strptime(time_str, '%H:%M:%S').replace(year=current_date.year,
                                                                         month=current_date.month,
                                                                         day=current_date.day)
        formatted_datetime = datetime.strptime(current_datetime.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        return True, datetime_obj_s, formatted_datetime
    except ValueError:
        try:
            datetime_obj_d_s = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
            formatted_datetime = datetime.strptime(current_datetime.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
            return True, datetime_obj_d_s, formatted_datetime
        except ValueError:
            try:

                datetime_obj_m = datetime.strptime(time_str, '%H:%M').replace(year=current_date.year,
                                                                              month=current_date.month,
                                                                              day=current_date.day)
                formatted_datetime = datetime.strptime(current_datetime.strftime("%Y-%m-%d %H:%M"), "%Y-%m-%d %H:%M")
                return True, datetime_obj_m, formatted_datetime
            except ValueError:
                try:
                    datetime_obj_d_m = datetime.strptime(time_str, '%Y-%m-%d %H:%M')
                    formatted_datetime = datetime.strptime(current_datetime.strftime("%Y-%m-%d %H:%M"),
                                                           "%Y-%m-%d %H:%M")
                    return True, datetime_obj_d_m, formatted_datetime
                except ValueError:
                    return False, None, None



