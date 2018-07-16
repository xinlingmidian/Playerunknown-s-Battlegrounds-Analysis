package com.yanghuabin.DeadPosition;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;


public class DeadPositionCount {

	public static void main(String[] args)  throws IOException, ClassNotFoundException, InterruptedException{
		Configuration conf = new Configuration();
		Job job = Job.getInstance(conf, "死亡热点位置统计");
		job.setJarByClass(com.yanghuabin.SafePosition.SafePositionCount.class);
		job.setMapperClass(DeadPositionMap.class);
		job.setReducerClass(DeadPositionReduce.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
       //输入路径必须存在，文件夹必须事先创建并上传好相关文件
		FileInputFormat.setInputPaths(job, new Path("hdfs://192.168.147.168:9000/input0"));
		//输出路径必须不存在，它自动创建输出
		FileOutputFormat.setOutputPath(job, new Path("hdfs://192.168.147.168:9000/output12"));
		if (!job.waitForCompletion(true))
			return;

	}

}
