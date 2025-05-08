dictionary = {
    "first": "kichuna",
    "second": "abar ki",
    "third": "kichuina chill"
}
dictionary["third"] = "bolbo nah"

print(dictionary)


#using the update() method:

dictionary.update({"third": "abar jiggasha korle mair dibo"})
dictionary.update({"fourth": "asholei kichu hoy nai"})  #new key with value

print(dictionary)

print(dictionary.values())