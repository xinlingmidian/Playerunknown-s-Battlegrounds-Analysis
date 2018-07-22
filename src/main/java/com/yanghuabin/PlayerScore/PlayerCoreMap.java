package com.yanghuabin.PlayerScore;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;


public class PlayerCoreMap extends Mapper<LongWritable, Text, Text, FloatWritable>{
	//Context 代表Map阶段上下文
	public void map(LongWritable ikey, Text ivalue, Context context) throws IOException, InterruptedException {
		String line = ivalue.toString();
		System.out.println(line);
		Float score = (float) 0;
		String player_name;
		//分隔字符串 （按照空格，换行符风格字符串）
		String[] values=line.split(",");
		
		if (values[0].compareTo("date")!=0)
		{
			player_name = values[11].toString();//玩家名称
			Float proportion = 40*(Float.parseFloat(values[14])-1)/(Float.parseFloat(values[1])-1);//40*(队伍排名-1)/(队伍总数-1)
			score = 100 - proportion;//基础分为60
			System.out.println(proportion);
			score += Float.parseFloat(values[10])*0.1f;//击杀人数加分，属于额外加分项
			score += Float.parseFloat(values[9])*0.01f;//玩家所造成的的伤害，属于额外加分项,更小也行
			context.write(new Text(player_name),new FloatWritable(score) );
			System.out.println(score);
			if (score>=90)
			{
				try {
					FileWriter fileWriter = new FileWriter(new File("C:\\Users\\Administrator\\Desktop\\Context.csv"),true);
					fileWriter.write(line+"\n");
					fileWriter.close();
				} catch (Exception e) {
					e.printStackTrace();
					System.out.print("输出得分大于90的玩家信息出错");
				}
			}
			
		}
		else {
			try {
				FileWriter fileWriter = new FileWriter(new File("C:\\Users\\Administrator\\Desktop\\Context.csv"),true);
				fileWriter.write(line+"\n");
				fileWriter.close();
			} catch (Exception e) {
				e.printStackTrace();
				System.out.print("输出第一行出错");
			}
		}
	}
}
