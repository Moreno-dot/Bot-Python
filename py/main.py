import os
import argparse
import shutil

# Define a function to clean a directory
def clean_directory(path):
    print(f"Limpando o diretório {path}")
    dir_content = os.listdir(path)
    print(f"Limpando {len(dir_content)} elementos.")
    
    # Create a dictionary to store files by extension
    files_by_extension = {}
    for file in dir_content:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1][1:]
            if file_extension not in files_by_extension:
                files_by_extension[file_extension] = []
            files_by_extension[file_extension].append(file_path)
    
    # Create folders for each extension and move files
    for extension, files in files_by_extension.items():
        folder_path = os.path.join(path, extension)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        for file in files:
            shutil.move(file, folder_path)
            print(f"Arquivo {file} movido para {folder_path}")

# Define a function to organize files by type
def organize_files_by_type(path):
    print(f"Organizando arquivos por tipo em {path}")
    dir_content = os.listdir(path)
    
    # Create folders for each file type
    file_types = ["images", "documents", "videos", "audio"]
    for file_type in file_types:
        folder_path = os.path.join(path, file_type)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
    
    # Move files to corresponding folders
    for file in dir_content:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file)[1][1:]
            if file_extension in ["jpg", "jpeg", "png"]:
                shutil.move(file_path, os.path.join(path, "images"))
            elif file_extension in ["doc", "docx", "pdf"]:
                shutil.move(file_path, os.path.join(path, "documents"))
            elif file_extension in ["mp4", "avi"]:
                shutil.move(file_path, os.path.join(path, "videos"))
            elif file_extension in ["mp3", "wav"]:
                shutil.move(file_path, os.path.join(path, "audio"))

# Define a function to delete empty folders
def delete_empty_folders(path):
    print(f"Deletando pastas vazias em {path}")
    dir_content = os.listdir(path)
    for folder in dir_content:
        folder_path = os.path.join(path, folder)
        if os.path.isdir(folder_path) and len(os.listdir(folder_path)) == 0:
            os.rmdir(folder_path)
            print(f"Pasta vazia {folder_path} deletada")

# Define the main function
def main():
    parser = argparse.ArgumentParser(description="Limpa e organiza um diretório.")
    parser.add_argument("--path", type=str, default=".", help="Caminho do diretório a ser limpo")
    args = parser.parse_args()
    path = args.path
    
    clean_directory(path)
    organize_files_by_type(path)
    delete_empty_folders(path)

if __name__ == "__main__":
    main()