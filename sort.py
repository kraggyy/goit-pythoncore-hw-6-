import os
import shutil
import sys
from transliterate import translit

EXTENSIONS = {
    'images': ('.jpeg', '.png', '.jpg', '.svg'),
    'video': ('.avi', '.mp4', '.mov', '.mkv'),
    'audio': ('.mp3', '.ogg', '.wav', '.amr'),
    'documents': ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx', '.odt'),
    'archives': ('.zip', '.gz', '.tar')
}

UNKNOWN_FOLDER = 'unknown'
output_directory = "./output"  # Ваша вихідна папка

def normalize(filename):
    # Функція для транслітерації та очищення імен файлів
    filename = translit(filename, 'ru', reversed=True)  # Транслітерація кирилічного тексту
    normalized = ''.join(c if c.isalnum() or c == '.' else '_' for c in filename)
    return normalized

def organize_files(directory):
    known_extensions = set()
    unknown_extensions = set()
    
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)  # Видалення порожньої папки
        
        for file in files:
            # Отримати розширення файлу
            filename, extension = os.path.splitext(file)
            extension = extension.lower()  # Перетворити розширення в нижній регістр
            
            # Визначити категорію файлу
            category = 'UNKNOWN_FOLDER'
            for cat, exts in EXTENSIONS.items():
                if extension in exts:
                    category = cat
                    known_extensions.add(extension)
                    break
            
            source_path = os.path.join(root, file)
            target_dir = os.path.join(output_directory, category)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            
            target_file = os.path.join(target_dir, normalize(filename) + extension)
            
            # Перемістити та перейменувати файл
            shutil.move(source_path, target_file)
    
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
