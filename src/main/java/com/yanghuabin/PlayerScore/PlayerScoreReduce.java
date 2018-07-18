package com.yanghuabin.PlayerScore;

import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;


public class PlayerScoreReduce extends Reducer<Text, FloatWritable, Text, FloatWritable> {
	public void reduce(Text _key, Iterable<FloatWritable> values, Context context)
			throws IOException, InterruptedException {
		FloatWritable average = new FloatWritable();
		float sum = 0f,i=0f;
		for (FloatWritable val:values)
		{
			sum += val.get();
			i++;
		}
		average.set(sum/i);
		context.write(_key, average);//求平均分数
	}

}
