import java.sql.*;

public class base{

    Connection conn = null;

    public base(){
    }

    public String getNombreId(int id){
        connect();
        String name = "";
        try{
            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery("SELECT " + id + " FROM ids");

            name = rs.getString("ORIGEN");
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
        close();

        return name;
    }

    public boolean connect(){
        boolean res = false;
        try{
            String url = "jdbc:sqlite:../metroDataBase.db";
            conn = DriverManager.getConnection(url);
            res = conn.isValid(300);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return res;
    }

    public boolean close() {
        boolean res = false;
        try{
            if(conn != null){
                conn.close();
                res = conn.isClosed();
            }
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
        return res;
    }
}
