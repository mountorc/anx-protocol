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
    all_hobbies = ['阅读', '运动', '音乐', '旅行', '美食', '电影', '游戏', '艺术']
    num_hobbies = random.randint(1, 5)
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

# 生成随机地址
def generate_address():
    cities = ['北京', '上海', '广州', '深圳', '杭州', '成都', '武汉', '西安']
    districts = ['朝阳区', '海淀区', '浦东新区', '天河区', '南山区', '西湖区', '锦江区', '武昌区']
    streets = ['建国路', '中关村大街', '世纪大道', '天河路', '科技园路', '西湖大道', '春熙路', '武珞路']
    return f"{random.choice(cities)}{random.choice(districts)}{random.choice(streets)}{random.randint(1, 100)}号"

# 生成随机电话号码
def generate_phone():
    prefixes = ['130', '131', '132', '133', '134', '135', '136', '137', '138', '139', '150', '151', '152', '153', '155', '156', '157', '158', '159', '170', '171', '172', '173', '175', '176', '177', '178', '180', '181', '182', '183', '184', '185', '186', '187', '188', '189']
    suffix = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return f"{random.choice(prefixes)}{suffix}"

# 生成随机公司名称
def generate_company():
    prefixes = ['科技', '网络', '信息', '数字', '智能', '创新', '未来', '全球']
    suffixes = ['有限公司', '科技公司', '网络公司', '信息公司', '数字公司']
    return f"{random.choice(prefixes)}{random.randint(1000, 9999)}{random.choice(suffixes)}"

# 生成随机职业
def generate_occupation():
    occupations = ['工程师', '设计师', '教师', '医生', '律师', '会计', '销售', '市场', '产品经理', '运营']
    return random.choice(occupations)

# 生成随机教育程度
def generate_education():
    educations = ['初中', '高中', '大专', '本科', '硕士', '博士']
    return random.choice(educations)

# 生成随机收入范围
def generate_income():
    ranges = ['3000以下', '3000-5000', '5000-8000', '8000-12000', '12000-20000', '20000以上']
    return random.choice(ranges)

# 生成随机表单类型
def generate_form_type():
    form_types = [
        '用户注册',
        '个人信息',
        '公司信息',
        '产品反馈',
        '活动报名',
        '问卷调查',
        '求职申请',
        '会员信息'
    ]
    return random.choice(form_types)

