import time,os,csv

filename = 'file\\student.sdata'
outfile = '排名.csv'

def main():
    
    while True:
        menu()
        choice = input('请选择您想要的功能(填数字)：')
        if choice == '1':
            add()
        elif choice == '2':
            search()
        elif choice == '3':
            delete()
        elif choice == '4':
            modify()
        elif choice == '5':
            rank()
        elif choice == '6':
            show()
        elif choice == '7':
            print('感谢您的使用，下次再见！')
            time.sleep(3)
            break
        else:
            print('您输入的有误，请重新输入')

def menu():
    print('欢迎使用学生成绩管理系统')
    time.sleep(1)
    print('''
    ==========  功能菜单  ==========
    1.录入学生成绩
    2.查找学生成绩
    3.删除学生成绩
    4.修改学生成绩
    5.进行排名
    6.显示所有学生成绩
    7.退出系统
    ================================
    ''')

def add():
    new = input('是否为新的考试录入成绩，以前的成绩会被清除(y/n):')
    if new == 'y':
        student_txt = open(filename,'w')
        student_txt.write('')
        student_txt.close()
        print('数据已经清除！')
    else:
        pass

    student_list = [] #保存多个学生数据
    default = True    #控制下方循环

    while default:
        id = input('请输入学生的考号：')
        name = input('请输入学生姓名：')
        try:
            Chinese = float(input('请输入学生的语文科目成绩：'))
            Math = float(input('请输入学生的数学科目成绩：'))
            English = float(input('请输入学生的英语科目成绩：'))
            History = float(input('请输入学生的历史科目成绩：'))
            Politics = float(input('请输入学生的政治科目成绩：'))
            Geography = float(input('请输入学生的地理科目成绩：'))
            Biology = float(input('请输入学生的生物科目成绩：'))
            Physics = float(input('请输入学生的物理科目成绩：'))
            Chemistry = float(input('请输入学生的化学科目成绩：'))
        except:
            print('输入无效，不是一个有效的数字！请重新输入')
            time.sleep(1)
            continue
        student = {'id':id,'name':name,'Chinese':Chinese,'Math':Math,'English':English,'History':History,'Politics':Politics,'Geography':Geography,'Biology':Biology,'Physics':Physics,'Chemistry':Chemistry}
        student_list.append(student)
        print('%s的成绩保存成功' % name)
        add_more = input('是否继续添加？(y/n):')
        if add_more == 'y':
            default = True
        else:
            default = False
       
    student_txt = open(filename,'a')
    for st in student_list:
        student_txt.write(str(st) + '\n')
    student_txt.close()
    #保存学生文件至系统
#录入学生成绩

def search():
    default = True
    student_new = []
    while default:
        id = ''
        name = ''
        mode = input('请输入查询方式，1.按考号查询 2.按姓名查询:')
        if mode == '1':
            id = input('请输入学生的考号:')
        elif mode == '2':
            name = input('请输入学生的姓名:')
        else:
            print('您输入输入有误，请重新输入')
            time.sleep(1)
            continue
        
        if os.path.exists(filename):
            with open(filename,'r') as file:
                student_list = file.readlines()
            for list in student_list:
                d = dict(eval(list))
                if id != '':
                    if d['id'] == id:
                        student_new.append(d)
                        
                if name != '':
                    if d['name'] == name:
                        student_new.append(d)

            dataPrint(student_new)       
            student_new.clear()
            time.sleep(3)
            search_more = input('是否继续查询？(y/n):')
            if search_more == 'y':
                default = True
            else:
                default = False
        else:
            print('数据文件不存在！')
            default = False
#查找学生成绩

