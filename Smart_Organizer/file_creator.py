import os


folder_path = "C:\\Users\kushk\Python Projects/projects\\Smart_Organizer"


file_samples = [
    "resume.pdf", "report.docx", "photo1.jpg", "photo2.png", "script.py",
    "video.mp4", "presentation.pptx", "data.csv", "archive.zip", "notes.txt"
]


for file_name in file_samples:
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as file:
        file.write("sample file")
print("Sample Files Created")