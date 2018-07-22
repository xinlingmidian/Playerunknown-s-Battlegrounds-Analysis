package com.yanghuabin.distance;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

//输出：字符- 整型

	public class DistanceMap extends Mapper<LongWritable, Text, Text, IntWritable>{
		
		private Text killby = new Text(); //map阶段输出的key
		
		public void map(LongWritable ikey, Text ivalue, Context context) throws IOException, InterruptedException {
			
			//地图名称,   死亡方式,杀手X,杀手Y,玩家X,玩家Y(逗号分隔)
			
			//map输入的value转为字符串，并按逗号把字符串分割  			
			String[] sp=  ivalue.toString().split(","); // 死亡方式,杀手X,杀手Y,玩家X,玩家Y(逗号分隔)
			String str=sp[1];  //玩家死亡方式
			String killX=sp[2] ;//kill X
			String killY=sp[3]; //kill y
			String playX=sp[4]; //play x
			String playY=sp[5]; //play y
			
			if(sp.length<6||str==null||str.trim().length()<=0
					||killX==null||killX.trim().length()<=0
					||killY==null||killY.trim().length()<=0
					||playX==null||playX.trim().length()<=0
					||playX==null||playX.trim().length()<=0)
			{
				return;
			}
			double kx = Double.parseDouble(killX);
			double ky = Double.parseDouble(killY);
			double px = Double.parseDouble(playX);
			double py = Double.parseDouble(playY);
			double mindistance = 5;
			if(kx<mindistance||ky<mindistance||px<mindistance||py<mindistance)
			{
				return;
			}
			double distance = Math.pow( (kx-px)/100, 2)+Math.pow((ky-py)/100, 2);
			double limitMinDistance = 640000; //大于800米(狙击)
			
			if(distance >= limitMinDistance)
			{
				killby.set(str);
				context.write(killby, new IntWritable(1));	 //输出value为1			
			}

		}
				
	}

