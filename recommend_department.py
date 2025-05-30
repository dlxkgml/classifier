import json

def recommend_department(what_tag, where_tag, how_tag, department_tags_path="./department_tags.json"):
    with open(department_tags_path, "r", encoding="utf-8") as f:
        departments = json.load(f)

    best_score = -1
    best_department = None

    for dept in departments:
        score = 0
        if what_tag in dept["what"]:
            score += 2
        if where_tag in dept["where"]:
            score += 1
        if how_tag in dept["how"]:
            score += 0.5

        if score > best_score:
            best_score = score
            best_department = dept["과"]

    if best_department:
        return best_department
    else:
        return "해당 부서 없음"
