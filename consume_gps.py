from app import consume
from app import write_to_text_file
import json
while True:
    d=consume()
    # d=json.dumps(d)
    # print(d,type(d))
    for i in d:
        #print(type(i))
        json_string=json.dumps(i)
        #print(json_string)
        write_to_text_file(json_string)


