from app import consume
from app import write_to_text_file
import json
while True:
    d=consume()
    # d=json.dumps(d)
    #print(d,type(d))
    write_to_text_file(str(d))


