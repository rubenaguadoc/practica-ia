import java.sql.*;
import java.util.ArrayList;

/**

    EXPLICACION :

    getDistanciaTren(int id); Pasado un ID devuelve un ArrayList<Integer> con la distancia de las 2 o 3 estaciones que rodean a la estacion ID

    getDistanciaRecta(int from, int to);
        from = id de la estacion de origen
        to = id de la estacion de destino

        >>> la variable from es siempre obligatoria, la variable to no lo es, si la variable to es positiva:
            >>> la funcion devuelve un ArrayList<Integer> con 1 solo valor, la distancia recta de la estacion FROM a la estacion TO
        >>> si la variable to es 0 o menor de 0
            >>> la funcion devuelve un ArrayList<Integer> con todas las distancias rectas de FROM.

*/

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
        if(to > 0)
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

            // TODO: Test para esto! Puede no funcar para nada :/
            if(miTo.equals(""))
                rs = st.executeQuery("SELECT * FROM recta WHERE DESTINO LIKE'" + miFrom + "'");
            else
                rs = st.executeQuery("SELECT * FROM recta WHERE DESTINO LIKE'" + miFrom + "' AND ORIGEN LIKE '" + miTo +"'");

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
