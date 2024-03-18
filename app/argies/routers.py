from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import datetime
from datetime import timedelta
import calendar
import traceback
from dateutil import easter
import copy


templates = Jinja2Templates(directory="./templates")
router = APIRouter()


def log_exception(e):
    print(f"Exception encountered: {e}")
    print(traceback.format_exc())


def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return calendar.day_name[born]


def custom_sort_key(date, dates_dict):
    day, month = map(int, dates_dict[date].split())
    return month, day


dates = {"1η Ιανουαρίου": "01 01", "Φώτα": "06 01", "25η Μαρτίου": "25 03", "1η Απριλίου": "01 04",
         "Πρωτομαγιά": "01 05", "Δεκαπενταύγουστος": "15 08", "1η Οκτωβρίου": "01 10", "28η Οκτωβρίου": "28 10",
         "Χριστούγεννα": "25 12", "26η Δεκεμβρίου": "26 12"}

greek_months = {"1": "Ιανουαρίου", "2": "Φεβρουαρίου", "3": "Μαρτίου", "4": "Απριλίου", "5": "Μαΐου",
                "6": "Ιουνίου", "7": "Ιουλίου", "8": "Αυγούστου", "9": "Σεπτεμβρίου",
                "10": "Οκτωβρίου", "11": "Νοεμβρίου", "12": "Δεκεμβρίου"}

greek_days = {"Monday": "Δευτέρα", "Tuesday": "Τρίτη", "Wednesday": "Τετάρτη", "Thursday": "Πέμπτη",
              "Friday": "Παρασκευή", "Saturday": "Σάββατο", "Sunday": "Κυριακή"}

year_min = datetime.datetime.now().year
year_max = year_min + 30


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.get("/all_years")
async def all_years_endpoint():
    try:
        dates_copy = copy.deepcopy(dates)
        years_dict = {}
        for year in range(year_min, year_max):
            number_of_weekends = 0
            for date in dates_copy.values():
                day = findDay(f"{date} {str(year)}")
                day = greek_days[day]
                if day == "Σάββατο" or day == "Κυριακή":
                    number_of_weekends += 1
            years_dict[year] = number_of_weekends
        return years_dict

    except ValueError as e:
        log_exception(e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        log_exception(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/year")
async def specific_year_endpoint(year: int):
    try:
        dates_copy = copy.deepcopy(dates)
        easter_date = easter.easter(year, method=2)
        easter_string_date = f"{easter_date.day} {easter_date.month}"
        kathara_deftera = easter_date - timedelta(days=48)
        kathara_deftera_string = f"{kathara_deftera.day} {kathara_deftera.month}"
        megali_paraskevi = easter_date - timedelta(days=2)
        megali_paraskevi_string = f"{megali_paraskevi.day} {megali_paraskevi.month}"
        deftera_pasxa = easter_date + timedelta(days=1)
        deftera_pasxa_string = f"{deftera_pasxa.day} {deftera_pasxa.month}"
        kataklismos = easter_date + timedelta(days=50)
        kataklismos_string = f"{kataklismos.day} {kataklismos.month}"

        dates_copy["Πάσχα"] = easter_string_date
        dates_copy["Καθαρά Δευτέρα"] = kathara_deftera_string
        dates_copy["Μεγάλη Παρασκευή"] = megali_paraskevi_string
        dates_copy["Δευτέρα Πάσχα"] = deftera_pasxa_string
        dates_copy["Δευτέρα Κατακλυσμού"] = kataklismos_string

        sorted_dates = sorted(dates_copy.keys(), key=lambda date: custom_sort_key(date, dates_copy))
        sorted_dates_dict = {date: dates_copy[date] for date in sorted_dates}

        days_dict = {}
        for date_string, date_num in sorted_dates_dict.items():
            if date_string in ["Πάσχα", "Καθαρά Δευτέρα", "Μεγάλη Παρασκευή", "Δευτέρα Πάσχα", "Δευτέρα Κατακλυσμού"]:
                split = date_num.split(" ")
                day = split[0]
                month = split[1]
                days_dict[date_string] = f"{day} {greek_months[month]}"
            else:
                day = findDay(f"{date_num} {str(year)}")
                days_dict[date_string] = greek_days[day]

        return days_dict

    except ValueError as e:
        log_exception(e)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        log_exception(e)
        raise HTTPException(status_code=500, detail=str(e))
