from type_constructor import create_type, create_action, create_pair_action
from random import randint
type_dict = dict()
eid = create_type("eid", type_dict, lower_bound=0, upper_bound=100)
cid = create_type("cid", type_dict, lower_bound=0, upper_bound=1000)
tid = create_type("tid", type_dict, lower_bound=0, upper_bound=10000)
amount = create_type("amount", type_dict, lower_bound=0, upper_bound=1000000)
time = create_type("time", type_dict, lower_bound=0, upper_bound=100000)

Trans = create_action("Trans", [("cid", "cid"), ("tid", "tid"), ("amount", "amount"), ("time", "time")],type_dict)
Authorize = create_action("Authorize", [("eid", "eid"), ("tid", "tid"),("cid", "cid"),("time", "time")],type_dict)
Report = create_action("Report", [("tid", "tid"),("time", "time")],type_dict)
TimeStamp = create_action("TimeStamp", [("time", "time")],type_dict)


ACTION = [TimeStamp, Trans, Authorize, Report]
state_action = [TimeStamp]

thresh = randint(1, 1000000)