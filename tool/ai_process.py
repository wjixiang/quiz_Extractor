import requests  

def chat_with_gpt(api_url, api_key, prompt):  
    headers = {  
        'Content-Type': 'application/json',  
        'Authorization': f'Bearer {api_key}'  
    }  
    
    data = {  
        'model': 'gpt-4o-mini',  # 或者使用其他可用的模型  
        'messages': [  
            {'role': 'system', 'content': 'You are a format converter.'},  
            {'role': 'user', 'content': prompt}  
        ]  
    }  
    
    response = requests.post(api_url, headers=headers, json=data)  
    
    if response.status_code != 200:  
        raise Exception(f"Error: {response.status_code}, {response.text}")  
    
    return response.json()['choices'][0]['message']['content']  

# 使用示例  
api_url = 'https://www.gptapi.us/v1/chat/completions'  # 自定义API地址  
api_key = 'sk-DODVVPSJqKAwrJ5kF3EcCd9005354f6bAd6eA658A145B5C7'  # 替换为您的API密钥  


def ai(input_content):
    try:  
        response = chat_with_gpt(api_url, api_key, input_content)  
        print(response)  
        return response
    except Exception as e:  
        print(e)  

def a1_test_convert():
    test_row = ""
    answer_row = ""
    with open('./tool/test_row.md','r') as f:
        test_row = f.read()

    print(test_row)
    user_input = f"不提供解释，修正格式，一个选项占单独一行，同一道题目内部不要有空行，题目与题目间由2个换行符分隔:\n{test_row}"

    test = ai(user_input)

    with open("./tool/test.md",'w') as f:
        f.write(test)


def answer_convert():
    test_row = ""
    answer_row = ""
    with open('./tool/answer_row.md','r') as f:
        answer_row = f.read()

    print(answer_row)

    answer = ai(f"不提供解释，修正下列列表的格式，提取转为有序列表，不改动原先的内容，一行一个:\n{answer_row}")

    print(answer)
    with open("./tool/answer.md",'w') as f:
        f.write(answer)

# answer_convert()