# 生成随机表单组件
def generate_variant_components(form_type):
    components = []
    component_id = f"card_{random.randint(1000000000000, 9999999999999)}_{random.randint(1000, 9999)}"
    
    # 基础组件
    components.append(f'<x input {component_id}_1> username: 请输入用户名 </x>')
    components.append(f'<x input {component_id}_2> email: 请输入邮箱 </x>')
    
    # 根据表单类型添加不同组件
    if form_type == '用户注册':
        components.append(f'<x date {component_id}_3> birthday: 请选择出生日期 </x>')
        components.append(f'<x input {component_id}_4> age: 请输入年龄 </x>')
        components.append(f'<x options {component_id}_5> gender: 男 女 其他 </x>')
        components.append(f'<x checkbox {component_id}_6> hobbies: 阅读 运动 音乐 旅行 </x>')
        components.append(f'<x textarea {component_id}_7> description: 请输入个人简介 </x>')
    elif form_type == '个人信息':
        components.append(f'<x input {component_id}_3> name: 请输入姓名 </x>')
        components.append(f'<x date {component_id}_4> birthday: 请选择出生日期 </x>')
        components.append(f'<x options {component_id}_5> gender: 男 女 其他 </x>')
        components.append(f'<x input {component_id}_6> phone: 请输入电话号码 </x>')
        components.append(f'<x textarea {component_id}_7> address: 请输入地址 </x>')
        components.append(f'<x options {component_id}_8> education: 初中 高中 大专 本科 硕士 博士 </x>')
    elif form_type == '公司信息':
        components.append(f'<x input {component_id}_3> company: 请输入公司名称 </x>')
        components.append(f'<x input {component_id}_4> contact: 请输入联系人 </x>')
        components.append(f'<x input {component_id}_5> phone: 请输入联系电话 </x>')
        components.append(f'<x textarea {component_id}_6> address: 请输入公司地址 </x>')
        components.append(f'<x input {component_id}_7> industry: 请输入所属行业 </x>')
    elif form_type == '产品反馈':
        components.append(f'<x input {component_id}_3> product: 请输入产品名称 </x>')
        components.append(f'<x options {component_id}_4> rating: 1星 2星 3星 4星 5星 </x>')
        components.append(f'<x checkbox {component_id}_5> issues: 功能问题 性能问题 界面问题 其他问题 </x>')
        components.append(f'<x textarea {component_id}_6> feedback: 请输入详细反馈 </x>')
    elif form_type == '活动报名':
        components.append(f'<x input {component_id}_3> name: 请输入姓名 </x>')
        components.append(f'<x input {component_id}_4> phone: 请输入电话号码 </x>')
        components.append(f'<x input {component_id}_5> company: 请输入公司名称 </x>')
        components.append(f'<x options {component_id}_6> position: 经理 工程师 设计师 其他 </x>')
        components.append(f'<x textarea {component_id}_7> notes: 备注信息 </x>')
    elif form_type == '问卷调查':
        components.append(f'<x input {component_id}_3> age: 请输入年龄 </x>')
        components.append(f'<x options {component_id}_4> gender: 男 女 其他 </x>')
        components.append(f'<x options {component_id}_5> education: 初中 高中 大专 本科 硕士 博士 </x>')
        components.append(f'<x options {component_id}_6> income: 3000以下 3000-5000 5000-8000 8000-12000 12000-20000 20000以上 </x>')
        components.append(f'<x checkbox {component_id}_7> interests: 科技 艺术 运动 音乐 旅行 美食 </x>')
    elif form_type == '求职申请':
        components.append(f'<x input {component_id}_3> name: 请输入姓名 </x>')
        components.append(f'<x input {component_id}_4> phone: 请输入电话号码 </x>')
        components.append(f'<x options {component_id}_5> education: 初中 高中 大专 本科 硕士 博士 </x>')
        components.append(f'<x input {component_id}_6> occupation: 请输入应聘职位 </x>')
        components.append(f'<x textarea {component_id}_7> experience: 请输入工作经验 </x>')
    elif form_type == '会员信息':
        components.append(f'<x input {component_id}_3> name: 请输入姓名 </x>')
        components.append(f'<x input {component_id}_4> phone: 请输入电话号码 </x>')
        components.append(f'<x date {component_id}_5> join_date: 请选择加入日期 </x>')
        components.append(f'<x options {component_id}_6> membership: 普通会员 银卡会员 金卡会员 钻石会员 </x>')
        components.append(f'<x textarea {component_id}_7> preferences: 请输入偏好设置 </x>')
    
    # 添加提交按钮
    components.append(f'<x button {component_id}_submit> 提交 </x>')
    
    return components, component_id

