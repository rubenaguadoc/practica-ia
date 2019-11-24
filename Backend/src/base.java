import java.sql.*;
import java.util.ArrayList;

public class base{

    Connection conn = null;

    public base(){
    }

    public String getNombreId(int id){
        connect();
        String name = "";
        try{
            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM ids WHERE ID=" + id);

            name = rs.getString(2); // 2 hace referencia a la columna de los NOMBRES
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
        close();

        return name;
    }

    public ArrayList<Integer> getDistanciaTren(int id){
        String estacion = getNombreId(id);
        ArrayList<Integer> codo = new ArrayList<>();

        connect();
        try{
            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM tren WHERE ORIGEN LIKE'" + estacion + "' OR DESTINO LIKE'" + estacion + "'");
            while(rs.next())
                codo.add(rs.getInt(4));
        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
        close();

        return codo;
    }

    public ArrayList<Integer> getDistanciaRecta(int from, int to){
        String miFrom = getNombreId(from);
        String miTo = "";
        if(to != -1)
            miTo = getNombreId(to);

        ArrayList<Integer> recta = new ArrayList<>();

        connect();
        try{
            Statement st = conn.createStatement();
            ResultSet rs = null;
            if(miTo.equals(""))
                rs = st.executeQuery("SELECT * FROM recta WHERE ORIGEN LIKE'" + miFrom + "'");
            else
                rs = st.executeQuery("SELECT * FROM recta WHERE ORIGEN LIKE'" + miFrom + "' AND DESTINO LIKE '" + miTo +"'");

            while(rs.next()){
                recta.add(rs.getInt(4));
            }

        }
        catch(Exception e){
            System.out.println(e.getMessage());
        }
        close();

        return recta;
    }

    public boolean connect(){
        boolean res = false;
        try{
            String url = "jdbc:sqlite:/home/jorge/Documentos/AA-UNI/IA/practica-ia/Backend/metroDataBase.db";
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
