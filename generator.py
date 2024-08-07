# 密码生成器

# 导入随机库
import random, string

def generate(a):
    # 获取密码长度
    len_all = int(a)

    # 确定密码中数字位数
    len_num = random.randint(1,len_all-1)

    # 确定密码中字母位数
    len_letter = len_all - len_num

    # 乱序前结果
    re = ''

    # 生成随机数字（位数按之前的确定）line10
    for i in range(len_num):
        a = str(random.randint(0,9))
        re = re + a

    # 生成随机字母
    for j in range(len_letter):
        b = str(random.choice(string.ascii_letters))
        re = re + b

    # 将re转换为列表li
    li = []
    for k in range(0,len(re)):
        li.append(re[k])

    # 打乱列表li
    random.shuffle(li)

    # 将li转换为字符串
    result = ''
    for k in range(0,len(li)):
        result = result + str(li[k])

    return result


