import re

org = input("OrgName: ")
user = input("userID: ")

text = '''
#insert string here. This can be any string containing MessageIds in the standard <message.id.format>
'''

#find every string matching the regex pattern for a standard MessageId and add it to "matches"
matches = re.findall(r'(<[^>]+>)', text)
#if "matches" is not empty
if len(matches) != 0:
    #dedupe
    dedupedMatches = set(matches)
    print(f'Found {len(dedupedMatches)} unique MessageIds.')
    #open file to write formatted MessageIds
    with open(f'./inFile_{org}_{user}.txt',"w+") as f:
        print(f"Writing MessageIds to 'inFile_{org}_{user}.txt' in the current directory...")
        #writing to file
        for i in dedupedMatches:
            f.write(f"{i}\n")
#otherwise
else:
    print("Error: no MessageIds found in provided text.")
