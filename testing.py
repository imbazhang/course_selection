L = [['课程序号', '课程名称', '课程类别', '学分', '教师', '校区', '已选/上限', '分组（已选/上限）', '课程安排', '意愿值', ' 操作'],
     ['ARTS0031112017.01', '合唱', '艺术体育系列', '2', '谭雅如', '闵行', '42/30', '[1-13]', '星期三9-11节', '闵音乐 楼267', '选课'],
     ['ARTS0031112033.01', '中外美术经典赏析', '艺术体育系列', '2', '熊瑛', '闵行', '34/30', '[1-12]', '星期一9-11节', '闵一教243', '选课'],
     ['ARTS0031112037.01', '美术与视觉审美（中国）', '艺术体育系列', '2', '郑文,顾平,国玲,顾琴,熊瑛', '闵行', '34/30', '[11-12]', '星期三9-11节', '闵一教124'],
        ['[5-7]', '星期三9-11节', '闵一教124'], ['[8-10]', '星期三9-11节', '闵一教124'], ['[1-3]', '星期三9-11节', '闵一教124'], ['[4]', '星期三9-11节', '闵一教124', '选课'],
     ['ARTS0031112038.01', '美术与视觉审美（西方）', '艺术体育系列', '2', '贾蕊,吕旗彰,邱敏,陈东杰,顾欣', '闵行', '35/30', '[1-2]', '星期一9-11节', '闵一教124'],
        ['[3-5]', '星期一9-11节', '闵一教124'],
        ['[6-7]', '星期一9-11节', '闵一教124'],
        ['[8-9]', '星期一9-11节', '闵一教124'],
        ['[10-12]', '星期一9-11节', '闵一教124', '选课'],
     ['ARTS0031112039.01', '书画鉴定', '艺 术体育系列', '2', '胡光华', '闵行', '45/40', '[2-13]', '星期三9-11节', '闵二教221', '选课'],
     ['ARTS0031112040.01', '古玩鉴赏', '艺术体育系列', '2', '何志国', '闵行', '49/40', '[1-12]', '星期一9-11节', '闵二教225', '选课'],
     ['ARTS0031112041.01', '楷书临摹与创作', '艺术体育系列', '2', '崔树强', '闵行', '47/30', '[1-12]', '星期一9-11节', '闵二教323', '选课'],
     ['BIOL0031112013.01', '人体科学', '通识精品课程', '2', '袁崇刚', '闵行', '83/50', '[1-18]', '星期二9-10节', '闵三教220', '选课'],
     ['BIOL0031112015.01', '食品安全与科学理性', '通识精品课程', '2', '杜震宇', '闵行', '94/75', '[1-12]', '星期一9-11节', '闵三教329', '选课'],
     ['BIOL0031112018.01', '城市化过程与生物多样性', '自然科学系列', '1', '陈珉', '闵行', '31/30', '[2-7]', '星期三9-11节', '闵三教206', '选课'],
     ['BIOL0031112022.01', '生态思辨', '自然科学系列', '2', '邹春静', '闵行', '30/60', '[1-18]', '星期一9-10节', '闵三教227', '选课'],
     ['BIOL0031112025.01', '基因编辑简史与实践DIY', '自然科学系列', '2', '李东亮', '闵行', '33/30', '[1-12]', '星期二9-11节', '闵三教206', '选课'],
     ['BUSI0031172001.01', '创新思维与执行力', '创新创业课', '2', '王海英', '闵行', '55/60', '[1-10]', '星期一5-8节', '闵一教335', '选课'],
     ['CHEM0031112009.01', '药物的发明与发现', '自然科学系列', '2', '罗宇', '闵行', '58/55', '[1-13]', '星期一9-11节', '闵四教203', '选课'],
     ['CHIN0031112012.01', '红楼梦研究', '人文科学系列', '2', '王冉冉', '闵行', '61/50', '[1-12]', '星期一9-11节', '闵一教323', '选课'],
     ['CHIN0031112035.01', '绘本与中西图像文化', '人文科学系列', '2', '陈静', '闵行', '32/30', '[1-12]', '星期三9-11节', '闵一教320', '选课'],
     ['CHIN0031112042.01', '经典与中国传统文化', '通识精品课程', '2', '吕志峰', '闵行', '64/50', '[1-12]', '星期一9-11节', '闵一教319', '选课'],
     ['CHIN0031112045.01', '昆曲清唱与研究', '人文科学系列', '2', '李舜华', '闵行', '26/25', '[1-12]', '星期一9-11节', '文史哲楼4255', '选课'],
     ['CHIN0031112049.01', '视听文化与现代文学', '人文科学系列', '2', '张春田', '闵行', '25/25', '[1-12]', '星期三9-11节', '文史哲楼4255', '选课'],
     ['CHIN0031112050.01', '诸子学研究 前沿', '人文科学系列', '2', '方勇', '闵行', '37/30', '[1-12]', '星期三9-11节', '闵一教319', '选课']]
i = 0
while i < len(L):
    if len(L[i]) != 11:
        if len(L[i]) is 3:
            L[i-1][7] = L[i-1][8] + L[i][0]
            L[i-1][8] = L[i-1][9] + L[i][2]
            L[i-1][9] = L[i][3] + L[i-1][10]
            del L[i]
        elif len(L[i]) is 4:
            L[i - 1][7] = L[i - 1][8] + L[i][0]
            L[i - 1][8] = L[i - 1][9] + L[i][2]
            L[i - 1][9] = L[i][3] + L[i - 1][10]
            L[i - 1].append(L[i][-1])
            del L[i]
    else:
        i += 1



