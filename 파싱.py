import xml.parsers.expat



def start_element(name, attrs):
    print("Start element:", name, attrs)



def char_data(data):
    print("Character data:", repr(data))

pa = xml.parsers.expat.ParserCreate()

pa.StartElementHandler = start_element
pa.CharacterDataHandler = char_data




