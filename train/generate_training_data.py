import json
import random
import datetime
import os

# 生成随机用户名
def generate_username():
    prefixes = ['user', 'test', 'demo', 'guest', 'admin']
    suffix = random.randint(1000, 9999)
    return f"{random.choice(prefixes)}{suffix}"

# 生成随机邮箱
def generate_email():
    domains = ['example.com', 'test.com', 'demo.com', 'mail.com']
    username = generate_username()
    return f"{username}@{random.choice(domains)}"

# 生成随机出生日期
def generate_birthday():
    start_date = datetime.date(1980, 1, 1)
    end_date = datetime.date(2005, 12, 31)
    days_between = (end_date - start_date).days
    random_days = random.randint(0, days_between)
    birthday = start_date + datetime.timedelta(days=random_days)
    return birthday.strftime('%Y-%m-%d')

# 生成随机年龄
def generate_age():
    return random.randint(18, 40)

# 生成随机性别
def generate_gender():
    return random.choice(['男', '女', '其他'])

# 生成随机爱好
def generate_hobbies():
    all_hobbies = ['阅读', '运动', '音乐', '旅行']
    num_hobbies = random.randint(1, 4)
    return random.sample(all_hobbies, num_hobbies)

# 生成随机个人简介
def generate_description():
    descriptions = [
        '喜欢阅读和旅行，热爱生活',
        '科技爱好者，喜欢探索新事物',
        '音乐发烧友，擅长多种乐器',
        '运动健将，喜欢各种户外活动',
        '安静内向，喜欢独处和思考',
        '开朗外向，喜欢结交新朋友',
        '美食爱好者，喜欢尝试各种美食',
        '电影迷，喜欢看各种类型的电影',
        '游戏玩家，喜欢玩各种电子游戏',
        '艺术爱好者，喜欢绘画和摄影'
    ]
    return random.choice(descriptions)

# 生成表单组件
def generate_form_components():
    components = []
    
    # 用户名输入框
    components.append('<x input card_1774672305364_7557> username: 请输入用户名 </x>')
    
    # 邮箱输入框
    components.append('<x input card_1774672305364_2819> email: 请输入邮箱 </x>')
    
    # 出生日期选择器
    components.append('<x date card_1774672305364_5872> birthday: 请选择出生日期 </x>')
    
    # 年龄输入框
    components.append('<x input card_1774672305364_4370> age: 请输入年龄 </x>')
    
    # 成年年数字本标签
    components.append('<x text card_1774672305364_4433> 成年年数: </x>')
    
    # 性别选择
    components.append('<x options card_1774672305364_5510> gender: 男 女 其他 </x>')
    
    # 爱好选择
    components.append('<x checkbox card_1774672305364_7560> hobbies: 阅读 运动 音乐 旅行 </x>')
    
    # 个人简介
    components.append('<x textarea card_1774672305364_5254> description: 请输入个人简介 </x>')
    
    # 提交按钮
    components.append('<x button card_1774672305364_4211> 提交 </x>')
    
    return components

# 生成训练数据
def generate_training_data(num_examples=200):
    training_data = []
    
    for i in range(num_examples):
        # 生成表单组件
        components = generate_form_components()
        form_markup = '\n'.join([f'  {component}' for component in components])
        system_content = f"ANX markup表单：<x form card_1774672305364_5722> ## 用户注册表单\n{form_markup}\n</x>"
        
        # 生成用户输入
        username = generate_username()
        email = generate_email()
        birthday = generate_birthday()
        age = generate_age()
        gender = generate_gender()
        hobbies = generate_hobbies()
        description = generate_description()
        
        # 生成CLI命令
        form_data = {
            'card_1774672305364_7557': username,
            'card_1774672305364_2819': email,
            'card_1774672305364_5872': birthday,
            'card_1774672305364_4370': age,
            'card_1774672305364_5510': gender,
            'card_1774672305364_7560': hobbies,
            'card_1774672305364_5254': description
        }
        
        # 构建set_form命令
        import json as json_module
        form_data_str = json_module.dumps(form_data, ensure_ascii=False)
        set_form_command = f"anx card_1774672305364_5722 set_form '{form_data_str}'"
        
        # 构建tap命令
        tap_command = "anx card_1774672305364_4211 tap"
        
        # 构建assistant响应
        assistant_content = f"1. `{set_form_command}`\n2. `{tap_command}`"
        
        # 构建训练数据
        training_example = {
            "messages": [
                {"role": "system", "content": system_content},
                {"role": "user", "content": "填一下表格"},
                {"role": "assistant", "content": assistant_content}
            ]
        }
        
        training_data.append(training_example)
    
    return training_data

# 保存训练数据
def save_training_data(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for example in data:
            json_str = json.dumps(example, ensure_ascii=False)
            f.write(json_str + '\n')
    print(f"训练数据已保存到 {output_file}，共 {len(data)} 条")

# 主函数
if __name__ == "__main__":
    output_file = os.path.join(os.path.dirname(__file__), "anx-system-markup-training-messages.jsonl")
    training_data = generate_training_data(200)
    save_training_data(training_data, output_file)
