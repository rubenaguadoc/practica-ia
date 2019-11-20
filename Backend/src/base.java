import java.sql.*;
public class base{

    public base(){
        connect();
    }

    public String getNombreId(int id){
        return "PUTA VIDA TT";
    }

    public static void connect(){
        Connection conn = null;
        try{
            String url = "jdbc:sqlite:../metroDataBase.db";
            conn = DriverManager.getConnection(url);

            System.out.println("La conexion va como dios.");
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        } finally {
            try {
                if(conn != null){
                    conn.close();
                }
            } catch (SQLException ex){
                System.out.println(ex.getMessage());
            }
        }
    }
}
