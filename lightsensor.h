#ifndef LIGHTSENSOR_H
#define LIGHTSENSOR_H

class Lightsensor
{
private:
    /* data */
public:
    Lightsensor
(/* args */);
    ~Lightsensor
();
};

Lightsensor::Lightsensor(/* args */)
{
}

Lightsensor::~Lightsensor()
{
}

const int LIGHT_SENSOR_PIN{}; 
const int LED_PIN {};  
const int ANALOG_THRESHOLD{};
int analogValue = {};

#endif