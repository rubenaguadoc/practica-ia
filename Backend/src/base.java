import java.sql.*;
import java.util.ArrayList;

/**
 * 
 * EXPLICACION :
 * 
 * getDistanciaTren(int id); Pasado un ID devuelve un ArrayList<Integer> con la
 * distancia de las 2 o 3 estaciones que rodean a la estacion ID
 * 
 * getDistanciaRecta(int from, int to); from = id de la estacion de origen to =
 * id de la estacion de destino
 * 
 * >>> la variable from es siempre obligatoria, la variable to no lo es, si la
 * variable to es positiva: >>> la funcion devuelve un ArrayList<Integer> con 1
 * solo valor, la distancia recta de la estacion FROM a la estacion TO >>> si la
 * variable to es 0 o menor de 0 >>> la funcion devuelve un ArrayList<Integer>
 * con todas las distancias rectas de FROM.
 * 
 */

public class base {

    Connection conn = null;

    public base() {
    }

    public ArrayList<Integer> obtenerNodos() {
        connect();
        ArrayList<Integer> nodos = new ArrayList<>();
        try {
            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery("SELECT ID FROM ids");
            while (rs.next())
                nodos.add(rs.getInt(1));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        close();
        return nodos;
    }

    public String getNombreId(int id) {
        connect();
        String name = "";
        try {
            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery("SELECT * FROM ids WHERE ID=" + id);

            name = rs.getString(2); // 2 hace referencia a la columna de los NOMBRES
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        close();

        return name;
    }

    public ArrayList<Integer> getDistanciaTren(int id) {
        String estacion = getNombreId(id);
        ArrayList<Integer> codo = new ArrayList<>();

        connect();
        try {
            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery(
                    "SELECT * FROM tren WHERE ORIGEN LIKE'" + estacion + "' OR DESTINO LIKE'" + estacion + "'");
            while (rs.next())
                codo.add(rs.getInt(4));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        close();

        return codo;
    }

    public int getDistanciaRecta(int from, int to) {
        String miFrom = getNombreId(from);
        String miTo = getNombreId(to);
        int recta = 0;

        connect();
        try {
            Statement st = conn.createStatement();
            ResultSet rs = null;

            rs = st.executeQuery(
                    "SELECT * FROM recta WHERE ORIGEN LIKE'" + miFrom + "' AND DESTINO LIKE '" + miTo + "'");
            if (rs.next()) {
                recta = rs.getInt(4);
            } else {
                rs = st.executeQuery(
                        "SELECT * FROM recta WHERE DESTINO LIKE'" + miFrom + "' AND ORIGEN LIKE '" + miTo + "'");
                recta = rs.getInt(4);
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        close();

        return recta;
    }

    public boolean connect() {
        boolean res = false;
        try {
            String url = "jdbc:sqlite:./metroDataBase.db";
            conn = DriverManager.getConnection(url);
            res = conn.isValid(300);
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
        return res;
    }

    public boolean close() {
        boolean res = false;
        try {
            if (conn != null) {
                conn.close();
                res = conn.isClosed();
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        return res;
    }
}