def delete():
    default = True
    while default:
        student_id = input('请输入要删除的学生考号（误操作请按回车以返回）:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename,'r') as rfile:
                    student_id_old = rfile.readlines()
            else:
                student_id_old = []
            is_delete = False

            if student_id_old:
                with open(filename,'w') as wfile:
                    d = {}
                    for st in student_id_old:
                        d = dict(eval(st))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            is_delete = True
                    if is_delete:
                        print('考号为%s的学生已经被删除' % student_id)
                    else:
                        print('未找到考号为%s的学生' % student_id)
            else:
                print('为查询到该学生信息！')
                time.sleep(3)
                continue
            show()
            delete_more = input('是否继续删除(y/n):')
            if delete_more == 'y':
                default = True
            else:
                default = False
#删除学生信息

def modify():
    show()
    student_id = input('请输入要修改的学生考号:')
    if os.path.exists(filename):
        with open(filename,'r') as rfile:
            student_list_old = rfile.readlines()
    else:
        print('数据文件不存在！')
        time.sleep(3)
        return
    with open(filename,'w') as wfile:
        d = {}
        for st in student_list_old:
            d = dict(eval(st))
            if d['id'] == student_id:
                while True:
                    try:
                        d['name'] = input('请输入学生姓名：')
                        d['Chinese'] = float(input('请输入学生的语文科目成绩：'))
                        d['Math'] = float(input('请输入学生的数学科目成绩：'))
                        d['English'] = float(input('请输入学生的英语科目成绩：'))
                        d['History'] = float(input('请输入学生的历史科目成绩：'))
                        d['Politics'] = float(input('请输入学生的政治科目成绩：'))
                        d['Geography'] = float(input('请输入学生的地理科目成绩：'))
                        d['Biology'] = float(input('请输入学生的生物科目成绩：'))
                        d['Physics'] = float(input('请输入学生的物理科目成绩：'))
                        d['Chemistry'] = float(input('请输入学生的化学科目成绩：'))
                    except:
                        print('输入无效，不是一个有效的数字！请重新输入')
                        time.sleep(1)
                        continue
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功！')
                time.sleep(2)
            else:
                wfile.write(str(d) + '\n')
    more_modify = input('是否继续修改(y/n):')
    if more_modify == 'y':
        modify()
    else:
        pass
#修改学生成绩

def rank():
    student_new = []
    if os.path.exists(filename):
        with open(filename,'r') as file:
            student_list = file.readlines()
        for list in student_list:
            student_new.append(eval(list))

        asc = True
        mode = input('请选择排名依据(01:语文排名；02：数学排名；03：英语排名；04：历史；05：政治；06：地理；07：生物；08：物理；09：化学；10：三科排名；11：全科排名):')
        if mode == '01':
            student_new.sort(key = lambda x:float(x['Chinese']),reverse=asc)
            mode_chinese = '语文'
        elif mode == '02':
            student_new.sort(key= lambda x:float(x['Math']),reverse=asc)
            mode_chinese = '数学'
        elif mode == '03':
            student_new.sort(key= lambda x:float(x['English']),reverse=asc)
            mode_chinese = '英语'
        elif mode == '04':
            student_new.sort(key= lambda x:float(x['History']),reverse=asc)
            mode_chinese = '历史'
        elif mode == '05':
            student_new.sort(key= lambda x:float(x['Politics']),reverse=asc)
            mode_chinese = '政治'
        elif mode == '06':
            student_new.sort(key= lambda x:float(x['Geography']),reverse=asc)
            mode_chinese = '地理'
        elif mode == '07':
            student_new.sort(key= lambda x:float(x['Biology']),reverse=asc)
            mode_chinese = '生物'
        elif mode == '08':
            student_new.sort(key= lambda x:float(x['Physics']),reverse=asc)
            mode_chinese = '物理'
        elif mode == '09':
            student_new.sort(key= lambda x:float(x['Chemistry']),reverse=asc)
            mode_chinese = '化学'
        elif mode == '10':
            student_new.sort(key= lambda x:float(x['Chinese']) + float(x['Math']) + float(x['English']),reverse=asc)
            mode_chinese = '三科'
        else:
            student_new.sort(key= lambda x:float(x['Chinese']) + float(x['Math']) + float(x['English']) + float(x['History']) + float(x['Politics']) + float(x['Geography']) + float(x['Biology']) + float(x['Physics']) + float(x['Chemistry']),reverse=asc)
            mode_chinese = '全科'

        if student_new:
            dataPrint(student_new)
            out = input('是否输出为csv格式(y/n):')
            n = 0
            if out == 'y':
                with open(outfile,'w',newline='') as oflie:
                    writer = csv.writer(oflie)
                    writer.writerow(['排名','考号','姓名','语文成绩','数学成绩','英语成绩','历史成绩','政治成绩','地理成绩','生物成绩','物理成绩','化学成绩','三科成绩','全科成绩'])
                    for info in student_new:
                        n = n + 1
                        student_print_list = [str(n) , info.get('id') , info.get('name') , str(info.get('Chinese')) , str(info.get('Math')) , str(info.get('English')) , str(info.get('History')) , str(info.get('Politics')) , str(info.get('Geography')) , str(info.get('Biology')) , str(info.get('Physics')) , str(info.get('Chemistry')) , str(float(info.get('Chinese')) + float(info.get('Math')) + float(info.get('English'))) , str(float(info.get('Chinese')) + float(info.get('Math')) + float(info.get('English')) + float(info.get('History')) + float(info.get('Politics')) + float(info.get('Geography')) + float(info.get('Biology')) + float(info.get('Physics')) + float(info.get('Chemistry')))]
                        writer.writerow(student_print_list)
                    writer.writerow(['按',mode_chinese,'成绩排名','','共',total(),'人参与'])
                    print('输出成功！')
                    time.sleep(3)                   
            else:
                pass

    else:
        print('数据文件不存在！')
#进行排名

def show():
    student_new = []
    if os.path.exists(filename):
        with open(filename,'r') as file:
            student_list = file.readlines()
        for list in student_list:
            student_new.append(eval(list))
        if student_new:
            dataPrint(student_new)
#显示所有学生信息

def dataPrint(student_new):
    print('考号\t姓名\t语文\t数学\t英语\t历史\t政治\t地理\t生物\t物理\t化学\t三科总成绩\t全科成绩')
    for info in student_new:
        print(info.get('id') + '\t'+
        info.get('name') + '\t'+
        str(info.get('Chinese')) + '\t'+
        str(info.get('Math')) + '\t'+
        str(info.get('English')) + '\t'+
        str(info.get('History')) + '\t'+
        str(info.get('Politics')) + '\t'+
        str(info.get('Geography')) + '\t'+
        str(info.get('Biology')) + '\t'+
        str(info.get('Physics')) + '\t' +
        str(info.get('Chemistry')) + '\t' +
        str(float(info.get('Chinese')) + float(info.get('Math')) + float(info.get('English'))) + '\t' + '\t' +
        str(float(info.get('Chinese')) + float(info.get('Math')) + float(info.get('English')) + float(info.get('History')) + float(info.get('Politics')) + float(info.get('Geography')) + float(info.get('Biology')) + float(info.get('Physics')) + float(info.get('Chemistry'))))
#打印成绩

def total():
    if os.path.exists(filename):
        with open(filename,'r') as file:
            student_list = file.readlines()
            if student_list:
                return len(student_list)
            else:
                return '没有'
    else:
        print('未找到数据文件！')
#输出学生数量

main()
