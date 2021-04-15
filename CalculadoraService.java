import org.apache.thrift.TProcessor;
import org.apache.thrift.server.TServer;
import org.apache.thrift.server.TSimpleServer;
import org.apache.thrift.transport.TServerSocket;
import org.apache.thrift.transport.TTransportException;

public class CalculadoraService {
    public static void main(String[] args) throws TTransportException {
        TServerSocket transporte_servidor = new TServerSocket(8080);
        TProcessor procesador = new Calculadora.Processor<>(new CalculadoraHandler());
        TServer servidor = new TSimpleServer(new TSimpleServer.Args(transporte_servidor).processor(procesador));
        servidor.serve();
    }
}
