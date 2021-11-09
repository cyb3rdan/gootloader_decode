import re
import js2py
import sys

re_pattern = r'(?:http(?:s?)://)?(?:[\w]+\.)+[a-z]+(?::\d{1,5})?'

jsfile = open(sys.argv[1],'r').readlines()
for lines in jsfile:
    line = lines.strip()
    if len(line) > 1000:
        cleaned_js = ";".join(line.split(";")[1:-3:])
        obfuscated_js = (js2py.eval_js(cleaned_js))
        interesting = (obfuscated_js[::-1][::4])
        domains = re.findall(re_pattern,interesting)
        for domain in domains:
            print ("[*] Potential domain: " + domain)

# Transformations
# print ("START")
# print (interesting[::-1][::2])
# print ("----")
# print (interesting[::-1][1::2])
# print ("----")
# print (interesting[1::2])
# print ("----")
# print (interesting[::-1][::4])
# print ("----")
# print (interesting[::-1][1::4])
# print ("----")
# print (interesting[::-1])
# print ("----")
# print (interesting[::2][::-2])
# print ("----")
# print (interesting[1::2][::2])
# print ("----")
# print (interesting[1::4][::-1])
# print ("----")
# print (interesting[::4][::-1])
# print ("----")
# print (interesting[1::2])
# print ("----")
# print (interesting[::2])
# print ("----")
# print (interesting[1::4])
# print ("----")
# print (interesting[::4])
# print ("----")
# print (interesting[1::])
# print ("END")
