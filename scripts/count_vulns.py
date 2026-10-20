import json
import sys
from collections import Counter

data = json.load(open(sys.argv[1], encoding="utf-8"))
total, fixed = Counter(), Counter()

for res in data.get("Results", []):
    cls = res.get("Class", "?")  # os-pkgs - системные пакеты, lang-pkgs - библиотеки
    for v in res.get("Vulnerabilities") or []:
        if v["Severity"] in ("CRITICAL", "HIGH"):
            total[(cls, v["Severity"])] += 1
            if v.get("Status") == "fixed":
                fixed[(cls, v["Severity"])] += 1

print("класс / уровень : всего, из них fixed")
for key in sorted(total):
    print(f"{key[0]:10} {key[1]:9} : {total[key]:4} , fixed {fixed[key]}")
print("ВСЕГО CRITICAL+HIGH:", sum(total.values()), "| fixed:", sum(fixed.values()))
