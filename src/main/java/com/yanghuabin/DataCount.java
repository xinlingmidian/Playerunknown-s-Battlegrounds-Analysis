package com.yanghuabin;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;


public class DataCount {

	public static void main(String[] args)  throws IOException, ClassNotFoundException, InterruptedException{
		Configuration conf = new Configuration();
		Job job = Job.getInstance(conf, "位置统计");
		job.setJarByClass(com.yanghuabin.DataCount.class);
		job.setMapperClass(DataMap.class);
		job.setReducerClass(DataReduce.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
       //输入路径必须存在
		FileInputFormat.setInputPaths(job, new Path("hdfs://192.168.147.168:9000/input0"));
		//输出路径必须不存在，它自动创建输出
		FileOutputFormat.setOutputPath(job, new Path("hdfs://192.168.147.168:9000/output11"));
		if (!job.waitForCompletion(true))
			return;

	}

}
