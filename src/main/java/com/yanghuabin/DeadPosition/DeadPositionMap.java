package com.yanghuabin.DeadPosition;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;


public class DeadPositionMap extends Mapper<Object, Text, Text, Text>{
	//Context 代表Map阶段上下文
	public void map(Object ikey, Text ivalue, Context context) throws IOException, InterruptedException {
		String line = ivalue.toString();
		String positionX = new String();
		String positionY = new String();
		//分隔字符串 （按照空格，换行符风格字符串）
		StringTokenizer itr = new StringTokenizer(line,"\n");
		String[] values=line.split(",");
		System.out.println(itr.toString());
		if (values[0].compareTo("MIRAMAR")==0)//筛选地图为"MIRAMAR"的数据，并选出玩家存活时间小于180s的数据
		{                                                  //其余数据可以相应修改地图的筛选条件
			positionX = values[2];
			positionY = values[3];	
			context.write(new Text(positionX),new Text(positionY));
		}
	}
}
