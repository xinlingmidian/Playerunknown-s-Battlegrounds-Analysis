# -*- coding: gbk -*- 
#对得分大于等等于90的玩家的数据进行分析，数据集事先已经由com.yanghuabin.PlayerScore包下的代码进行了预处理，生成包含
#玩家与得分信息的part-r-00000（由Hadoop生成）和得分大于等于90分的玩家的详细信息（Context）
#玩家与得分信息已被上传到了数据库，参见db包及sql文件
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import copy
import sys #要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方法
reload(sys) 
sys.setdefaultencoding('gbk')

sns.set()
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False  
plt.style.use('ggplot') 


def is_win(rank):   #排名第一认为胜利
    label = 0
    if rank == 1:
        label = 1
    return label


if __name__ == '__main__':
    try:
        meta_data = pd.read_csv('C:\\Users\\***\\Desktop\\Context.csv', sep=',', header=0)#输入Context的文件路径
    except Exception as e:
        print('Error:', e)

    print('---------------------------')
 
    used_data = meta_data[['match_id','game_size','match_mode','party_size','team_id','team_placement','player_kills','player_name',
    'player_dbno','player_assists','player_dmg','player_dist_ride','player_dist_walk','player_survive_time']]
    
    sum_count = pd.value_counts(used_data['match_id']).count()
    sum_count = meta_data.iloc[:,2].size
    print(r'all %d' % sum_count)
    print('')
    

    #fig = plt.figure(figsize = (7,7))
    fig = plt.figure(figsize = (9,7))
    

    #计算排名占前10%的玩家人数
    ranks = used_data['team_placement']  
    map(float,ranks)
    team_size = used_data['game_size']
    map(float,team_size)
    totalcount = 0
    for i in range(len(ranks)):       #使用python计算比较慢，还是用Hadoop方便
        if float(float(ranks[i]) / float(team_size[i]))<0.1:
            totalcount = totalcount + 1
            print float(float(ranks[i]) / float(team_size[i]))
    print totalcount
    
    
    #print ranks
    
    #分别计算伤害大于等于100，击杀数大于1的玩家人数占比
    x = used_data[used_data['player_dmg']>=100]['player_dmg']
    #y = used_data[used_data['team_placement']==1]['team_placement']
    z = used_data[used_data['player_kills']>1]['player_kills']
    print(x.size)
    #print(y.size)
    print(z.size)
    print('%.4f' %(float(x.size) / float(sum_count)))
    #print('%.4f' %(float(y.size) / float(sum_count)))#改用上面的方式计算排名占比
    print('%.4f' %(float(z.size) / float(sum_count)))
    print("////////")



    #对高于90分的玩家的，画出伤害大于等于100的占比图
    high_damage = float(x.size) / float(sum_count)
    plt.title('伤害占比图',fontsize = 14)
    plt.grid(True,linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
    plt.pie([1-high_damage,high_damage],labels=['<300','>=300'],autopct='%f%%',colors = ['#1C7ECE','#FF4D5B'],startangle = 120)
    plt.shouw()


    #分析击杀人数和伤害量与获得胜利的关系分布,画出击杀人数和伤害量与获得胜利的关系分布图
    
    pro_unique_match_data = copy.deepcopy(used_data) #拷贝一份数据
    pro_unique_match_data['获胜'] = used_data['team_placement'].apply(is_win)
    g = sns.stripplot(data=pro_unique_match_data[['获胜', 'player_dmg', 'player_kills']], x='player_kills',y='player_dmg', hue='获胜')
    g.set(title='击杀人数和伤害量与获得胜利的关系分布', xlabel='击杀人数', ylabel='造成的伤害')
    plt.tight_layout()
    plt.savefig('./pic/factors_vs_win.png', dpi=300)
    plt.grid(True,linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
    try:
        plt.show()
    except Exception as e:
        print('Error',e)
    

    #分析得分前十的玩家的数据，由数据库中找出得分前十的玩家，玩家名单如下
    '''
    9un-281172381-   9un-666024225   366898408   ACGww   641465992   687465   151026695
    Aivol   AKAZAJI   57O-266-973qun
    '''
    
    def search_player(name):
        player_data = used_data[used_data['player_name'] == name][['player_dmg','player_kills','team_placement']]
    
        
        print float(player_data['player_dmg'].sum()) / float(player_data['player_dmg'].count())
        print float(player_data['player_kills'].sum()) / float(player_data['player_kills'].count())
        print float(player_data['team_placement'].sum()) / float(player_data['team_placement'].count())
       

        print ("---------------------------")

    s = ['9un-281172381-','9un-666024225','366898408','ACGww','641465992','687465','151026695','Aivol','AKAZAJI','57O-266-973qun']
    for pname in s:
        search_player(pname)
    
    
    

