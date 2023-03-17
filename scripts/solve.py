from xml.etree import ElementTree as ET

def parse_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    columns = []
    rows = []

    for clues in root.iter('clues'):
        clue_type = clues.get('type')
        lines = []
        for line in clues.iter('line'):
            counts = []
            for count in line.iter('count'):
                if 'color' in count.attrib:
                    color = count.attrib['color']
                    counts.append((color, int(count.text)))
                else:
                    counts.append(('black', int(count.text)))
            lines.append(counts)

        if clue_type == 'columns':
            columns = lines
        elif clue_type == 'rows':
            rows = lines

    return rows, columns


# rows, columns=parse_xml('../puzzles/1.xml')
# print(columns)
# print(rows)




