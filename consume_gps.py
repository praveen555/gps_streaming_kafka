from app import consume
from app import write_to_text_file

while True:
    d=consume()
    write_to_text_file(d)


