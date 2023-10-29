import datetime
from long_weekends.long_weekends import spot_holiday_bridges

sorted_dates_dict = {'1η Ιανουαρίου': '01 01', 'Φώτα': '06 01', 'Καθαρά Δευτέρα': '12 3', '25η Μαρτίου': '25 03',
                     '1η Απριλίου': '01 04', 'Μεγάλη Παρασκευή': '27 4', 'Πάσχα': '29 4', 'Δευτέρα Πάσχα': '30 4',
                     'Πρωτομαγιά': '01 05', 'Δευτέρα Κατακλυσμού': '18 6', 'Δεκαπενταύγουστος': '15 08',
                     '1η Οκτωβρίου': '01 10', '28η Οκτωβρίου': '28 10', 'Χριστούγεννα': '25 12',
                     '26η Δεκεμβρίου': '26 12'}
days_dict = {'1η Ιανουαρίου': 'Δευτέρα', 'Φώτα': 'Σάββατο', 'Καθαρά Δευτέρα': '12 Μαρτίου', '25η Μαρτίου': 'Κυριακή',
             '1η Απριλίου': 'Κυριακή', 'Μεγάλη Παρασκευή': '27 Απριλίου', 'Πάσχα': '29 Απριλίου',
             'Δευτέρα Πάσχα': '30 Απριλίου', 'Πρωτομαγιά': 'Τρίτη', 'Δευτέρα Κατακλυσμού': '18 Ιουνίου',
             'Δεκαπενταύγουστος': 'Τετάρτη', '1η Οκτωβρίου': 'Δευτέρα', '28η Οκτωβρίου': 'Κυριακή',
             'Χριστούγεννα': 'Τρίτη', '26η Δεκεμβρίου': 'Τετάρτη'}

#
# consecutive_holidays = set()
# sorted_dates = list(sorted_dates_dict.keys())
# for index, date in enumerate(sorted_dates):
#     day = days_dict[date]
#
#     current_date_num = sorted_dates_dict[date]
#     previous_date_num = sorted_dates_dict[sorted_dates[index - 1]]
#     current_holiday = datetime.datetime(2023, day=int(current_date_num.split(" ")[0]),
#                                         month=int(current_date_num.split(" ")[1]))
#     previous_holiday = datetime.datetime(2023, day=int(previous_date_num.split(" ")[0]),
#                                          month=int(previous_date_num.split(" ")[1]))
#
#     if day == "Δευτέρα" or day == "Παρασκευή":
#         consecutive_holidays.add(current_holiday)
#
#     if date == "1η Ιανουαρίου":
#         continue
#
#     date_diff = (current_holiday - previous_holiday).days
#     if date_diff == 1:
#         consecutive_holidays.add(previous_holiday)
#         consecutive_holidays.add(current_holiday)
#
#
# print(consecutive_holidays)

holidays = [datetime.datetime(2035, day=int(date.split(" ")[0]), month=int(date.split(" ")[1]))
            for date in sorted_dates_dict.values()]

start = '2035-01-01'
end = '2035-12-31'

bridges, long_weekends = spot_holiday_bridges(
    start=start, end=end, holidays=holidays)
print(bridges)
print("==============")
print(long_weekends)
