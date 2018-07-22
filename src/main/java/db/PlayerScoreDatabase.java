package db;


import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class PlayerScoreDatabase  {
	String url ="jdbc:mysql://localhost:3306/test"; //所存的数据库名为test
    String driver="com.mysql.jdbc.Driver";
    String user = "root";  
    String password = "******";  //数据库的密码
    Connection conn=null;
    PreparedStatement ps=null;
    ResultSet resultSet=null;


	public void connectionDB() {

		try {
			Class.forName(driver);
			conn = DriverManager.getConnection(url, user, password);
			System.out.println("Successfully connected");
		} catch (ClassNotFoundException e) {

			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		}

	}

	public void WriteContextIntoDB() throws IOException {
		// 1.将大文本插入到数据库，只需要读出 文本插入即可
		String insertsql = "insert into playername value(?,?)";//表中共两列，第一列为name,第二列为score
		File file = new File("C:\\Users\\****\\Desktop\\test");//前一步由Hadoop计算出的游戏玩家分数信息，将其重命名为test
		BufferedReader reader = null;
		try {
			ps = conn.prepareStatement(insertsql);
			String temp = null;
			String[] date = null ;
			reader = new BufferedReader(new FileReader(file));
			while((temp=reader.readLine())!=null)
			{
				date = temp.toString().split("\t");
				ps.setString(1, date[0]);
				ps.setFloat(2, Float.parseFloat(date[1]));
				ps.execute();
			}
			// 使用setCharacterStream()设置字符流			
			//ps.setCharacterStream(1, fileReader, (int) file.length());
			System.out.println("成功向数据库插入文本 ");
		} catch (SQLException e) {
			System.out.println("SQLException");
			e.printStackTrace();
		} catch (FileNotFoundException e) {
			System.out.println("FileNotFoundException ");
			e.printStackTrace();
		}finally {
			if (reader!=null)
			{
				try {
					reader.close();
				} catch (Exception e2) {
					e2.printStackTrace();
				}
			}
		}

	}

	// 2.从数据读出文本内在写到磁盘
	public void ReadContextFromDB() {

		try {
			String sql = "select*from playername where score >= 90 order by score desc";//选择超过90分的玩家数据，为分析做准备
			//SELECT * FROM `playername` WHERE score >= 90 ORDER BY `score` DESC
			ps = conn.prepareStatement(sql);
			ps.executeQuery();
			resultSet = ps.getResultSet();
			// 写入到目标文件
			FileWriter fileWriter = new FileWriter(new File("C:\\Users\\****\\Desktop\\inputContext.txt"));
			while (resultSet.next()) {	
				String fname = resultSet.getString("name");
				String fscore = resultSet.getString("score");
				fileWriter.write(fname+"\t"+fscore+"\n");  //数据的存入格式
			}
			fileWriter.close();

		} catch (SQLException e) {
			System.out.println("SQLException");
			e.printStackTrace();
		} catch (IOException e) {
			System.out.println("IOException");
			e.printStackTrace();
		}
	}

	public static void main(String[] args) throws IOException {
		PlayerScoreDatabase  t = new PlayerScoreDatabase ();
        t.connectionDB();
        //t.WriteContextIntoDB();                      //往数据库写入数据
        //System.out.println("写入成功，请到数据库查看");  
        t.ReadContextFromDB();
        System.out.println("写入成功，请到桌面查看");
	}
}


