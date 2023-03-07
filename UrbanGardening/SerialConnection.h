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
	void writeString(std::string s)
	{
		boost::asio::write(serial, boost::asio::buffer(s.c_str(), s.size()));
	}

    std::string readLine()
    {
        // Erstmal nur die Daten char für char auslesen, so simple wie möglich
        using namespace boost;
        char c;
        std::string result;
        for (;;)
        {
            asio::read(serial, asio::buffer(&c, 1));
            switch (c)
            {
            case '\r':
                break;
            case '\n':
                return result;
            default:
                result += c;
            }
        }
    }

private:
	boost::asio::io_service io;
	boost::asio::serial_port serial;
};

