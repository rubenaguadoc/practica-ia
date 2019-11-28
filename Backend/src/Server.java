import static spark.Spark.post;

import java.util.ArrayList;

import static spark.Spark.options;
import static spark.Spark.before;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class Server {
    public static void main(String[] args) {
        options("/*", (request, response) -> {

            String accessControlRequestHeaders = request.headers("Access-Control-Request-Headers");
            if (accessControlRequestHeaders != null) {
                response.header("Access-Control-Allow-Headers", accessControlRequestHeaders);
            }

            String accessControlRequestMethod = request.headers("Access-Control-Request-Method");
            if (accessControlRequestMethod != null) {
                response.header("Access-Control-Allow-Methods", accessControlRequestMethod);
            }

            return "OK";
        });

        before((request, response) -> response.header("Access-Control-Allow-Origin", "*"));

        post("/", "application/json", (request, response) -> {
            ReqParams params = new Gson().fromJson(request.body(), ReqParams.class);

            // TODO: Change to algorithm call
            System.out.println(params.inicio);
            System.out.println(params.fin);
            System.out.println(params.hora);
            System.out.println(params.transbordos);

            ArrayList<ArrayList<Integer>> result = new ArrayList<>();
            ArrayList<Integer> stations = new ArrayList<>();
            ArrayList<Integer> lines = new ArrayList<>();
            stations.add(1);
            stations.add(2);
            stations.add(3);
            stations.add(4);
            stations.add(5);
            stations.add(6);

            lines.add(0); // Red
            lines.add(0);
            lines.add(1); // Yellow
            lines.add(1);
            lines.add(2); // Green
            lines.add(2);

            result.add(stations);
            result.add(lines);
            // TODO:

            String jsonResponse = new GsonBuilder().create().toJson(result);

            response.type("application/json");
            return jsonResponse;
        });
    }

}