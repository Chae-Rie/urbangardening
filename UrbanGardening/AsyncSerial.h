#pragma once
class AsyncSerial : private boost::noncopyable
{
public:
    AsyncSerial();

    AsyncSerial(const std::string& devname, unsigned int baud_rate,
        boost::asio::serial_port_base::parity opt_parity =
        boost::asio::serial_port_base::parity(
            boost::asio::serial_port_base::parity::none),
        boost::asio::serial_port_base::character_size opt_csize =
        boost::asio::serial_port_base::character_size(8),
        boost::asio::serial_port_base::flow_control opt_flow =
        boost::asio::serial_port_base::flow_control(
            boost::asio::serial_port_base::flow_control::none),
        boost::asio::serial_port_base::stop_bits opt_stop =
        boost::asio::serial_port_base::stop_bits(
            boost::asio::serial_port_base::stop_bits::one));

    void open(const std::string& devname, unsigned int baud_rate,
        boost::asio::serial_port_base::parity opt_parity =
        boost::asio::serial_port_base::parity(
            boost::asio::serial_port_base::parity::none),
        boost::asio::serial_port_base::character_size opt_csize =
        boost::asio::serial_port_base::character_size(8),
        boost::asio::serial_port_base::flow_control opt_flow =
        boost::asio::serial_port_base::flow_control(
            boost::asio::serial_port_base::flow_control::none),
        boost::asio::serial_port_base::stop_bits opt_stop =
        boost::asio::serial_port_base::stop_bits(
            boost::asio::serial_port_base::stop_bits::one));

    bool isOpen() const;

    bool errorStatus() const;

    void close();

    void write(const char* data, size_t size);

    void write(const std::vector<char>& data);

    void writeString(const std::string& s);

    virtual ~AsyncSerial() = 0;
};

class BufferedAsyncSerial : public AsyncSerial
{
public:
    BufferedAsyncSerial();

    BufferedAsyncSerial(const std::string& devname, unsigned int baud_rate,
        boost::asio::serial_port_base::parity opt_parity =
        boost::asio::serial_port_base::parity(
            boost::asio::serial_port_base::parity::none),
        boost::asio::serial_port_base::character_size opt_csize =
        boost::asio::serial_port_base::character_size(8),
        boost::asio::serial_port_base::flow_control opt_flow =
        boost::asio::serial_port_base::flow_control(
            boost::asio::serial_port_base::flow_control::none),
        boost::asio::serial_port_base::stop_bits opt_stop =
        boost::asio::serial_port_base::stop_bits(
            boost::asio::serial_port_base::stop_bits::one));

    size_t read(char* data, size_t size);

    std::vector<char> read();

    std::string readString();

    std::string readStringUntil(const std::string delim = "\n");

    virtual ~BufferedAsyncSerial();
};

