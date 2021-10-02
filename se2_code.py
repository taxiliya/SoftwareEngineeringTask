import sys

def changefiles():
    filecontent = []
    filepath = sys.argv[1]
    with open(filepath, "r") as f:  # 打开文件
        data = f.readlines()    # 读取文件中每行数据
        for fline in data:    # 循环读取每行数据
            filecontent.append(fline.split())  # 将每行数据分割后再存入list中
    with open("yq_out.txt", "w") as f:  # 写入文件
        i = False   #设置i的作用是让省份与省份之间打印出空行，但是第一个省份去不要有空行
        province = ""
        default_string = "待明确地区"
        for fline in filecontent:
            if fline[0] != province:    # 如果读到的省份数据和之前记录的数据不同，则
                if i:
                    f.write('\n')    # 打印个空行
                i = True
                f.write(fline[0]+'\n')    # 打印新省份
                province = fline[0]    # 更新省份
                f.write(fline[1]+'\t'+fline[2]+'\n')
            elif fline[1] != default_string:    # 省份相同，则只打印后边的城市与数字，加个判断是为了去除“待明确地区”
                f.write(fline[1]+'\t'+fline[2]+'\n')
        f.write('\n')    # 样例末尾有个空行


if __name__ == '__main__':
    changefiles()