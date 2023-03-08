#include "pch.h"
#include "SerialConnection.h"

void SerialConnection::writeString(std::string s)
{
    boost::asio::write(serial, boost::asio::buffer(s.c_str(), s.size()));
}

std::string SerialConnection::readLine()
{
    // Erstmal nur die Daten char f�r char auslesen, so simple wie m�glich
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
    return std::string();
}
