import json
import random
catfacts = [
 "The longest living cat on record according to the Guinness Book belongs to the late Creme Puff of Austin, Texas who lived to the ripe old age of 38 years and 3 days!",
 "Cats have \"nine lives\" thanks to a flexible spine and powerful leg and back muscles",
 "A cat's nose pad is ridged with a unique pattern, just like the fingerprint of a human.",
 "Florence Nightingale owned more than 60 cats in her lifetime.",
 "A cat sees about 6 times better than a human at night, and needs 1/6 the amount of of light that a human does - it has a layer of extra reflecting cells which absorb light."
]

def handler(event, context):
    outputdata = {}
    try:
        catFactsLength = len(catfacts)
        n = random.randint(0,(catFactsLength-1))
        print(catfacts[n])
        outputbody = {
            "fact": catfacts[n],
            "length": len(catfacts[n]   )     
        }
        outputdata["status"] = "Success"
        outputdata["message"] = outputbody
    except Exception as e:
        outputdata["status"] = "Failure"
        outputdata["message"] = str(e)
        
    if outputdata["status"] == "Success":
        return {"statusCode": 200,"headers": {"Access-Control-Allow-Headers": "Content-Type","Access-Control-Allow-Origin": "*","Access-Control-Allow-Methods": "GET,POST,PUT,DELETE"},"body": json.dumps(outputdata["message"])}
    else:
        return {"statusCode": 400,"headers": {"Access-Control-Allow-Headers": "Content-Type","Access-Control-Allow-Origin": "*","Access-Control-Allow-Methods": "GET,POST,PUT,DELETE"},"body": json.dumps(outputdata["message"])}


if __name__=="__main__":
    event = None
    context = None
    result = handler(event,context)
    print(result)

