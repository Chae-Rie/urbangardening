#include "pch.h"
#include "AsyncSerial.h"

AsyncSerial::AsyncSerial()
{
}

AsyncSerial::AsyncSerial(const std::string& devname, unsigned int baud_rate, boost::asio::serial_port_base::parity opt_parity, boost::asio::serial_port_base::character_size opt_csize, boost::asio::serial_port_base::flow_control opt_flow, boost::asio::serial_port_base::stop_bits opt_stop)
{
}

void AsyncSerial::open(const std::string& devname, unsigned int baud_rate, boost::asio::serial_port_base::parity opt_parity, boost::asio::serial_port_base::character_size opt_csize, boost::asio::serial_port_base::flow_control opt_flow, boost::asio::serial_port_base::stop_bits opt_stop)
{
}

bool AsyncSerial::isOpen() const
{
	return false;
}

bool AsyncSerial::errorStatus() const
{
	return false;
}

void AsyncSerial::close()
{
}

void AsyncSerial::write(const char* data, size_t size)
{
}

void AsyncSerial::write(const std::vector<char>& data)
{
}

void AsyncSerial::writeString(const std::string& s)
{
}

// ------------------------------------------------------


BufferedAsyncSerial::BufferedAsyncSerial()
{
}

BufferedAsyncSerial::BufferedAsyncSerial(const std::string& devname, unsigned int baud_rate, boost::asio::serial_port_base::parity opt_parity, boost::asio::serial_port_base::character_size opt_csize, boost::asio::serial_port_base::flow_control opt_flow, boost::asio::serial_port_base::stop_bits opt_stop)
{
}

size_t BufferedAsyncSerial::read(char* data, size_t size)
{
	return size_t();
}

std::vector<char> BufferedAsyncSerial::read()
{
	return std::vector<char>();
}

std::string BufferedAsyncSerial::readString()
{
	return std::string();
}

std::string BufferedAsyncSerial::readStringUntil(const std::string delim)
{
	return std::string();
}

BufferedAsyncSerial::~BufferedAsyncSerial()
{
}
