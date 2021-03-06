import os

from pdf2image import convert_from_path

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

# Для работы библиотеки pdf2image на windows нужно установить poppler - https://blog.alivate.com.au/poppler-windows/


# берём все pdf файлы из своей директории
pdf_files = [filename for filename in os.listdir(
    '.') if filename.endswith('.pdf')]
# прописываем путь сохранения.
save_dir = '../Семь сестёр/1'

for pdf_file in pdf_files:
    images = convert_from_path(pdf_file, size=(None, 1000),
                               jpegopt={"progressive": True})

    for i, image in enumerate(images):
        image.save(os.path.join(save_dir, pdf_file.replace('.pdf', '') + '_' + str(i + 1).zfill(3) + '.jpg'), 'JPEG')
