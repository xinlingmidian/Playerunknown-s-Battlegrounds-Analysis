package com.yanghuabin.DeadPosition;

import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;


public class DeadPositionReduce extends Reducer<Text, Text, Text, Text> {

	public void reduce(Text _key, Iterable<Text> values, Context context)
			throws IOException, InterruptedException {
		for (Text val:values)
		{
			context.write(new Text(_key), val);//不用对数据进行操作修改
		}

	}

}
