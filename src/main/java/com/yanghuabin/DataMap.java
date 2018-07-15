package com.yanghuabin;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;


public class DataMap extends Mapper<Object, Text, Text, Text>{

	//private final static LongWritable one = new LongWritable(1);
	//private Text word = new Text();
	//private Text name = new Text();
	//Context 代表Map阶段上下文
	public void map(Object ikey, Text ivalue, Context context) throws IOException, InterruptedException {
		String line = ivalue.toString();
		String positionX = new String();
		String positionY = new String();
		int time = 0;
		//分隔字符串 （按照空格，换行符风格字符串）
		StringTokenizer itr = new StringTokenizer(line,"\n");
		String[] values=line.split(",");
		System.out.println(itr.toString());
		if (values[1].compareTo("time")!=0)
		{
			time = Integer.parseInt(values[1]);
			System.out.println(time);
		}
		else {
			time = 190;
		}
		if ((time<=180)&&values[0].compareTo("MIRAMAR")==0)
		{
			positionX = values[2];
			positionY = values[3];
			
			context.write(new Text(positionX),new Text(positionY));
		}
		//values[7].compareTo("180")==-1&&
		
		
		/*while (itr.hasMoreTokens()) {
			//StringTokenizer tokenzerline = new StringTokenizer(itr.nextToken(),",");
			if (values[i])
			while (itr.l){
				//String killerBy = tokenzerline.nextToken();
				String killerName = tokenzerline.nextToken(",");
				word.set(killerName);
				//name.set(killerName);
				context.write(word, one);
			}
		}*/
		
//		String[] values=ivalue.toString().split(" ");
//		for (String str : values) {
//			word.set(str);
//			context.write(word, one);
//		}
	}
}
