import java.sql.*;
import java.util.HashMap;

public class base {

    Connection conn = null;

    public base() {
    }

    public HashMap<Integer, Integer> obtenerNodos() {
        connect();
        HashMap<Integer, Integer> nodos = new HashMap<>();
        try {
            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery("SELECT ID, LINEA FROM ids");
            while (rs.next())
                nodos.put(rs.getInt(1), rs.getInt(2));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        close();
        return nodos;
    }

    public HashMap<Integer, Integer> getDistanciaTren(int id) {
        HashMap<Integer, Integer> codo = new HashMap<>();

        connect();
        try {
            Statement st = conn.createStatement();
            ResultSet rs = st.executeQuery("SELECT DESTINO, DISTANCIA FROM tren WHERE ORIGEN = " + id);
            while (rs.next()){
                codo.put(rs.getInt(1), rs.getInt(2));
            }
            rs = st.executeQuery("SELECT ORIGEN, DISTANCIA FROM tren WHERE DESTINO = " + id);
            while (rs.next()){
                codo.put(rs.getInt(1), rs.getInt(2));
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        close();

        return codo;
    }

    public int getDistanciaRecta(int from, int to) {
        int recta = 0;

        connect();
        try {
            Statement st = conn.createStatement();
            ResultSet rs = null;

            rs = st.executeQuery("SELECT DISTANCIA FROM recta WHERE ORIGEN = " + from + " AND DESTINO = " + to);
            if (rs.next()) {
                recta = rs.getInt(1);
            } else {
                rs = st.executeQuery("SELECT DISTANCIA FROM recta WHERE DESTINO = " + from + " AND ORIGEN = " + to);
                recta = rs.getInt(1);
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
