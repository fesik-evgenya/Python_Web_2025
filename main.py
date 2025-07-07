# Внешние библиотеки
# Документы
# Word - DOCX (python - DOCX)
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
# для размеров
from docx.shared import  Mm   # Inches(дюймы) Mm(миллиметры) Pt(Поинт - 1/72 дюйма)

doc = Document()  # создание экземпляра документа
# Добавление заголовка
heading = doc.add_heading('Отчёт за месяц', 1)
heading.alignment= WD_ALIGN_PARAGRAPH.CENTER

paragraph = doc.add_paragraph('В этом отчёте представлены')
paragraph.alignment= WD_ALIGN_PARAGRAPH.CENTER
# run - что-то внутри абзаца ( текст, картинка и т.п.)
paragraph.add_run(' ключевые показатели').bold = True

# Новый параграф для списка
paragraph = doc.add_paragraph()  # вставляем пустую строку
paragraph_format = paragraph.paragraph_format
paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

# маркированный список
paragraph = doc.add_paragraph('Первый пункт', style='List Bullet')
paragraph = doc.add_paragraph('Второй пункт', style='List Bullet')

# нумерованный список
paragraph = doc.add_paragraph('Первый пункт', style='List Number')
paragraph = doc.add_paragraph('Второй пункт', style='List Number')

# добавляем таблицу
table = doc.add_table(rows=3, cols=3)
# Заполняем таблицу
for i, row in enumerate(table.rows):
    for j, cell in enumerate(table.columns):
        cell.text = f'Строка {i+1}, Столбец{j+1}'

doc.add_paragraph()
doc.add_picture('./images/sunny_day_2.jpg', width=Mm(105))

doc.save('./docs/report.docx')

# Word - DOCX (docxtpl)
from docxtpl import DocxTemplate

# Загрузка шаблона
doc = DocxTemplate('./docs/template.docx')

# Данные для подставки в шаблон
content = {
    'company': 'ООО "Монолит"',
    'employee': 'Петров Д.И.',
    'position': 'Менеджер',
    'date': '01/01/2025'
}

doc.render(content)
doc.save('docs/about.docx')