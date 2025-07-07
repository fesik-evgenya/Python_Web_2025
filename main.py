# Внешние библиотеки
# Документы
# Excel (openpyxl)
# работа с формулами: ws['A3'] = "=SUM(A1:A10)"
# Форматирование = from openpyxl.style import Font
#                  ws['A1'].font = Font(bolt=True, size=14)
from openpyxl import Workbook, load_workbook
#
# # Создаём пустой Excel-файл
# wb = Workbook()
# ws = wb.active
# ws.title = 'Отчёт'
#
# wb.save('./docs/report.xlsx')

# Запись данных в существующий файл
wb = load_workbook('./docs/report.xlsx')
# обращаемся к активному листу
ws = wb.active

# Способы записи
ws['A1'] = 'Отчёт за 01.06.2025 - 15.06.2025 гг'
ws.cell(row=2, column=1, value='Автор: Фесик Е.В.')

# заполняем
ws['A4'] = 'ФИО'
ws['B4'] = 'Должность'
ws['C4'] = 'Отдел'

# Данные
employees = [
    ['Иванов И.И.', 'Менеджер', 'Продажи'],
    ['Петров П.П.', 'Бухгалтер', 'Финансы'],
    ['Сидорова С.С.', 'Аналитик', 'IT'],
]

for row, data in enumerate(employees, start=5):
    ws.cell(row=row, column=1, value=data[0])
    ws.cell(row=row, column=2, value=data[1])
    ws.cell(row=row, column=3, value=data[2])

wb.save('./docs/report_01062025-15062025.xlsx')

wb = load_workbook('./docs/report_01062025-15062025.xlsx')
ws = wb.active

rows_count = ws.max_row  # число заполненных строк

for row in ws.iter_rows(values_only=True, min_row=5):
    fio, pos, dept = row
    print(f'Фамилия: {fio}, Должность: {pos}, Отдел: {dept}')