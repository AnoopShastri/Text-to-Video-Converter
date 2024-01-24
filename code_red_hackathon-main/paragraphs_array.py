with open("generated_text.txt", "r") as file:
    text = file.read()
#paragraphs = text.splitlines()
paragraphs = [para.strip() for para in text.splitlines() if para.strip()]