# 生成训练数据
def generate_variant_training_data(num_examples=200):
    training_data = []
    
    for i in range(num_examples):
        # 生成表单类型
        form_type = generate_form_type()
        
        # 生成表单组件
        components, form_id = generate_variant_components(form_type)
        form_markup = '\n'.join([f'  {component}' for component in components])
        system_content = f"ANX markup表单：<x form {form_id}> ## {form_type}表单\n{form_markup}\n</x>"
        
        # 生成用户输入
        username = generate_username()
        email = generate_email()
        
        # 生成表单数据
        form_data = {
            f'{form_id}_1': username,
            f'{form_id}_2': email
        }
        
        # 根据表单类型添加不同字段
        if form_type == '用户注册':
            form_data[f'{form_id}_3'] = generate_birthday()
            form_data[f'{form_id}_4'] = generate_age()
            form_data[f'{form_id}_5'] = generate_gender()
            form_data[f'{form_id}_6'] = generate_hobbies()
            form_data[f'{form_id}_7'] = generate_description()
        elif form_type == '个人信息':
            form_data[f'{form_id}_3'] = f"{random.choice(['张', '李', '王', '刘', '陈'])}{random.choice(['三', '四', '五', '六', '七', '八'])}"
            form_data[f'{form_id}_4'] = generate_birthday()
            form_data[f'{form_id}_5'] = generate_gender()
            form_data[f'{form_id}_6'] = generate_phone()
            form_data[f'{form_id}_7'] = generate_address()
            form_data[f'{form_id}_8'] = generate_education()
        elif form_type == '公司信息':
            form_data[f'{form_id}_3'] = generate_company()
            form_data[f'{form_id}_4'] = f"{random.choice(['张', '李', '王', '刘', '陈'])}{random.choice(['经理', '总', '先生', '女士'])}"
            form_data[f'{form_id}_5'] = generate_phone()
            form_data[f'{form_id}_6'] = generate_address()
            form_data[f'{form_id}_7'] = random.choice(['科技', '金融', '教育', '医疗', '零售'])
        elif form_type == '产品反馈':
            form_data[f'{form_id}_3'] = random.choice(['产品A', '产品B', '产品C', '产品D', '产品E'])
            form_data[f'{form_id}_4'] = f"{random.randint(1, 5)}星"
            form_data[f'{form_id}_5'] = random.sample(['功能问题', '性能问题', '界面问题', '其他问题'], random.randint(1, 4))
            form_data[f'{form_id}_6'] = generate_description()
        elif form_type == '活动报名':
            form_data[f'{form_id}_3'] = f"{random.choice(['张', '李', '王', '刘', '陈'])}{random.choice(['三', '四', '五', '六', '七', '八'])}"
            form_data[f'{form_id}_4'] = generate_phone()
            form_data[f'{form_id}_5'] = generate_company()
            form_data[f'{form_id}_6'] = random.choice(['经理', '工程师', '设计师', '其他'])
            form_data[f'{form_id}_7'] = '无'
        elif form_type == '问卷调查':
            form_data[f'{form_id}_3'] = generate_age()
            form_data[f'{form_id}_4'] = generate_gender()
            form_data[f'{form_id}_5'] = generate_education()
            form_data[f'{form_id}_6'] = generate_income()
            form_data[f'{form_id}_7'] = random.sample(['科技', '艺术', '运动', '音乐', '旅行', '美食'], random.randint(1, 6))
        elif form_type == '求职申请':
            form_data[f'{form_id}_3'] = f"{random.choice(['张', '李', '王', '刘', '陈'])}{random.choice(['三', '四', '五', '六', '七', '八'])}"
            form_data[f'{form_id}_4'] = generate_phone()
            form_data[f'{form_id}_5'] = generate_education()
            form_data[f'{form_id}_6'] = generate_occupation()
            form_data[f'{form_id}_7'] = f"{random.randint(1, 10)}年相关工作经验"
        elif form_type == '会员信息':
            form_data[f'{form_id}_3'] = f"{random.choice(['张', '李', '王', '刘', '陈'])}{random.choice(['三', '四', '五', '六', '七', '八'])}"
            form_data[f'{form_id}_4'] = generate_phone()
            form_data[f'{form_id}_5'] = datetime.date.today().strftime('%Y-%m-%d')
            form_data[f'{form_id}_6'] = random.choice(['普通会员', '银卡会员', '金卡会员', '钻石会员'])
            form_data[f'{form_id}_7'] = '无特殊偏好'
        
        # 构建set_form命令
        import json as json_module
        form_data_str = json_module.dumps(form_data, ensure_ascii=False)
        set_form_command = f"anx {form_id} set_form '{form_data_str}'"
        
        # 构建tap命令
        tap_command = f"anx {form_id}_submit tap"
        
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

# 追加训练数据
def append_training_data(data, output_file):
    with open(output_file, 'a', encoding='utf-8') as f:
        for example in data:
            json_str = json.dumps(example, ensure_ascii=False)
            f.write(json_str + '\n')
    print(f"训练数据已追加到 {output_file}，共追加 {len(data)} 条")

# 主函数
if __name__ == "__main__":
    output_file = os.path.join(os.path.dirname(__file__), "anx-system-markup-training-messages.jsonl")
    training_data = generate_variant_training_data(200)
    append_training_data(training_data, output_file)
