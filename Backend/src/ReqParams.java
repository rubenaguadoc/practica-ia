
public class ReqParams {

  public final int inicio;
  public final int fin;
  public final String hora;
  public final Boolean transbordos;

  public ReqParams(int inicio, int fin, String hora, Boolean transbordos) {
    this.inicio = inicio;
    this.fin = fin;
    this.hora = hora;
    this.transbordos = transbordos;
  }

}