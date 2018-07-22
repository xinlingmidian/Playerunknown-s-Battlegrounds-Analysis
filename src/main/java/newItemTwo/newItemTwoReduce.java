package newItemTwo;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class newItemTwoReduce extends Reducer< IntWritable,Text,Text, IntWritable> {
	
	public void reduce(IntWritable _key, Text value, Context context) throws IOException, InterruptedException {
//		// process values
//		int total = 0;
//		for (IntWritable val : values) {
//			total = val.get() +total;
//		}
//		result.set(total); 
//		context.write(_key, result);
//	}
		
     //	context.write(value, _key);  //输出：<死亡方式，人数>
		context.write(value,_key);
	}
}
