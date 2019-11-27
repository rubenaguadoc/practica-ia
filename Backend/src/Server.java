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

            ArrayList<Integer> result = new ArrayList<>();
            result.add(1);
            result.add(2);
            result.add(3);
            result.add(4);
            // TODO:

            String jsonResponse = new GsonBuilder().create().toJson(result);

            response.type("application/json");
            return jsonResponse;
        });
    }

}