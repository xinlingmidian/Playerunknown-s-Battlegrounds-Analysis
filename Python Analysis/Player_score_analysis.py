# -*- coding: gbk -*- 
#�Ե÷ִ��ڵȵ���90����ҵ����ݽ��з��������ݼ������Ѿ���com.yanghuabin.PlayerScore���µĴ��������Ԥ�������ɰ���
#�����÷���Ϣ��part-r-00000����Hadoop���ɣ��͵÷ִ��ڵ���90�ֵ���ҵ���ϸ��Ϣ��Context��
#�����÷���Ϣ�ѱ��ϴ��������ݿ⣬�μ�db����sql�ļ�
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import copy
import sys #Ҫ��������sys����Ϊ Python ��ʼ�����ɾ�� sys.setdefaultencoding �������
reload(sys) 
sys.setdefaultencoding('gbk')

sns.set()
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False  
plt.style.use('ggplot') 


def is_win(rank):   #������һ��Ϊʤ��
    label = 0
    if rank == 1:
        label = 1
    return label


if __name__ == '__main__':
    try:
        meta_data = pd.read_csv('C:\\Users\\***\\Desktop\\Context.csv', sep=',', header=0)#����Context���ļ�·��
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
    

    #��������ռǰ10%���������
    ranks = used_data['team_placement']  
    map(float,ranks)
    team_size = used_data['game_size']
    map(float,team_size)
    totalcount = 0
    for i in range(len(ranks)):       #ʹ��python����Ƚ�����������Hadoop����
        if float(float(ranks[i]) / float(team_size[i]))<0.1:
            totalcount = totalcount + 1
            print float(float(ranks[i]) / float(team_size[i]))
    print totalcount
    
    
    #print ranks
    
    #�ֱ�����˺����ڵ���100����ɱ������1���������ռ��
    x = used_data[used_data['player_dmg']>=100]['player_dmg']
    #y = used_data[used_data['team_placement']==1]['team_placement']
    z = used_data[used_data['player_kills']>1]['player_kills']
    print(x.size)
    #print(y.size)
    print(z.size)
    print('%.4f' %(float(x.size) / float(sum_count)))
    #print('%.4f' %(float(y.size) / float(sum_count)))#��������ķ�ʽ��������ռ��
    print('%.4f' %(float(z.size) / float(sum_count)))
    print("////////")



    #�Ը���90�ֵ���ҵģ������˺����ڵ���100��ռ��ͼ
    high_damage = float(x.size) / float(sum_count)
    plt.title('�˺�ռ��ͼ',fontsize = 14)
    plt.grid(True,linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
    plt.pie([1-high_damage,high_damage],labels=['<300','>=300'],autopct='%f%%',colors = ['#1C7ECE','#FF4D5B'],startangle = 120)
    plt.shouw()


    #������ɱ�������˺�������ʤ���Ĺ�ϵ�ֲ�,������ɱ�������˺�������ʤ���Ĺ�ϵ�ֲ�ͼ
    
    pro_unique_match_data = copy.deepcopy(used_data) #����һ������
    pro_unique_match_data['��ʤ'] = used_data['team_placement'].apply(is_win)
    g = sns.stripplot(data=pro_unique_match_data[['��ʤ', 'player_dmg', 'player_kills']], x='player_kills',y='player_dmg', hue='��ʤ')
    g.set(title='��ɱ�������˺�������ʤ���Ĺ�ϵ�ֲ�', xlabel='��ɱ����', ylabel='��ɵ��˺�')
    plt.tight_layout()
    plt.savefig('./pic/factors_vs_win.png', dpi=300)
    plt.grid(True,linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
    try:
        plt.show()
    except Exception as e:
        print('Error',e)
    

    #�����÷�ǰʮ����ҵ����ݣ������ݿ����ҳ��÷�ǰʮ����ң������������
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
    
    
    

