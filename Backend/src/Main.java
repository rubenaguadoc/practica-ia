import es.upm.aedlib.graph.Edge;
import es.upm.aedlib.graph.Vertex;
import es.upm.aedlib.graph.DirectedGraph;
import es.upm.aedlib.graph.DirectedAdjacencyListGraph;
import java.util.HashMap;
import java.util.ArrayList;
import es.upm.aedlib.map.HashTableMap;

public class Main{

    DirectedGraph<Integer,Integer> graph = new DirectedAdjacencyListGraph <Integer,Integer> ();
    HashTableMap <Integer, Vertex<Integer>> vertices = new HashTableMap <Integer, Vertex<Integer>> ();


    private void crearGrafo (){
	//INSERTAR NODOS AL GRAFO
	ArrayList<Integer> nodos = new ArrayList<Integer>();

	for (int i = 0; i < nodos.size(); i++){
	    vertices.put(nodos.get(i),graph.insertVertex(new Integer(nodos.get(i))));
	}
	//METER LOS PESOS AL GRAFO
	for (Vertex<Integer> v : graph.vertices()) {
	    HashMap<Integer, Integer> prox = new HashMap<Integer, Integer>();
	    for (Integer v2 : prox.keySet()) {
		graph.insertEdge(v, vertices.get(v2), prox.get(v2));
	    }
	}
    }


    private void bestPath (){
    }


    private int[]  getPath (int from, int to) {
	int[] a = new int[2];
	return a;
    }

    public static void main (String [] args){
        base miBase = new base();
        String nombre = miBase.getNombreId(9);
        System.out.println("Output :: " + nombre);
    }
}
