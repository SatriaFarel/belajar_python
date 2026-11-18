# Docs Module JSON Link https://docs.python.org/3/library/json.html
import json

siswa = {
    "nama": "Bagus",
    "kelas": 10
}

text_json = json.dumps(siswa)
print(text_json)
json_string = '{"nama":"Bagus", "kelas": 10}'
data_json = json.loads(json_string)
print(f"{data_json.get("nama")}, {data_json.get("kelas")}")

print(52%3)