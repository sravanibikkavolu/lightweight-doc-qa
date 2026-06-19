import re

def split_sections(markdown_text):

    sections = re.split(r"\n# ", markdown_text)

    cleaned = []

    for section in sections:

        section = section.strip()

        if len(section) > 50:
            cleaned.append(section)

    return cleaned


def find_section(question, sections):

    best_score = 0
    best_section = ""

    for section in sections:

        score = sum(
            word.lower() in section.lower()
            for word in question.split()
        )

        if score > best_score:
            best_score = score
            best_section = section

    return best_section