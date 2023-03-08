#pragma once

// TODO: Den Code richtig auf die cpp Datei aufteilen.
class SerialConnection
{
public:
	SerialConnection(std::string port, unsigned int baud_rate)
		: io(), serial(io, port)
	{
		serial.set_option(boost::asio::serial_port_base::baud_rate(baud_rate));
	}

    void writeString(std::string s);

    std::string readLine();

private:
	boost::asio::io_service io;
	boost::asio::serial_port serial;
};

