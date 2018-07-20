package com.yanghuabin.PlayerScore;

import java.io.File;
import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;


public class PlayerScoreCount {
	public File file ;
	PlayerScoreCount() {
		try {
			file = new File("C:\\Users\\Administrator\\Desktop\\Context.csv");
			if (!file.exists()) {
				file.createNewFile();
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	public static void main(String[] args)  throws IOException, ClassNotFoundException, InterruptedException{
		Configuration conf = new Configuration();
		Job job = Job.getInstance(conf, "玩家分数统计");
		job.setJarByClass(com.yanghuabin.PlayerScore.PlayerScoreCount.class);
		job.setMapperClass(PlayerCoreMap.class);
		job.setReducerClass(PlayerScoreReduce.class);
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(FloatWritable.class);
		
       //输入路径必须存在，文件夹必须事先创建并上传好相关文件
		FileInputFormat.setInputPaths(job, new Path("hdfs://192.168.147.168:9000/itemFive-input"));
		//输出路径必须不存在，它自动创建输出
		FileOutputFormat.setOutputPath(job, new Path("hdfs://192.168.147.168:9000/itemFive-output"));
		if (!job.waitForCompletion(true))
			return;

	}

}
