import json

if __name__ == "__main__":
    dict0 = {
            "session_id": 1,
            "responses": "response_list"}

    name_emb = {'a': '1111', 'b': '2222', 'c': '3333', 'd': dict0}

    # xx = json.dumps(dict0, indent=4)
    # print(xx)
    # 🔥🔥 原来是让 dict 显示的更加漂亮, 对齐缩进 4 个空格
    yy = json.dumps(name_emb, indent=4)
    print(yy)