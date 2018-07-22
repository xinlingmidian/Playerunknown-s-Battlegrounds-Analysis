package ItemTwo;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

//输出：字符- 整型

	public class ItemTwoMap extends Mapper<LongWritable, Text, Text, IntWritable>{
		
		private Text killby = new Text(); //map阶段输出的key
		
		public void map(LongWritable ikey, Text ivalue, Context context) throws IOException, InterruptedException {

			//map输入的value转为字符串，并按逗号把字符串分割  			
			String[] sp=  ivalue.toString().split(",");
			String str=sp[0];  //玩家死亡方式
			
			if(str!=null&&str.trim().length()>0){
				killby.set(str);
				context.write(killby, new IntWritable(1));	 //输出value为1			
			}
			
//			for (String str : sp) {
//				if(str!=null&&str.trim().length()>0)
//				killby.set(str);
//				context.write(killby, new IntWritable(1));
//			}
		}
				
	}


