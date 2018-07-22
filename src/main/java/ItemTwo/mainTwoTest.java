package ItemTwo;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class mainTwoTest {

	public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {
		
		Configuration conf = new Configuration();
		//自定义键值对分隔符
		conf.set("mapred.textoutputformat.ignoreseparator","true");
		conf.set("mapred.textoutputformat.separator",",");		
		
		Job job = Job.getInstance(conf, "ItemTwo");
		
		job.setJarByClass(ItemTwo.mainTwoTest.class); //设置执行任务的主类
		job.setMapperClass(ItemTwoMap.class);    //设置map的类
		job.setCombinerClass(ItemTwoReduce.class); // 因为hadoop是一个分布式，所有它会在每个节点进行一个预处理
		job.setReducerClass(ItemTwoReduce.class);  //设置Reduce 类 ，最终的结果输出
		
		job.setOutputKeyClass(Text.class);      //告诉最终输出的key是什么类型              （  字符串）
		job.setOutputValueClass(IntWritable.class); //输出的value是什么类型             （整型）
		
//==============    项目数据运行：   ============================		(10mins)
         //告诉MapReduce执行什么数据作为输入，这里的路径必须是HDFS的路径
		FileInputFormat.setInputPaths(job, new Path("hdfs://192.168.147.168:9000/itemTwo-input"));
		 //路径中的目录必须不存在，需要它自己创建，否则会提示错误
		FileOutputFormat.setOutputPath(job, new Path("hdfs://192.168.147.168:9000/itemTwo-result1"));
	
//==============    测试用例：   ================================		
	//	FileInputFormat.setInputPaths(job, new Path("hdfs://192.168.147.168:9000/test0/问题2"));		
	//	FileOutputFormat.setOutputPath(job, new Path("hdfs://192.168.147.168:9000/testOut2.2"));
		
		if (!job.waitForCompletion(true)){
			
			System.out.println("\n\nOK!");
			return;
		}
	}
}
