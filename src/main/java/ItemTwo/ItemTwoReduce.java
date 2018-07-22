package ItemTwo;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class ItemTwoReduce extends Reducer<Text, IntWritable, Text, IntWritable> {
	
	private IntWritable result = new IntWritable();
	//在进入到Reduce的时候，是已经排序过，所有key是相同数据的key,values 是一个列表,如：Vector ,{1,1,1}
	public void reduce(Text _key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
		// process values
		int total = 0;
		for (IntWritable val : values) {
			total = val.get() +total;
		}
		result.set(total); 
		context.write(_key, result);
	}

}