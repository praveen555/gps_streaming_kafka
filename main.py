import datetime

timestamp = [ 1695691508,1695691510,1695691513]
for timestamp in timestamp:
    dt_object = datetime.datetime.fromtimestamp(timestamp)
    print(dt_object)
