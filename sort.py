import os
import shutil
import sys
from transliterate import translit

EXTENSIONS = {
    'images': ('.jpeg', '.png', '.jpg', '.svg'),
    'videos': ('.avi', '.mp4', '.mov', '.mkv'),
    'documents': ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx''.odt'),
    'music': ('.mp3', '.ogg', '.wav', '.amr'),
    'archives': ('.zip', '.gz', '.tar')
}


UNKNOWN_FOLDER = 'unknown'


output_directory = "./sort_result"



def normalize(filename):
    # Функція для транслітерації та очищення імен файлів
    filename = translit(filename, 'ru', reversed=True)  # Транслітерація кирилічного тексту
    normalized = ''.join(c if c.isalnum() or c == '.' else '_' for c in filename)
    return normalized

def organize_files(directory):
    known_extensions = set()
    unknown_extensions = set()
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Отримати розширення файлу
            _, extension = os.path.splitext(file)
            extension = extension.lower()  # Перетворити розширення в нижній регістр
            
            # Визначити категорію файлу
            category = 'UNKNOWN_FOLDER'
            for cat, exts in EXTENSIONS.items():
                if extension in exts:
                    category = cat
                    known_extensions.add(extension)
                    break
            
            source_path = os.path.join(root, file)
            target_path = os.path.join(output_directory, category, normalize(file))
            
            if not os.path.exists(os.path.join(output_directory, category)):
                os.makedirs(os.path.join(output_directory, category))
            
            # Перемістити та перейменувати файл
            shutil.move(source_path, target_path)
            
    # Повернути результати
    return known_extensions, unknown_extensions

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Використання: python sort.py <шлях до папки>")
    else:
        directory = sys.argv[1]
        known_extensions, unknown_extensions = organize_files(directory)
        
        print("Відомі розширення:")
        print(known_extensions)
        
        print("Невідомі розширення:")
        print(unknown_extensions)