import unicodedata
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')

def format_currency(value: str) -> float or str:
    if not value:
        return 0.0
    elif isinstance(value, str):
        if "%" in value:
            value = value.replace("%", "").strip()
    try:
        return locale.atof(value)
    except:
        return value

def strip_accents(s: str) -> str:
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')