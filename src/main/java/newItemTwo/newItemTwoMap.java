package newItemTwo;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

// goal:对上一步map/reduce的结果进行排序（按照上一步reduce输出的value值进行排序）
/* map阶段：
                 输入：key -LongWritable    value -Text
                 输出：key -IntWritable     value -Text (按照key排序)
   reduce阶段:
                输入：key -IntWritable     value -Text
                输出：key -Text            value -IntWritable 
*/
	public class newItemTwoMap extends Mapper<LongWritable, Text, IntWritable,Text>{
		
		private Text deathWay = new Text(); 			  //玩家死亡方式
		private IntWritable totalNum = new IntWritable(); //该方式下玩家死亡总人数
				
		public void map(LongWritable ikey, Text ivalue, Context context) throws IOException, InterruptedException {

			//map输入的value转为字符串，并按逗号把字符串分割  			
			String[] sp=  ivalue.toString().split(",");
			String str0 =sp[0];  //死亡方式
			String str1 =sp[1];  //死亡人数
			
			if(str0!=null&&str0.trim().length()>0 && str1!=null&&str1.trim().length()>0){
				int Num=Integer.parseInt(str1);
				deathWay.set(str0);
				totalNum.set(Num);
				context.write(totalNum, deathWay);				
			}
			

		}
				
	}



