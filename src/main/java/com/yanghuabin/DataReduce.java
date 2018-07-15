package com.yanghuabin;

import java.io.IOException;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;


public class DataReduce extends Reducer<Text, Text, Text, Text> {
	//private LongWritable result = new LongWritable();
	//public String s;
	public void reduce(Text _key, Iterable<Text> values, Context context)
			throws IOException, InterruptedException {
	
		//long sumtotal = 0;
		
		for (Text val:values)
		{
			//t.append(val.getBytes(), 0, 1);
			context.write(new Text(_key), val);
		}
		//result.set(sumtotal);
		

	}

}
