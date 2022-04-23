
import json




diagnose_class = [
    {'name':'内科', 'cl':['分泌内科', '心血管内科', '心血管内科','消化内科', '呼吸与危重症医学科', '肾内科','血液内科','神经内科','过敏反应科']},
    {'name':'外科', 'cl':['神经外科', '胃肠外科', '胸外科', '泌尿外科', '关节外科', '手足外科']},
    {'name':'妇产科', 'cl': ['妇科门诊', '产科门诊']},
    {'name':'儿科', 'cl': ['小儿内科', '小儿外科', '儿童保健科', '小儿推拿门诊']},
    {'name':'中医科', 'cl': ['中医内科门诊']},
    {'name':'五官科', 'cl': ['眼科', '耳鼻咽喉科']}
    ]



str = json.dumps(diagnose_class, ensure_ascii=False)
print(json.dumps(diagnose_class, ensure_ascii=False))

with open("./diagnose.json", 'w', encoding='utf-8') as wp:
    wp.write(str)