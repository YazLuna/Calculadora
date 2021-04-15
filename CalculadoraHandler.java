import org.apache.thrift.TException;

public class CalculadoraHandler implements Calculadora.Iface  {
	@Override
	public double sumar(double numeroA, double numeroB) throws TException {
		return numeroA + numeroB;
	}

	@Override
	public double restar(double numeroA, double numeroB) throws TException {
		return  numeroA - numeroB;
	}

	@Override
	public double multiplicar(double numeroA, double numeroB) throws TException {
		return  numeroA * numeroB;
	}

	@Override
	public double dividir(double numeroA, double numeroB) throws TException {
		return  numeroA / numeroB;
	}

}