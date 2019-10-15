

# Client
class Smartphone(object):

    max_input_voltage = 5

    @classmethod
    def outcome(cls, input_voltage):
        if input_voltage > cls.max_input_voltage:
            print("Input voltage: {}V -- BURNING!!!".format(input_voltage))
        else:
            print("Input voltage: {}V -- Charging...".format(input_voltage))

    def charge(self, input_voltage):
        """Charge the phone with the given input voltage."""
        self.outcome(input_voltage)


# Supplier
class ISocket(object):
    output_voltage = None


class EUSocket(ISocket):
    print("EUSocket")
    output_voltage = 230


class USSocket(ISocket):
    print("USSocket")
    output_voltage = 120


class EUAdapter(object):
    """EUAdapter encapsulates client (Smartphone) and supplier (EUSocket)."""
    input_voltage = EUSocket.output_voltage
    output_voltage = Smartphone.max_input_voltage
    print("EU Adapter")


class USAdapter(object):
    """EUAdapter encapsulates client (Smartphone) and supplier (EUSocket)."""
    input_voltage = USSocket.output_voltage
    output_voltage = Smartphone.max_input_voltage
    print("US Adapter")


smartphone = Smartphone()
smartphone.charge(EUAdapter.output_voltage)

smartphone2 = Smartphone()
smartphone.charge(USAdapter.output_voltage)
