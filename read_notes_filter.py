import read_notes as rn
from datetime import datetime

def read_notes_filter():
    from_date = datetime.strptime(input('Введите дату/время в формате ГГГГ-ММ-ДД ЧЧ:ММ (например, 2022-01-01 12:00): '), '%Y-%m-%d %H:%M')
    notes = rn.read_notes()
    notes_filter = [note for note in notes if datetime.strptime(note['created_at'], '%Y-%m-%d %H:%M:%S') >= from_date or note['updated_at'] and datetime.strptime(note['updated_at'], '%Y-%m-%d %H:%M:%S') >= from_date]
    return notes_filter